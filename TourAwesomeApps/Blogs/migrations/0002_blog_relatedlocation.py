# Generated by Django 4.1.3 on 2022-12-07 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='relatedLocation',
            field=models.CharField(max_length=50, null=True),
        ),
    ]