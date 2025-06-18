from django.db import models

class Service(models.Model):
    service_name = models.CharField(max_length=255, null=False, blank=False)
    
    def __str__(self):
        return self.service_name

class Barber(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self):
        return self.name

class Reservation(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    date = models.DateField(null=False, blank=False)
    time = models.TimeField(null=False, blank=False)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE)
    notes = models.TextField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.name