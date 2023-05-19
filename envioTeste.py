import os.path
import base64
from email.message import EmailMessage
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

Email_padrao = 'leapylab@gmail.com'
Email_destino = 'testexe2904@gmail.com'
SCOPES = ['https://mail.google.com/']
creds = None

def envia_email():
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
                
            with open('token.json', 'w') as token:
                token.write(creds.to_json())
    
    try:
        # Cria o serviço Gmail API
        service = build('gmail', 'v1', credentials=creds)
        
        # Cria uma mensagem de e-mail
        message = EmailMessage()
        message.set_content('Olá, este é um exemplo de envio de e-mail via API do Gmail.')
        
        message['To'] = Email_padrao
        message['From'] = Email_padrao
        message['Subject'] = 'Exemplo de envio de e-mail'
        
        # Codifica a mensagem em base64
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
        
        # Cria o objeto de envio de mensagem
        send_message = {
            'raw': encoded_message
        }
        
        # Envia a mensagem
        result = service.users().messages().send(userId='me', body=send_message).execute()
        print('E-mail enviado com sucesso!')
    
    except HttpError as error:
        print('Ocorreu um erro ao enviar o e-mail:')
        print(error)
    
if __name__ == '__main__':
    envia_email()
