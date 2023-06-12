import os.path
import base64
from email.message import EmailMessage
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from pseudoController import executaFuncoes
from gptIA import gtpAssistant 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import mimetypes
Email_padrao = 'leapylab@gmail.com'
Email_destino = 'testexe2904@gmail.com'
SCOPES = ['https://mail.google.com/']
creds = None
def envia_email():
    # verifica sem o determinado token existe
    if os.path.exists('token.json'): 
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        # se a credencial não existe ou não esta mais na data 
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
        message = MIMEMultipart()
        dataMessage = executaFuncoes()
        message['To'] =  dataMessage["email"]
        message['From'] = Email_padrao
        message['Subject'] = dataMessage["title"]
        # file_attachments = dataMessage["file"]
        file_attachments = [dataMessage["file"]]
        message.attach(MIMEText(dataMessage['content'], 'plain')) 
        # message.set_content(dataMessage["content"])
        for attachment in file_attachments:
            content_type, encoding = mimetypes.guess_type(attachment)
            main_type, sub_type = content_type.split('/', 1)
            file_name = os.path.basename(attachment)

            f = open(attachment, 'rb')

            myFile = MIMEBase(main_type, sub_type)
            myFile.set_payload(f.read())
            myFile.add_header('Content-Disposition', 'attachment', filename=file_name)
            encoders.encode_base64(myFile)

            f.close()

            message.attach(myFile)
        
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
