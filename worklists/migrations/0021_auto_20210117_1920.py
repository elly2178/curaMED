# Generated by Django 3.1.5 on 2021-01-17 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worklists', '0020_auto_20210117_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worklistinformation',
            name='scheduled_performing_physician_s_name',
            field=models.CharField(choices=[('dr1', 'Dr. Stephan Weingartner'), ('dr2', 'Dr. Matias Schuetz'), ('dr3', 'Dr. Marvin Spengler')], max_length=80),
        ),
    ]
