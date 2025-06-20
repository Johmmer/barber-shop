from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
from .forms import ReservationForm
from .models import Reservation
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow
import datetime
import logging

logger = logging.getLogger(__name__)


def get_reservation():
    reservations = Reservation.objects.all()
    return reservations
reservations = get_reservation()

def google_calendar_init(request):
    flow = Flow.from_client_secrets_file(
        settings.GOOGLE_CLIENT_SECRETS_FILE,
        scopes=settings.GOOGLE_API_SCOPES,
        redirect_uri=settings.REDIRECT_URI
    )
    authorization_url, state = flow.authorization_url(access_type='offline', include_granted_scopes='true')
    request.session['state'] = state
    return redirect(authorization_url)

def google_calendar_redirect(request):
    state = request.session.get('state')  # Usa get() para evitar KeyError
    if not state:
        return HttpResponse("Error: No se encontró el estado en la sesión.", status=400)

    flow = Flow.from_client_secrets_file(
        settings.GOOGLE_CLIENT_SECRETS_FILE,
        scopes=settings.GOOGLE_API_SCOPES,
        state=state,
        redirect_uri=settings.REDIRECT_URI
    )
    authorization_response = request.build_absolute_uri()
    flow.fetch_token(authorization_response=authorization_response)
    credentials = flow.credentials
    request.session['credentials'] = credentials_to_dict(credentials)
    return render(request, 'reservations/authorization.html')

def credentials_to_dict(credentials):
    return {
        'token': credentials.token,
        'refresh_token': credentials.refresh_token,
        'token_uri': credentials.token_uri,
        'client_id': credentials.client_id,
        'client_secret': credentials.client_secret,
        'scopes': credentials.scopes
    }

def create_calendar_events(request):
        # Log de debugging completo
    logger.info("=== DEBUG CREATE CALENDAR EVENTS ===")
    logger.info(f"Request path: {request.path}")
    logger.info(f"Request full URL: {request.build_absolute_uri()}")
    logger.info(f"Session keys: {list(request.session.keys())}")
    
    # Mostrar todo el contenido de la sesión
    for key, value in request.session.items():
        logger.info(f"Session[{key}]: {value}")
    
    # Verificar específicamente las credenciales
    if 'credentials' in request.session:
        logger.info("✓ Credentials found in session")
        logger.info(f"Credentials type: {type(request.session['credentials'])}")
        logger.info(f"Credentials content: {request.session['credentials']}")
    else:
        logger.info("✗ NO credentials in session")
        logger.info("Available session keys:", list(request.session.keys()))
    
    reservations = get_reservation()
    creds = Credentials(**request.session['credentials'])
    service = build('calendar', 'v3', credentials=creds)
    
    for reservation in reservations:
        date_value = reservation.date
        time_value = reservation.time
        combined_datetime = datetime.datetime.combine(date_value, time_value)
        duration = datetime.timedelta(hours=1)
        end_time = combined_datetime + duration
        
        event = {
            
            'summary': reservation.name,
            'start': {
                'dateTime': combined_datetime.isoformat(),
                'timeZone': 'America/Santo_Domingo',
            },
            'end': {
                'dateTime': end_time.isoformat(),
                'timeZone': 'America/Santo_Domingo',
            },
        }
        
        try:
            event_result = service.events().insert(calendarId='primary', body=event).execute()
            print(f'Event created: {event_result["htmlLink"]}')
        except Exception as e:
            print(f'Error creating event: {e}')
    return HttpResponse('success')

def index(request):
    return HttpResponse('index')

def reserve(request):  
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            # Process the form data
            # (e.g., save to a database, send email, etc.)
            reserve_time = form.cleaned_data['time']
            if not Reservation.objects.filter(time=reserve_time).exists():
                form.save()
                return redirect('create_event')
    else:
        form = ReservationForm()
    return render(request, 'reservations/form.html', {'form': form})
