# Generated by Django 3.0.3 on 2020-02-18 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gj_layers', '0005_auto_20200218_1916'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wmslayer',
            name='src',
        ),
    ]
