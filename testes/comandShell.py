import subprocess
def pegar_arq_bash():
    caminho_arquivo = 'testes/bash.sh'

    processo = subprocess.Popen(['bash', caminho_arquivo], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    saida, erro = processo.communicate()

    if processo.returncode == 0:
        return saida.decode()
    else:
        return erro.decode()