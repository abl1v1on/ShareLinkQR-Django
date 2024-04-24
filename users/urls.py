from django.urls import path

from . import views

app_name = 'user'

urlpatterns = [
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('signup/', views.SignUpUserView.as_view(), name='signup'),
]
