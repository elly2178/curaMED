# Generated by Django 3.1.2 on 2020-11-01 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0016_auto_20201101_1127'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patientinformation',
            old_name='language',
            new_name='sprache',
        ),
    ]
