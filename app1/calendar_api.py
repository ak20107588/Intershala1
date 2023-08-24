# calendar_api.py
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import os
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/calendar']

def get_google_calendar_service():
    creds = None
    token_file = 'path/to/your/token.json' 

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json",SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)
    return service

def create_calendar_event(summary, date, start_time, end_time):
    service = get_google_calendar_service()

    # Define event details
    event = {
        'summary': summary,
        'start': {
            'dateTime': start_time,
            'timeZone': 'Your_Time_Zone',  # e.g., 'America/New_York'
        },
        'end': {
            'dateTime': end_time,
            'timeZone': 'Your_Time_Zone',
        },
    }

    # Create the event
    event = service.events().insert(calendarId='primary', body=event).execute()
    return event['id']
