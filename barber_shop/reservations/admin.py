from django.contrib import admin
from .models import Service, Barber, Reservation
# Register your models here.

admin.site.register(Service)

admin.site.register(Barber)

admin.site.register(Reservation)