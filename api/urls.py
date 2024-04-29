from django.urls import path

from . import views

app_name = 'apiv1'

urlpatterns = [
    path('social-networks/', views.SocialNetworksListAPIView.as_view(), name='social_networks'),
    path('social-networks/<int:user_id>/', views.get_user_social_networks, name='user_social_networks'),
]
