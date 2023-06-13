import subprocess
import models.acharArquivo
#entender pq nao está executando
def executaBash(path):
    # caminho_arquivo = "models/bash/execC.sh"
    caminho_arquivo = models.acharArquivo.encontrar_arquivo(path)
    if caminho_arquivo:
        print("caminho encontrado")
    else:
        print("ops... nao encontramos...")

    print("executando arquivo bash...")
    processo = subprocess.Popen(['bash', caminho_arquivo], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    saida, erro = processo.communicate()

    if processo.returncode == 0:
        return saida.decode()
    else:
        return erro.decode()
