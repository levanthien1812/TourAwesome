from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser
import datetime

def user_image_path(instance, filename):
    return 'users/user_{0}_{1}'.format(instance.id, filename)

class MyUser(AbstractUser):
    phoneNum = models.CharField(max_length=11, default=0)
    image = models.ImageField(upload_to=user_image_path, default='users/user-profile.png')
    name = models.CharField(max_length=30,null=True)
    email = models.EmailField(unique=True)
    birthday = models.DateField(default=now, null=True)
    isMale = models.BooleanField(default=True)
    

class Booking(models.Model):
    userID = models.ForeignKey('Users.MyUser', on_delete=models.CASCADE)
    tourID = models.ForeignKey(
        'Tours.Tour', on_delete=models.CASCADE)
    startDate = models.DateField()
    bookingDate = models.DateField(auto_now_add=True)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.userID + self.tourID
