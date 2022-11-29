from datetime import datetime
from django.db import models
# from multiselectfield import Multiselectfield

def tour_image_path(instance, filename):
    return 'tours/{0}/images/{1}'.format(instance.tour.id, filename)


def tour_timeline_path(instance, filename):
    return 'tours/{0}/{1}'.format(instance.id, filename)


class Tour (models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=30)
    price = models.FloatField()
    startDate = models.DateField()
    description = models.CharField(max_length=1000)
    highlight = models.CharField(max_length=1000)
    timeline = models.FileField(upload_to=tour_timeline_path, null=True)
    isDomestic = models.BooleanField(default=True)
    duration_days = models.PositiveIntegerField()
    duration_nights = models.PositiveIntegerField()
    pub_date = models.DateTimeField(default = datetime.now())
    isHot = models.BooleanField(default=True)

    @property
    def duration(self):
        return '%s ngày %s đêm' % (self.duration_days, self.duration_nights)

    def __str__(self):
        return self.name


class TourImage (models.Model):
    tour = models.ForeignKey('Tour', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=tour_image_path)
    
class TourVehicle (models.Model):
    vehicles_choices = [
        ('TRAIN', 'Tàu hỏa'),
        ('PLANE', 'Máy bay'),
        ('COACH', 'Xe khách'),
        ('SHIP', 'Thuyền')
    ]
    
    tour = models.ForeignKey('Tour', on_delete=models.CASCADE)
    vehicle = models.CharField(
        max_length=6,
        choices=vehicles_choices,
    )
