from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
import os
from datetime import datetime, timedelta

# Credentials file (use a dummy path)
CLIENT_SECRETS_FILE = 'path_to_dummy/client_details.json'
API_NAME = 'calendar'
API_VERSION = 'v3'

# Initialize the Google Calendar API
def initialize_calendar():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json')

    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, ['https://www.googleapis.com/auth/calendar'])
        creds = flow.run_local_server(port=8080)

    service = build(API_NAME, API_VERSION, credentials=creds)
    return service

# Create a study event in the calendar
def create_study_event(service, calendar_id, summary, description, start_date):
    event = {
        'summary': summary,
        'description': description,
        'start': {
            'dateTime': start_date.strftime('%Y-%m-%dT%H:%M:%S'),
            'timeZone': 'Asia/Kolkata',
        },
        'end': {
            'dateTime': (start_date + timedelta(hours=3)).strftime('%Y-%m-%dT%H:%M:%S'),
            'timeZone': 'Asia/Kolkata',
        },
    }
    event = service.events().insert(calendarId=calendar_id, body=event).execute()
    return event

# Define your study plan (use dummy data)
def get_study_plan():
    study_plan = {
        "Day 1": {
            "Morning": "Study and understand Dummy Topic 1.",
            "Afternoon": "Practice problems related to Dummy Topic 1.",
            "Evening": "Learn about Dummy Topic 2."
        },
        "Day 2": {
            "Morning": "Study Dummy Topic 3 and solve numerical problems.",
            "Afternoon": "Study Dummy Topic 4 and solve numerical problems.",
            "Evening": "Study Dummy Topic 5 and solve numerical problems."
        },
        # Add other days and tasks here
    }
    return study_plan

def main():
    service = initialize_calendar()
    calendar_id = 'primary'
    study_plan = get_study_plan()
    
    start_date = datetime.now() + timedelta(days=1)

    for day, tasks in study_plan.items():
        for time, description in tasks.items():
            summary = f'Study - {day} - {time}'
            create_study_event(service, calendar_id, summary, description, start_date)
            start_date += timedelta(hours=3)

if __name__ == "__main__":
    main()
