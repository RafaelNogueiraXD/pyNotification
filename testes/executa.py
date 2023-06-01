import subprocess

def executaBash():
    caminho_arquivo = "testes/bash/execC.sh"
    processo = subprocess.Popen(['bash', caminho_arquivo], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    saida, erro = processo.communicate()

    if processo.returncode == 0:
        return saida.decode()
    else:
        return erro.decode()

# def executar_arquivo_bash():
#     try:
#         subprocess.run(["./bash/execC.sh"], check=True)
#     except subprocess.CalledProcessError as e:
#         print(f"Ocorreu um erro ao executar o arquivo bash: {e}")

# executar_arquivo_bash()
