# Generated by Django 3.0.4 on 2020-04-11 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0017_auto_20200411_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='current',
            name='pid',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='current',
            name='sid',
            field=models.IntegerField(default=0),
        ),
    ]
