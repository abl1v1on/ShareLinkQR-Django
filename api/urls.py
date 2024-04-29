from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView

from . import views

app_name = 'apiv1'

urlpatterns = [
    path('token/', views.MyTokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('register/', views.RegisterView.as_view()),
    path('social-networks/', views.get_social_networks)
]

