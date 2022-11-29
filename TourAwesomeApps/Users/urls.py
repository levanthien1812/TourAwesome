from django.urls import path

from . import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views._login, name='login'),
    path('logout', views._logout, name='logout'),
    path('account', views.showAccount, name='show-account'),
    path('bookings', views.showBookings, name='show-bookings'),
]
