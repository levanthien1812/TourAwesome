from django.urls import path

from . import views

urlpatterns = [
    path('', views.homeView, name='home'),
    path('create', views.createTour, name='create-tour'),
    path('<slug:pk>', views.getTour, name='get-tour'),
    path('<slug:location>', views.getTour, name='get-location-tours'),
    path('<slug:pk>/update', views.updateTour, name='update-tour'),
    path('<slug:pk>/delete', views.deleteTour, name='delete-tour'),
    path('<slug:pk>/book', views.bookTour, name='book-tour'),
]
