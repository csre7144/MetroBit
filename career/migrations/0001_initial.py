# Generated by Django 5.0.4 on 2024-06-12 06:34

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='career',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('position', models.CharField(choices=[('10:00 am', '10:00 am'), ('10:30 am', '10:30 am'), ('11:00 am', '11:00 am'), ('11:45 am', '11:45 am'), ('12:30 pm', '12:30 pm'), ('1:30 pm', '1:30 pm'), ('2:30 pm', '2:30 pm'), ('3:00 pm', '3:00 pm')], max_length=50)),
            ],
        ),
    ]
