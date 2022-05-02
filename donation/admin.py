from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.datetime_safe import datetime
from .models import *
# Register your models here.

"""class ReqAdmin(admin.ModelAdmin):
    # Overide of the save model
    def save_model(self, request, obj, form, change):
        obj.requirements.quantity += obj.quantity
        obj.donated.count += obj.quantity
        obj.requirements.updated_quantity = datetime.now()
        obj.cart.save()
        super().save_model(request, obj, form, change)"""

admin.site.register(User, UserAdmin)
admin.site.register(Ngos)
admin.site.register(Donors)
admin.site.register(Requirements)
admin.site.register(Donated)