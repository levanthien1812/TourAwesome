from django.db import models

def blog_image_path(instance, filename):
    return 'blogs/{0}/images/{1}'.format(instance, filename)

def blog_content_path(instance, filename):
    return 'blogs/{0}/{1}'.format(instance, filename)

class Blog(models.Model):
    title = models.CharField(max_length=300)
    image = models.FileField(upload_to=blog_image_path, null=True)
    description = models.CharField(max_length=1500, null=True)
    content = models.FileField(upload_to=blog_content_path)
    # likes = models.PositiveIntegerField(default=0)
