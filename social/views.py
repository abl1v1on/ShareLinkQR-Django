from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import qrcode

from .forms import AddSocialNetworkForm
from .models import SocialNetwork


@login_required
def index(request):
    social_networks = SocialNetwork.objects.filter(user_id=request.user.id)

    context = {
        'title': 'Мои социальные сети',
        'social_networks': social_networks
    }
    return render(request, 'index.html', context)


@login_required
def add_social_network(request):
    if request.method == 'POST':
        form = AddSocialNetworkForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if SocialNetwork.objects.filter(user_id=request.user.id, name=cd['name']).exists():
                SocialNetwork.objects.filter(user_id=request.user.id, name=cd['name']).delete()
            SocialNetwork.objects.create(name=cd['name'], link=cd['link'], user_id=request.user.id)
            return redirect('social:home')
    else:
        form = AddSocialNetworkForm()
    return render(request, 'add-social-network.html', {'title': 'Добавить соц. сеть', 'form': form})


@login_required
def qr_code_view(request):
    url = f'http://127.0.0.1:8000/social-networks/{request.user.id}/'
    filename = f'static/qrCodes/{request.user.username}_qrcode.png'
    img = qrcode.make(url)
    img.save(filename)

    context = {
        'title': 'Мой QR код',
        'path_to_qrcode': filename,
    }
    return render(request, 'user-qr-code.html', context)


@login_required
def social_networks_view(request, user_id):
    if SocialNetwork.objects.filter(user_id=user_id).exists():
        social_networks = SocialNetwork.objects.filter(user_id=user_id)
    else:
        return redirect('social:home')

    context = {
        'title': f'Соц. сети пользователя {get_user_model().objects.get(pk=user_id).username}',
        'social_networks': social_networks
    }
    return render(request, 'social-network-list.html', context)
