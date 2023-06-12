import subprocess
import models.acharArquivo
#entender pq nao está executando
def executaBash():
    # caminho_arquivo = "models/bash/execC.sh"
    caminho_arquivo = models.acharArquivo.encontrar_arquivo("execC.sh","/home/rafael/Área de Trabalho/trabalhos/pyNotification/models/bash/")
    if caminho_arquivo:
        print("caminho encontrado")
    else:
        print("ops... nao encontramos...")

    processo = subprocess.Popen(['bash', caminho_arquivo], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    saida, erro = processo.communicate()

    if processo.returncode == 0:
        return saida.decode()
    else:
        return erro.decode()
