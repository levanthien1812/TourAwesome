# Generated by Django 4.1.3 on 2022-11-28 17:02

import TourAwesomeApps.Blogs.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.FileField(null=True, upload_to=TourAwesomeApps.Blogs.models.blog_image_path),
        ),
    ]
