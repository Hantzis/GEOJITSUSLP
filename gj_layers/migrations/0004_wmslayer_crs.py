# Generated by Django 3.0.3 on 2020-02-18 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gj_layers', '0003_auto_20200218_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='wmslayer',
            name='crs',
            field=models.ForeignKey(default='EPSG:4326', on_delete=django.db.models.deletion.PROTECT, to='gj_layers.WMSCRS'),
            preserve_default=False,
        ),
    ]
