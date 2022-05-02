from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings
from django.urls import reverse
# Create your models here.

class User(AbstractUser):
    is_ngo = models.BooleanField(default=False)
    is_donor = models.BooleanField(default=False)

class Donors(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=200, null=True, default='XYZ')
    phone = models.IntegerField()
    def __str__(self):
        return self.name
    def get_absolute_url(self):
       return reverse('donation:donor_detail', kwargs={'pk': self.pk})

class Ngos(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=200, null=True, default='NGO')
    phone = models.IntegerField()
    donors =models.ForeignKey(Donors, null=True, on_delete=models.SET_NULL)
    def get_absolute_url(self):
        return reverse('donation:ngo_detail', kwargs={'pk': self.pk})
    def __str__(self):
        return self.name

class Requirements(models.Model):
    CATEGORIES= (
        ('Medicine', 'Medicine'),
        ('Food', 'Food'),
        ('Clothing', 'Clothing'),
        ('Stationary', 'Stationary'),
    )
    ngo = models.ForeignKey(Ngos, null=True, blank=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORIES, blank=True, null=True)
    quantity = models.FloatField()
    donated_quantity = models.IntegerField(null=True)

    def __str__(self):
        return self.name

class Donated(models.Model):
    requirements = models.ForeignKey(Requirements, null=True, blank=True, on_delete=models.CASCADE)
    ngo = models.ForeignKey(Ngos, null=True, blank=True, on_delete=models.CASCADE)
    donor = models.ForeignKey(Donors, null=True, blank=True, on_delete=models.CASCADE)
    count = models.IntegerField()
    def __str__(self):
        return str(self.requirements)




