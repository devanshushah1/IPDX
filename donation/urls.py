from django.urls import path, include
from . import views
from .views import *
from rest_framework.routers import DefaultRouter

#router = DefaultRouter()
#router.register('ngo', views.NgoViewSet, basename='ngo')

urlpatterns = [
    path('ngo_signup/', views.NgoSignUp, name="NgoSignUp"),
    path('donor_signup/', views.DonorSignUp, name="DonorSignUp"),
    path('', views.SignUp, name="signup"),
    path('login/', views.Login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('ngo/',views.NgoPage,name="ngo"),
    path('donor/',views.DonorPage,name="donor"),
    path('donor/<int:pk>/',views.DonorView.as_view(),name="donor_detail"),
    path('ngo/<int:pk>/',views.NgoView.as_view(),name="ngo_detail"),
    path('upload_req/<int:id>/',views.upload_requirement,name="upload_req"),
    path('req_list/<int:id>/',views.req_list,name="req_list"),
    path('req_list_backup/<int:id>/', views.req_list_backup, name="req_list_backup"),
    path('edit/<int:id>/',views.edit,name="edit"),
    path('delete/<int:id>/',views.delete,name="delete"),
    path('done/<int:id>/', views.done, name="done"),
    path('undone/<int:id>/', views.undone, name="undone"),
    path('req_list_donor/',views.req_list_donors,name="req_list_donor"),
    path('donate/<int:id>/', views.donate, name="donate"),
    path('donated_list/<int:id>/',views.donated_list,name="donated_list"),
    path('donated_list_donor/<int:id>/',views.donated_list_donor,name="donated_list_donor"),

    path('generic/ngos/<int:user_id>/', views.GenericAPIView.as_view()),
    path('ngo_drf/', NgoAPIView.as_view(), name="ngo_drf"),
    path('ngo_drf/<int:id>/', NgoDetails.as_view(), name="detail"),
    path('donor_drf/', DonorAPIView.as_view()),
    path('donor_drf/<int:id>/', DonorDetails.as_view()),
path('req_drf/', ReqAPIView.as_view()),
]