# Generated by Django 5.0.1 on 2024-03-04 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apptcc', '0002_dispositivo'),
    ]

    operations = [
        migrations.AddField(
            model_name='scanner',
            name='ativo',
            field=models.CharField(default=1, max_length=3),
            preserve_default=False,
        ),
    ]
