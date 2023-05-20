import requests
import json

def gtpAssistant(condition,tematica):
    API_KEY = "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"
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    link = "https://api.openai.com/v1/chat/completions"
    id_modelo = "gpt-3.5-turbo-0301"
    if condition == "title":
        conteudo = "diga um titulo de no máximo 30 letras, sobre " + tematica 
    else:    
        conteudo = "digite um relatório sobre " + tematica + "\n O nome de que faz esse relatório é o 'Laboratorio Lea'"
    body_mensagem ={"model": "gpt-3.5-turbo","messages": [{"role": "user", "content": conteudo}]}
    body_mensagem = json.dumps(body_mensagem)


    requisicao = requests.post(link, headers=headers, data=body_mensagem)
    # print(requisicao)
    # print(requisicao.text)
    resposta = requisicao.json()
    mensagem = resposta["choices"][0]["message"]["content"]
    return mensagem
   


if __name__ == "__main__":
    print(gtpAssistant("title","gmail"))