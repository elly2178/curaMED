# Generated by Django 3.1.2 on 2020-10-26 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0002_auto_20201026_1843'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientinformation',
            name='gender',
        ),
    ]
