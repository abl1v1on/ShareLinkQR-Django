import qrcode
from .models import SocialNetwork


class QRCode:
    def __init__(self):
        self.filename = ''

    def generate_qrcode(self, request):
        url = f'http://192.168.0.107:8000/social-networks/{request.user.id}/'
        self.filename = f'static/qrCodes/{request.user.username}_qrcode.png'
        img = qrcode.make(url)
        img.save(self.filename)

    def get_filename(self):
        return self.filename


class SocialNetworkUtils:
    def __init__(self):
        self.model = SocialNetwork

    def get_social_networks(self):
        return self.model.objects.all()
    
    def get_social_networks_by_filter(self, **kwargs):
        return self.get_social_networks().filter(**kwargs)

    def create_social_network(self, **kwargs):
        return self.model.objects.create(**kwargs)


social_utils = SocialNetworkUtils()

# Создал utils