import subprocess

def executaBash():
    caminho_arquivo = "models/bash/execC.sh"
    processo = subprocess.Popen(['bash', caminho_arquivo], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    saida, erro = processo.communicate()

    if processo.returncode == 0:
        return saida.decode()
    else:
        return erro.decode()
