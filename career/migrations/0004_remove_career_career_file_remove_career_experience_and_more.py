# Generated by Django 5.0.4 on 2024-06-12 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0003_career_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='career',
            name='career_file',
        ),
        migrations.RemoveField(
            model_name='career',
            name='experience',
        ),
        migrations.RemoveField(
            model_name='career',
            name='join',
        ),
        migrations.RemoveField(
            model_name='career',
            name='position',
        ),
    ]
