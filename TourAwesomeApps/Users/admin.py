from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser, Booking

admin.site.register(MyUser, UserAdmin)
admin.site.register(Booking)


