# Generated by Django 4.1.1 on 2022-09-15 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app_1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='mileage',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='car',
            name='model_year',
            field=models.IntegerField(),
        ),
    ]
