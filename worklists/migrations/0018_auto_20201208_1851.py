# Generated by Django 3.1.2 on 2020-12-08 17:51

from django.db import migrations, models
import worklists.models


class Migration(migrations.Migration):

    dependencies = [
        ('worklists', '0017_auto_20201208_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worklistinformation',
            name='scheduled_procedure_step_start_date',
            field=models.CharField(max_length=100, validators=[worklists.models.validate_date]),
        ),
    ]