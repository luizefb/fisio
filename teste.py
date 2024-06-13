import requests
import json

link = 'https://teste-dbd-default-rtdb.firebaseio.com/'

#COMEÇO PESQUISA -------------------------------------------
def pesquisa(link:str):
    #COLETA TODOS OS LINKS
    pesquisa = requests.get(f'{link}Prontuarios/.json')

    #TRANSFORMA EM DICIONARIO
    dic_pesquisa = pesquisa.json()

    #PEGA APENAS OS VALORES DAS CHAVES
    dic_pesquisa = dic_pesquisa.values()

    # AQ TU TEM Q COLOCAR O NOME DO PACIENTE
    select = "Salve"

    #PROCURA O NOME E PADRONIZA OQ N É A CHAVE DESEJADA
    encontrar_paciente = map(lambda dic: dic if dic['nome'] == select else '#', dic_pesquisa)

    #ELIMINA AS OUTRAS CHAVES
    paciente = tuple(filter(lambda dic: dic != '#', encontrar_paciente))

    #PEGA A CHAVE COM AS INFORMAÇÕES
    paciente_info = dict(paciente[0])

    #PRINT PRA VE C TA FUNCIONANDO
    print(paciente_info["nome"])

#FIM PESQUISA -------------------------------------------

#COMECO DELETE -------------------------------------------
def delete(link:str):
    pesquisa = requests.get(f'{link}Prontuarios/.json')

    #TRANSFORMA EM DICIONARIO
    dic_pesquisa = pesquisa.json()

    # AQ TU TEM Q COLOCAR O NOME DO PACIENTE QUE TU QUER APAGAR
    select = "Salve"

    #PPROCURA OQ TU QUER E APAGA AO ENCONTRAR O NOME DO PACIENTE. CASO N ENCONTRE ELE N FAZ NADA
    for id in dic_pesquisa:
        if dic_pesquisa[id]['marco'] == select:
            requisicao = requests.delete(f'{link}Prontuarios/{id}')
        else:
            pass

#FIM DELETE

#INICIO UPDATE
def update(link:str):
    pass
#FIM UPDATE

pesquisa(link=link)
delete(link=link)
update(link=link)
