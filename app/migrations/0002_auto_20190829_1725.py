# Generated by Django 2.2.3 on 2019-08-29 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact_tble',
            name='Emailaddress',
        ),
        migrations.RemoveField(
            model_name='contact_tble',
            name='Message',
        ),
    ]
