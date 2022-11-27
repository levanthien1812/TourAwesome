from django.db import models

def blog_content_path(instance, filename):
    return 'blogs/{0}_{1}'.format(instance, filename)

class Blog(models.Model):
    title = models.CharField(max_length=300)
    content = models.FileField(upload_to=blog_content_path)
    # likes = models.PositiveIntegerField(default=0)
