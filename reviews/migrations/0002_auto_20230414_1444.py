# Generated by Django 3.2.18 on 2023-04-14 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='genre',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.IntegerField(default=100),
        ),
    ]
