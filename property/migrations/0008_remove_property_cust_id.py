# Generated by Django 3.0.4 on 2020-04-09 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_auto_20200402_2126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='cust_id',
        ),
    ]
