# Generated by Django 3.0.4 on 2020-04-11 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0016_auto_20200411_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='image',
            field=models.ImageField(default='', upload_to='media/property_manage/images'),
        ),
    ]
