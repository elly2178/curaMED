# Generated by Django 3.1.2 on 2020-11-12 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0021_patientinformation_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientinformation',
            name='number',
            field=models.CharField(max_length=10),
        ),
    ]
