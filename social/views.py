from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import AddSocialNetworkForm
from .utils import QRCode, social_utils


@login_required
def index(request):
    social_networks = social_utils.get_social_networks_by_filter(user_id=request.user.id)

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
            if social_utils.get_social_networks_by_filter(user_id=request.user.id, name=cd['name']).exists():
                social_utils.get_social_networks_by_filter(user_id=request.user.id, name=cd['name']).delete()
            social_utils.create_social_network(name=cd['name'], link=cd['link'], user_id=request.user.id)
            return redirect('social:home')
    else:
        form = AddSocialNetworkForm()
    return render(request, 'add-social-network.html', {'title': 'Добавить соц. сеть', 'form': form})


@login_required
def qr_code_view(request):
    qr = QRCode()
    qr.generate_qrcode(request)

    context = {
        'title': 'Мой QR код',
        'path_to_qrcode': qr.get_filename(),
    }
    return render(request, 'user-qr-code.html', context)


def social_networks_view(request, user_id):
    if social_utils.get_social_networks_by_filter(user_id=user_id).exists():
        social_networks = social_utils.get_social_networks_by_filter(user_id=user_id)
    else:
        return redirect('social:home')

    context = {
        'title': f'Соц. сети пользователя {get_user_model().objects.get(pk=user_id).username}',
        'social_networks': social_networks
    }
    return render(request, 'social-network-list.html', context)

# Удалил запросы к бд