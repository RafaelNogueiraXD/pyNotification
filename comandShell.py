import subprocess

caminho_arquivo = './bash.sh'

processo = subprocess.Popen(['bash', caminho_arquivo], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
saida, erro = processo.communicate()

if processo.returncode == 0:
    # print('Arquivo bash executado com sucesso!')
    print('\tSaída:\n', saida.decode())
else:
    print('Erro ao executar o arquivo bash:')
    print('Saída:', saida.decode())
    print('Erro:', erro.decode())
