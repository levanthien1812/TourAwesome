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
    path('introduce/', views.introduce, name='introduce'),
    path('<slug:pk>/add-review', views.addReview, name='add-review')
    
    # path('<slug:pk>/detail-check-login', views.detailCheckLogin, name='detail-check-login')
]
