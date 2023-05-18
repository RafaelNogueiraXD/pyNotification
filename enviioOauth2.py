# pip install google-auth google-auth-oauthlib smtplib
# pip install --upgrade google-api-python-client
# pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2

import smtplib
from email.mime.text import MIMEText
from google.oauth2 import service_account
import base64
import google.oauth2.credentials
import google_auth_oauthlib.flow
import logging

TIME_FORMAT = '%Y-%m-%d,%H:%M:%S'
CLIENT_SECRET_FILE = 'credentials2.json'
API_NAME  = 'gmail'

logging.basicConfig(format='%(asctime)s %(levelname)s {%(module)s} [%(funcName)s] %(message)s',
							datefmt=TIME_FORMAT, level=logging.DEBUG)

credentials = google_auth_oauthlib.flow.Flow.from_client_secrets_file('credentials2.json', scopes=['https://www.googleapis.com/auth/gmail.send'])
mensagem = MIMEText('Conteúdo do email em HTML')
mensagem['Subject'] = 'Teste de envio usando Oauth'
mensagem['From'] = 'leapylab@gmail.com'
mensagem['To'] = 'testexe2904@gmail.com'
logging.debug("teste")
with smtplib.SMTP('smtp.gmail.com', 587) as servidor_smtp:
    print("antes ")
    servidor_smtp.starttls()
    print("depois ")
    servidor_smtp.login(credentials, credentials.token)
    servidor_smtp.sendmail(mensagem['From'], mensagem['To'], mensagem.as_string())

