# Generated by Django 2.0.2 on 2018-03-16 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0006_profile_speciality'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='appointment_type',
            field=models.CharField(default='Offline', max_length=20),
        ),
    ]
