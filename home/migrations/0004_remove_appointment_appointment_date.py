# Generated by Django 4.0 on 2021-12-13 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_appointment_appointment_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='appointment_date',
        ),
    ]
