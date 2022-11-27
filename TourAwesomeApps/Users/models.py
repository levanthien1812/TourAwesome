from django.db import models
from django.contrib.auth.models import AbstractUser

def user_image_path(instance, filename):
    return 'users/user_{0}_{1}'.format(instance.id, filename)

class MyUser(AbstractUser):
    phoneNum = models.CharField(max_length=11, default=0)
    image = models.ImageField(upload_to=user_image_path, default='users/user-profile.png')
    username = models.EmailField(unique=True)