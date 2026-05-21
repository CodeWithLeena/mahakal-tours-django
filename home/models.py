from django.db import models


class Vehicle(models.Model):
    name = models.CharField(max_length=100)
    price_per_km = models.DecimalField(max_digits=6, decimal_places=2)
    capacity = models.IntegerField(default=4)
    vehicle_type = models.CharField(max_length=50, default='Sedan')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - ₹{self.price_per_km}/km"


class ContactQuery(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.phone}"
