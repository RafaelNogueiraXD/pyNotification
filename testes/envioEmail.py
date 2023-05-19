import smtplib
#funciona só na minha residencia
from email.mime.text import MIMEText
import subprocess
import datetime

# Obtém a data e hora atual
data_hora_atual = datetime.datetime.now()

# Formata a data e hora no formato desejado
data_hora_formatada = data_hora_atual.strftime("%Y-%m-%d %H:%M:%S")

caminho_arquivo = './bash.sh'

processo = subprocess.Popen(['bash', caminho_arquivo], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
saida, erro = processo.communicate()
concatena = "\t " + data_hora_formatada + "\n" + saida.decode()
if processo.returncode == 0:
    # print('Arquivo bash executado com sucesso!')
    print('\tSaída:\n', concatena)
else:
    print('Erro ao executar o arquivo bash:')
    print('Saída:', saida.decode())
    print('Erro:', erro.decode())
    
    
    
username = 'testexe2904@gmail.com'
password = 'gjewssljkazolath'

smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = username
smtp_password = password
mensagem = MIMEText(concatena)
mensagem["Subject"] = "Comando ls"

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
