# Generated by Django 3.1.2 on 2020-10-31 21:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0013_auto_20201031_2119'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patientinformation',
            old_name='language',
            new_name='sprache',
        ),
    ]
