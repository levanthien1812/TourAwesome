# Generated by Django 4.1.3 on 2022-12-15 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tours', '0028_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.PositiveIntegerField(default=5),
        ),
    ]
