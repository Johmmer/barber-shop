from django.contrib import admin
from .models import Service, Barber, Time, Reservation
# Register your models here.

admin.site.register(Service)

admin.site.register(Barber)

admin.site.register(Time)

admin.site.register(Reservation)