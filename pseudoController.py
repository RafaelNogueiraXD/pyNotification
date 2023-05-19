from testes import parseLog, comandShell
from testes.parseLog import parse_arguments, configure_logging
from testes.comandShell import pegar_arq_bash
from datetime import datetime


# Obtém a data e hora atual
data_hora_atual = datetime.now()

# Formata a data e hora no formato desejado
data_hora_formatada = data_hora_atual.strftime("%Y-%m-%d %H:%M:%S")
def hora_atual_numerica():
    agora = datetime.now()
    hora_numerica = agora.month * 2592000 + agora.day *86400 + agora.hour * 3600 + agora.minute * 60 + agora.second
    return hora_numerica

def executaFuncoes():
    args = parse_arguments()
    configure_logging(args.verbose)
    # calculate_square(args)
    HorarioInicial = hora_atual_numerica()
    retornoBash = pegar_arq_bash()
    HorarioFinal = hora_atual_numerica()
    tempoExec = HorarioFinal - HorarioInicial
    print("\nAdicione uma observacao ao email: ")
    obs = input()
    saida = "O programa foi executado dia: " + data_hora_formatada + "\n" + retornoBash + "\n tempo de execução: " + str(tempoExec) + " segundos "
    saida = saida + "\n Observacao: " + obs
    return saida

def addTitle():
    print("Digite o Titulo de Email: ")
    titulo = input()
    return titulo
    

if __name__ == "__main__":
    print(executaFuncoes()) 