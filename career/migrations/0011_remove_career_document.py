# Generated by Django 5.0.4 on 2024-06-13 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0010_alter_career_document'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='career',
            name='document',
        ),
    ]
