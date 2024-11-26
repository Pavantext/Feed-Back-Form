# Generated by Django 5.1.3 on 2024-11-26 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=15)),
                ('ticket_support', models.CharField(max_length=20)),
                ('it_support', models.CharField(max_length=20)),
                ('security', models.CharField(max_length=20)),
                ('housekeeping', models.CharField(max_length=20)),
                ('facilitators', models.CharField(max_length=20)),
                ('archakas', models.CharField(max_length=20)),
                ('devotion', models.CharField(max_length=20)),
                ('harathi', models.CharField(max_length=20)),
                ('fountain', models.CharField(max_length=20)),
                ('prasadam', models.CharField(max_length=20)),
                ('visit', models.CharField(max_length=20)),
                ('improvement_areas', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
