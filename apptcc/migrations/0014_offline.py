# Generated by Django 5.0.1 on 2024-04-25 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apptcc', '0013_remove_service_ip_service_dispositivo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=16)),
            ],
        ),
    ]
