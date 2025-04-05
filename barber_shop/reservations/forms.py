from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'email', 'date', 'time', 'service', 'barber', 'notes']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escriba su nombre'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Escriba su email'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'id': 'datepicker', 'placeholder': 'seleccione una fecha'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'id': 'timepicker', 'placeholder': 'seleccione una hora'}),
            'service': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Seleccione un servicio'}),
            'barber': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Seleccione un barbero'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escriba sus notas'}),
        }