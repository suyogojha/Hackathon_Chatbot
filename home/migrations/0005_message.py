# Generated by Django 4.0 on 2021-12-13 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_appointment_appointment_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('message', models.CharField(blank=True, max_length=255, null=True)),
                ('contact', models.PositiveIntegerField()),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]