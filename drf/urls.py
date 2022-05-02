from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'requirements', views.RequirementsViewSet)
router.register(r'donate', views.DonateViewSet)


# url

urlpatterns = [
    # ngo section
    path('ngo', views.ngo, name='ngo'),

    path('', include(router.urls)),

    # donor section
    path('donor', views.donor, name='donor'),

]
