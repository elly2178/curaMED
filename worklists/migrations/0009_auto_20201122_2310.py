# Generated by Django 3.1.2 on 2020-11-22 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worklists', '0008_auto_20201122_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worklistinformation',
            name='patient_s_birth_date',
            field=models.CharField(max_length=100),
        ),
    ]