# Generated by Django 3.0.2 on 2020-01-27 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='child',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='license',
            field=models.CharField(default='NA', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pnum',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='profile',
            name='vehicle_type',
            field=models.CharField(default='NA', max_length=100),
        ),
    ]
