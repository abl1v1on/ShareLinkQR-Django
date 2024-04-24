from django import forms

from .models import SocialNetwork, SOCIAL_NETWORK_CHOICES


class AddSocialNetworkForm(forms.ModelForm):
    name = forms.ChoiceField(choices=SOCIAL_NETWORK_CHOICES,
                             widget=forms.Select(attrs={'class': 'form-select w-25 mt-3',
                                                        'style': 'margin: 0 auto'}))
    link = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control w-25 mt-3', 'style': 'margin: 0 auto',
                                                       'placeholder': 'Введите ссылку'}))

    class Meta:
        model = SocialNetwork
        fields = ('name', 'link')
