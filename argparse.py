
import argparse

# Cria um objeto ArgumentParser
parser = argparse.ArgumentParser(description='Exemplo de uso do argparse')

# Define um argumento posicional
parser.add_argument('posicional', type=int, help='Argumento posicional')

# Define um argumento opcional
parser.add_argument('--opcional', type=str, help='Argumento opcional')

# Analisa os argumentos da linha de comando
args = parser.parse_args()

# Acessa os valores dos argumentos
print('Argumento posicional:', args.posicional)
print('Argumento opcional:', args.opcional)
