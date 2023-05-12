import smtplib
from email.mime.text import MIMEText
username = 'testexe2904@gmail.com'
password = 'gjewssljkazolath'

smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = username
smtp_password = password
mensagem = MIMEText('ola, new email')
mensagem["Subject"] = "Agora é o rei que ta louco"

mensagem['From'] = username
mensagem["to"] = 'testexe2904@gmail.com'

with smtplib.SMTP(smtp_server, smtp_port) as servidor_smtp:
        servidor_smtp.starttls()
        servidor_smtp.login(smtp_username,smtp_password)
        servidor_smtp.sendmail(mensagem["From"], mensagem["To"], mensagem.as_string())


#será usado futuramente 
def ler_arquivo_html(arquivo):
    with open(arquivo, 'r') as f:
        conteudo = f.read()
    return conteudo
