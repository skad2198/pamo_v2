# Generated by Django 3.0.7 on 2020-06-09 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20200609_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='name',
            field=models.CharField(default='abc', max_length=100),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='vehicle_type',
            field=models.CharField(choices=[('scv', 'SCV'), ('pickup', 'Pick-Up'), ('truck', 'Truck'), ('bus', 'Bus'), ('car', 'Car'), ('tractor', 'Agriculture Tractor'), ('others', 'Others')], default='others', max_length=30),
        ),
    ]
