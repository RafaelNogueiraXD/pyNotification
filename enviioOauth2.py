
from future import print_function
import os.path
import base64
import requests
from email.message import EmailMessage
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import google.auth

SCOPES = ['https://mail.google.com/']
flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
credentials = flow.run_local_server(port=0)

service = build('gmail', 'v1', credentials=credentials)
message = {
    'raw': base64.urlsafe_b64encode(raw_message_bytes).decode('utf-8')
}
service.users().messages().send(userId='me', body=message).execute()
