from django.urls import path
from . import views

app_name = 'social'

urlpatterns = [
    path('', views.index, name='home'),
    path('add-social-network/', views.add_social_network, name='add_social_network'),
    path('qr-code/', views.qr_code_view, name='qr_code'),
    path('social-networks/<int:user_id>/', views.social_networks_view, name='social_networks'),
]

