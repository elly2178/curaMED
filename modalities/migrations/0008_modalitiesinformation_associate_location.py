# Generated by Django 3.1.2 on 2020-11-21 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modalities', '0007_remove_modalitiesinformation_associate_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='modalitiesinformation',
            name='associate_location',
            field=models.CharField(default='random', max_length=500),
            preserve_default=False,
        ),
    ]