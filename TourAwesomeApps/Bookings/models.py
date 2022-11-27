from django.db import models

class Booking(models.Model):
    userID = models.ForeignKey('Users.MyUser', on_delete=models.CASCADE)
    tourID = models.ForeignKey(
        'Tours.Tour', on_delete=models.CASCADE)
    startDate = models.DateField()
    bookingDate = models.DateField(auto_now_add=True)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.userID + self.tourID
