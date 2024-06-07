import json
import requests
from datetime import date
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4


link = 'https://teste-dbd-default-rtdb.firebaseio.com/'

loop = 0

while loop !=5:

    print('Oq Você deseja fazer?\n')

    loop = int(input('1- add\n2- verificar dados\n3-Deletar \n4-Atualizar \n5- sair\n'))

    if loop == 1:
        #Info do paciente
        nomePaciente = str(input('Digite o nome do paciente: '))
        idadePaciente = str(input('Digite o idade do paciente: '))
        telefone = str(input('Digite o telefone do paciente: '))
        dataNascimento = str(input('Digite a data de nascimento(DD-MM-AAAA): '))
        profisaao = str(input('Digite o profisaao do paciente: '))
        diagnosticoPossivel = str(input('Digite o possivel diagnostico do paciente: '))
        endereco = str(input('Digite o endereco do paciente: '))

        #Palpação
        trofismo = bool(input('Possui Trofismo: '))
        tonus = bool(input('Possui Tonus: '))
        intensidade = str(input('Digite o intensidade da hipertonia: '))

        palpacao = {
            'trofismo': trofismo,
            'tonus': tonus,
            'intensidade da hipertonia': intensidade
        }
        pdf = canvas.Canvas(f'{nomePaciente}.pdf', pagesize=A4)

        dados = {
            'nome': nomePaciente,
            'idade': idadePaciente,
            'dataAtendimento': str(date.today()),
            'telefone': telefone,
            'dataNascimento': dataNascimento,
            'profisaao': profisaao,
            'diagnostico': diagnosticoPossivel,
            'endereco': endereco,
            'palpaçaõ': palpacao
        }
        espacamento = 20
        for info in dados.keys():
            #print(f'{info} = {dados[info]}')
            pdf.drawString(100,650 - espacamento,f'{info} = {dados[info]}')
            espacamento+= 25

        pdf.save()

        requisicao = requests.post(f'{link}/Prontuarios/.json',data=json.dumps(dados))

        #Pra saber c deu certo
        print(requisicao)
        print('Cadastrado com sucesso')

    elif loop == 2:
        requisicao = requests.get(f'{link}/Prontuarios/.json')

        select = str(input('De qual paciente você gostaria de saber '))

        dic_requisicao = requisicao.json()

        dic_info = dic_requisicao.values()

        try:
            if select:
                encontrar_paciente = map(lambda dic: dic if dic['nome'] == select else '', dic_info)
                paciente = tuple(filter(lambda dic: dic != '', encontrar_paciente))
                paciente_info = dict(paciente[0])
                print(paciente_info)

                select = str(input('Deseja saber oq do paciente: '))
                print(paciente_info[f'{select}'])

            else:
                print(dic_info)
        except Exception as e:
            print('Algo deu errado ', e)

    elif loop == 3:
        requisicao = requests.get(f'{link}/Prontuarios/.json')
        dic_requisicao = requisicao.json()

        select = str(input('Digite o nome do paciente'))

        for id in dic_requisicao:
            if dic_requisicao[id]['nome'] == select:
                print(dic_requisicao[id])
                escolher = str(input(f'Deseja mesmo apagar os dados de {select}(Y/N): '))

                if escolher == 'Y':
                    requisicao = requests.delete(f'{link}/Prontuarios/{id}/.json')
                    print(requisicao)
                    print('Deletado com Sucesso')

                if escolher == 'N':
                    print('N alteramos nada do seu paciente')
                else:
                    print('Escolha uma opção valida')

    elif loop == 4:
        requisicao = requests.get(f'{link}/Prontuarios/.json')
        select = str(input('Digite o nome do paciente'))

        dic_requisicao = requisicao.json()
        for id in dic_requisicao:
            if dic_requisicao[id]['nome'] == select:
                print(dic_requisicao[id])
                update_chave = input('Digite oq voce quer atualizar do paciente: ')
                update_valor = input('Digite o novo valor')

                dados = {f'{update_chave}':f'{update_valor}'}

                print(dados)
                print(id)
                requisicao = requests.patch(f'{link}/Prontuarios/{id}/.json', data=json.dumps(dados))

                print(requisicao)
                print(requisicao.text, requisicao.content)

    elif loop == 5:
        print('Obgd por contar cm nossos serviços...')

    else:
        print('Digite algo valido')