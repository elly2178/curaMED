# Generated by Django 3.1.2 on 2020-10-27 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0007_patientinformation_birthdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientinformation',
            name='birthdate',
            field=models.DateField(),
        ),
    ]
