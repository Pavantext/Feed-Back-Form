# Generated by Django 5.1.2 on 2024-11-30 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='quality',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedback',
            name='rating',
            field=models.TextField(blank=True, null=True),
        ),
    ]
