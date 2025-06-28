from django.contrib import admin
from .models import Service, Barber, Hora, Reservation
# Register your models here.

admin.site.register(Service)

admin.site.register(Barber)

admin.site.register(Hora)

admin.site.register(Reservation)