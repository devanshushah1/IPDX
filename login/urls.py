from django.urls import path
from . import views

# app_name = 'login'

urlpatterns = [
    path('', views.home, name="home"),
    path('index/', views.index, name='index'),
    # registration and login
    path('ngo_signup', views.NgoSignUpView.as_view(), name='ngo_signup'),
    path('donor_signup', views.DonorSignUpView.as_view(), name='donor_signup'),
    path('login', views.login, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('chat', views.chatUser, name='chat'),

]
