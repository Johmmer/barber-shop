from django.db import models
from django.core.exceptions import ValidationError

def validate_price(value):
    if value < 0:
        raise ValidationError('El precio no puede ser negativo')

class Service(models.Model):
    service_name = models.CharField(max_length=255, null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[validate_price], default=300.00)
    
    def __str__(self):
        return self.service_name

class Barber(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self):
        return self.name

class Time(models.Model):
    start_time = models.TimeField(null=False, blank=False)
    text = models.CharField(max_length=100, null=False, blank=False)
    def __str__(self):
        return self.text

class Reservation(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    date = models.DateField(null=False, blank=False)
    time = models.ForeignKey(Time, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE)
    notes = models.TextField(null=True, blank=True)

    
    def __str__(self):
        return self.name