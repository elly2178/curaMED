# Generated by Django 3.1.2 on 2020-11-21 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modalities', '0006_auto_20201121_1649'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modalitiesinformation',
            name='associate_location',
        ),
    ]
