# Generated by Django 3.1.2 on 2020-11-08 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0003_auto_20201031_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='administrationinformation',
            name='telefon_number',
            field=models.CharField(default='23456789', max_length=10),
            preserve_default=False,
        ),
    ]
