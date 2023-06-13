# /home/rafael/Área de Trabalho/trabalhos/Avaliacao/arquivo.zip
import os

def separar_caminho_arquivo(path):
    caminho = os.path.dirname(path)
    arquivo = os.path.basename(path)
    return arquivo, caminho

def encontrar_arquivo(path):
    nome_arquivo, diretorio_inicial = separar_caminho_arquivo(path)
    for raiz, diretorios, arquivos in os.walk(diretorio_inicial):
        if nome_arquivo in arquivos:
            caminho_arquivo = os.path.join(raiz, nome_arquivo)
            return caminho_arquivo

    return None


if __name__ == "__main__":
    # nome_arquivo = "arquivo.zip"
    diretorio_inicial = "/home/rafael/Área de Trabalho/trabalhos/pyNotification/models/bash/execC.sh"

    caminho_encontrado = encontrar_arquivo(diretorio_inicial)
    if caminho_encontrado:
        print("Arquivo encontrado:", caminho_encontrado)
    else:
        print("Arquivo não encontrado.")