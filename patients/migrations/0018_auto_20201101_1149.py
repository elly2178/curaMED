# Generated by Django 3.1.2 on 2020-11-01 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0017_auto_20201101_1128'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patientinformation',
            old_name='first_name',
            new_name='adresse',
        ),
        migrations.RenameField(
            model_name='patientinformation',
            old_name='geburtstag',
            new_name='geburtsdatum',
        ),
        migrations.RenameField(
            model_name='patientinformation',
            old_name='second_name',
            new_name='name',
        ),
        migrations.AddField(
            model_name='patientinformation',
            name='plz',
            field=models.CharField(default=2551, max_length=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patientinformation',
            name='vorname',
            field=models.CharField(default='brom', max_length=50),
            preserve_default=False,
        ),
    ]
