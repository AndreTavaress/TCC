# Generated by Django 5.0.4 on 2024-05-06 23:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apptcc', '0014_scanner_off'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scanner',
            name='off',
        ),
    ]
