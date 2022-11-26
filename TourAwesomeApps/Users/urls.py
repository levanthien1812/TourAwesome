from django.urls import path

from . import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views._login, name='login'),
    path('logout', views._logout, name='logout')
]
