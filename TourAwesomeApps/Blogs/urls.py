from django.urls import path
from . import views

urlpatterns = [
    path('', views.getBlogs, name='get-blogs'),
    path('create', views.createBlog, name='create-blog'),
    path('<int:pk>', views.getBlog, name='get-blog')
]
