# Generated by Django 3.1.2 on 2020-11-18 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worklists', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='worklistinformation',
            name='scheduled_station_ae_title',
            field=models.CharField(default='bn', max_length=16),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='worklistinformation',
            name='patient_s_name',
            field=models.CharField(max_length=64),
        ),
    ]
