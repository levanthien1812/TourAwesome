# Generated by Django 4.1.3 on 2022-11-29 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogs', '0002_blog_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='description',
            field=models.CharField(max_length=1500, null=True),
        ),
    ]
