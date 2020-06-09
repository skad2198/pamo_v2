from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth.models import User
# Create your models here.


class vehicle(models.Model):

    image = models.FileField(null=True)
    name = models.CharField(max_length=100, default="abc")
    brand = models.CharField(max_length=20, choices=(('tata', 'TATA'), ('mahindra',
                                                                        'Mahindra'), ('daewoo', 'Daewoo')))
    vehicle_type = models.CharField(max_length=30, choices=(
        ('scv', "SCV"), ('pickup', "Pick-Up"), ('truck', "Truck"), ('bus', "Bus"), ('car', "Car"), ('tractor', "Agriculture Tractor"), ('others', "Others")), default="others")
    description = models.TextField(max_length=2000, default="")
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.brand
