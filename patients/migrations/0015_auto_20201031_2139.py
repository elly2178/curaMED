# Generated by Django 3.1.2 on 2020-10-31 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0014_auto_20201031_2138'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patientinformation',
            old_name='birthdate',
            new_name='geburtstag',
        ),
    ]