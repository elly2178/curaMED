# Generated by Django 3.1.2 on 2020-10-31 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrationinformation',
            name='city',
            field=models.TextField(max_length=40),
        ),
        migrations.AlterField(
            model_name='administrationinformation',
            name='street',
            field=models.TextField(max_length=80),
        ),
    ]
