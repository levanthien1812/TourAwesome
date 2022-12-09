from django.db import models

def blog_image_path(instance, filename):
    return 'blogs/{0}/images/{1}'.format(instance.id, filename)

def blog_content_path(instance, filename):
    return 'blogs/{0}/{1}'.format(instance.id, filename)

class Blog(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to=blog_image_path, null=True)
    description = models.CharField(max_length=1500, null=True)
    content = models.FileField(upload_to=blog_content_path)
    relatedLocation = models.CharField(max_length=50, null=True)
    # likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
