from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser
import datetime


def user_image_path(instance, filename):
    return 'users/user_{0}_{1}'.format(instance.id, filename)


sex_choices = [
    ('MALE', 'Nam'),
    ('FEMALE', 'Nữ')
]


class MyUser(AbstractUser):
    phoneNum = models.CharField(max_length=11, default=0)
    image = models.ImageField(
        upload_to=user_image_path, default='users/user-profile.png')
    name = models.CharField(max_length=30, null=True)
    email = models.EmailField(unique=True)
    birthday = models.DateField(default=now, null=True)
    sex = models.CharField(max_length=6, choices=sex_choices, null=True)


class Booking(models.Model):
    userID = models.ForeignKey('Users.MyUser', on_delete=models.CASCADE)
    tourID = models.ForeignKey(
        'Tours.Tour', on_delete=models.CASCADE)
    startDate = models.DateField(null=True, blank=True)
    bookingDate = models.DateField(auto_now_add=True)
    quantity = models.PositiveIntegerField()
    price = models.BigIntegerField(null=True, default=0)

    def __str__(self):
        return self.userID + self.tourID


payment_choices = [
    ('ATOFFICE', 'Thanh toán tại văn phòng'),
    ('BYTRANSFER', 'Chuyển khoản qua ngân hàng')
]


class BookingDetail(models.Model):
    bookingID = models.ForeignKey('Users.Booking', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phoneNum = models.CharField(max_length=11)
    address = models.CharField(max_length=150)
    payment = models.CharField(
        max_length=10, choices=payment_choices, default=payment_choices[0])
    
