# Generated by Django 3.1.2 on 2020-11-08 16:25

from django.db import migrations, models
import django.db.models.deletion
import modalities.models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0005_auto_20201108_1533'),
        ('modalities', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modalitiesinformation',
            name='status',
        ),
        migrations.AddField(
            model_name='modalitiesinformation',
            name='ae_title',
            field=models.CharField(default='some', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='modalitiesinformation',
            name='associate_location',
            field=models.ForeignKey(default='14', on_delete=django.db.models.deletion.CASCADE, to='administration.administrationinformation'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='modalitiesinformation',
            name='ip',
            field=models.GenericIPAddressField(default='172.58.25.85'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='modalitiesinformation',
            name='port',
            field=models.PositiveIntegerField(default='5', validators=[modalities.models.validate_port]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='modalitiesinformation',
            name='title',
            field=models.CharField(max_length=150),
        ),
    ]
