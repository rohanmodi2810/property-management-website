# Generated by Django 3.0.4 on 2020-03-31 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_auto_20200330_1726'),
    ]

    operations = [
        migrations.CreateModel(
            name='log_in_buyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='log_in_seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=25)),
            ],
        ),
    ]
