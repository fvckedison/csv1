# Generated by Django 3.1.5 on 2021-05-24 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csvfile', '0002_auto_20210525_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='ISO',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AlterField(
            model_name='profile',
            name='aperture',
            field=models.CharField(default='', max_length=2),
        ),
        migrations.AlterField(
            model_name='profile',
            name='camera',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='disease',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='exposure',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='exposureTime',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AlterField(
            model_name='profile',
            name='filter',
            field=models.CharField(default='', max_length=4),
        ),
        migrations.AlterField(
            model_name='profile',
            name='focalLength',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AlterField(
            model_name='profile',
            name='height',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='number',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photoName',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='plantsNumber',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='shootinLocation',
            field=models.CharField(default='', max_length=4),
        ),
        migrations.AlterField(
            model_name='profile',
            name='shootingArea',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='shootingDate',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='shootingFunction',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='shootingTime',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='width',
            field=models.CharField(default='', max_length=10),
        ),
    ]
