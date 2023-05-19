from testes import parseLog, comandShell
from testes.parseLog import parse_arguments, configure_logging, calculate_square
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
    calculate_square(args)
    HorarioInicial = hora_atual_numerica()
    retornoBash = pegar_arq_bash()
    HorarioFinal = hora_atual_numerica()
    tempoExec = HorarioInicial - HorarioFinal
    saida = "O programa foi executado dia: " + data_hora_formatada + "\n" + retornoBash + "\n tempo de execução: " + str(tempoExec)
    return saida
    

if __name__ == "__main__":
    print(executaFuncoes()) 