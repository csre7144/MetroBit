# Generated by Django 5.0.4 on 2024-06-14 10:05

import phonenumber_field.modelfields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0020_alter_career_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='career',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=13, region=None),
        ),
    ]
