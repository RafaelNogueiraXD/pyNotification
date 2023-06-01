from testes import parseLog, comandShell
from testes.parseLog import parse_arguments, configure_logging, email_identify
from testes.comandShell import pegar_arq_bash
from testes.executa import executaBash
from datetime import datetime
from gptIA import gtpAssistant

# Obtém a data e hora atual
data_hora_atual = datetime.now()

# Formata a data e hora no formato desejado
data_hora_formatada = data_hora_atual.strftime("%Y-%m-%d %H:%M:%S")
def hora_atual_numerica():
    agora = datetime.now()
    hora_numerica = agora.month * 2592000 + agora.day *86400 + agora.hour * 3600 + agora.minute * 60 + agora.second
    return hora_numerica
def withGpt(saidaGeral):
    print("Gerando dados com GPT . . .")
    saida = gtpAssistant("report", saidaGeral)
    title = gtpAssistant("title", saidaGeral)
    return {"title": title, "output": saida}

def manualInfo(saida):
    print("Digite o titulo da mensagem: ")
    title = input()
    return {"title": title, "output": saida}


def executaFuncoes():
    args = parse_arguments()
    configure_logging(args.verbose)
    # calculate_square(args)
    HorarioInicial = hora_atual_numerica()
    retornoBash = executaBash()
    HorarioFinal = hora_atual_numerica()
    tempoExec = HorarioFinal - HorarioInicial
    obs = "sem observações"
    saida = "O programa foi executado dia: " + data_hora_formatada + "\n" + retornoBash + "\n tempo de execução: " + str(tempoExec) + " segundos "
    saida = saida + "\n Observacao: " + obs
    if args.gpt == "GPT":
        dataHelper = withGpt(saida)
    else:
        dataHelper = manualInfo(saida) 
    
    dataMessage = {"email": email_identify(args),"title":  dataHelper["title"],"content": dataHelper["output"]}
    return dataMessage

    

if __name__ == "__main__":
    teste = executaFuncoes()
    print("envia para: " + teste["email"]) 
    print(teste["title"]) 
    print(teste["content"]) 