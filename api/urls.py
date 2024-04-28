from django.urls import path

from . import views

app_name = 'apiv1'

urlpatterns = [
    path('social-networks/', views.social_networks_view, name='social_networks'),
]
