# Generated by Django 3.1.2 on 2020-10-31 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0009_patientinformation_language'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patientinformation',
            old_name='language',
            new_name='languagge',
        ),
    ]
