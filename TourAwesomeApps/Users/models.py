from django.db import models
from django.contrib.auth.models import AbstractUser


def user_image_path(instance, filename):
    return 'user/user_{0}_{1}'.format(instance.id, filename)


roles_choices = [
    ('ADMIN', 'Admin'),
    ('GUIDE', 'Hướng dẫn viên'),
    ('COUNSELOR', 'Tư vấn viên'),
    ('USER', 'Người dùng')
]

class MyUser(AbstractUser):
    phoneNum = models.CharField(max_length=11, default=0)
    image = models.ImageField(upload_to=user_image_path)
    username = models.EmailField(unique=True)
    role = models.CharField(
        max_length=10,
        choices=roles_choices,
        default=roles_choices[2]
    )