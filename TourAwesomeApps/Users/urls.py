from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views._login, name='login'),
    path('logout', views._logout, name='logout'),
    path('account', views.update, name='update-account'),
    path('bookings', views.showBookings, name='show-bookings'),
    path('manage-users', views.manageUser, name='manage-users'),
    path('manage-tours', views.manageTour, name='manage-tours'),
    path('manage-bookings', views.manageBookings, name='manage-bookings'),
    path('<int:pk>/delete', views.deleteUser, name='delete-user'),
    path('bookings/<int:pk>/accept', views.acceptBooking, name='accept-booking'),
    
    # FOR RESET PASSWORD WHEN FORGET
    # path('reset_password', auth_views.PasswordResetView.as_view(), name='reset_password'),
    # path('reset_password_sent', auth_views.PasswordResetView.as_view(), name='password_reset_done'),
    # path('password/<uidb64>/<token>', auth_views.PasswordResetView.as_view(), name='password_reset_confirm'),
    # path('reset_password_complete', auth_views.PasswordResetView.as_view(), name='password_reset_complete')
]
