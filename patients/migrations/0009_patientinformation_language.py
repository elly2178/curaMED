# Generated by Django 3.1.2 on 2020-10-30 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0008_auto_20201027_2107'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientinformation',
            name='language',
            field=models.CharField(default='german', max_length=10),
            preserve_default=False,
        ),
    ]
