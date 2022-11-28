from django.urls import path

from . import views

urlpatterns = [
    path('', views.homeView, name='home'),
    path('create', views.createTour, name='create-tour'),
    path('<slug:pk>/update', views.updateTour, name='update-tour')
]
