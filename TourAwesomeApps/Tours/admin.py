from django.contrib import admin
from .models import Tour, TourImage, TourVehicle

# Register your models here.
admin.site.register(Tour)
admin.site.register(TourImage)
admin.site.register(TourVehicle)
