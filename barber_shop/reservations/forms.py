from django import forms
from .models import Reservation
from datetime import time

def generar_horas():
    horas = []
    for h in range(8, 21):
        hora = time(hour=h).strftime('%H:%M')
        hora_mostrar = time(hour=h).strftime('%I:%M %p')
        horas.append((hora, hora_mostrar))
    return horas

class ReservationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['time'].widget = forms.Select(
            choices=generar_horas(),
            attrs={'class': 'form-control'}
        )

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'email', 'date', 'time', 'service', 'barber', 'notes']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escriba su nombre'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Escriba su email'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'id': 'datepicker', 'placeholder': 'seleccione una fecha'}),
            'service': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Seleccione un servicio'}),
            'barber': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Seleccione un barbero'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escriba sus notas'}),
        }