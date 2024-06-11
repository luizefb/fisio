import requests
import json

link = 'https://teste-dbd-default-rtdb.firebaseio.com/'
anamnese = {
                'HDA': '20',
                'Sinais Vitais': {
                    'PA': '20',
                    'FC': '20',
                    'FR': '20',
                    'SPO2': '20',
                    'QP': '20'
                },
                'Comorbidade': {
                    'HAS': '20',
                    'DM': '20',
                    'Cardiopatia': '20',
                    'Outra': '20'
                },
                'AF': '20'
            }
inspecao = {
                'locomoção Independente': True,
                'Muleta': False,
                'Andador': True,
                'Cadeira de Rodas': False,
                'Cicatriz': True,
                'Escara': False,
                'Escara Local': True,
                'Colaborativo': False,
                'Não Colaborativo': True,
                'Hidratado': False,
                'Corado': True,
                'Hematoma': False,
                'Edema': True,
                'Calor': False,
                'Rubor': True
}
palpacao = {
                'Intensidade da Hipertonia': '40',
                'Trofismo': {
                    'Atrofia': False,
                    'Hipotrofia': True,
                    'Hipertrofia': False,
                    'Normotrofia': True,
                    'Local': False
                },  # FIM TROFISMO
                'Tônus': {
                    'Atonia':True,
                    'Hipotonia': False,
                    'Normotonia': True,
                    'Hipertonia': False,
                    'Hipertonia plastica': True,
                    'Hipertonia elastica': False
                }  # FIM TONUS
            }  # FIM PALPAÇÃO
adm = {
                'Preservada': False,
                'Ilimitada': True,
                'Movimento': 'Rodar o Giroscopio'
            }  # FIM ADM
reflexosProfundos= {
                    'Direito': {
                        'Bicipatal': 'hipo',
                        'Triciptal': 'hipo',
                        'Estilorradial': 'hipo',
                        'Cúbitopronador': 'hipo',
                        'Patelar': 'hipo',
                        'Aquileu': 'hipo',
                        'Adutor': 'hipo'
                    },  # FIM REFLEXOS PROFUNDOS DIREITO
                    'Esquerdo': {
                        'Bicipatal': 'hipo',
                        'Triciptal': 'hipo',
                        'Estilorradial': 'hipo',
                        'Cúbitopronador': 'hipo',
                        'Patelar': 'hipo',
                        'Aquileu': 'hipo',
                        'Adutor': 'hipo'
                    }  # FIM REFLEXOS PROFUNDOS ESQUERDO
                }  # FIM REFLEXOS PROFUNDOS
reflexosSuperficiais = {
                    'Direito': {
                        'Cutaneo Plantar Presente': True,
                        'Cutaneo Plantar Ausente': False,
                        'Cutaneo Abdominal Presente': False,
                        'Cutaneo abdominal Ausente': True
                    },
                    'Esquerdo': {
                        'Cutaneo Plantar Presente': 'hipo',
                        'Cutaneo Plantar Ausente': 'hipo',
                        'Cutaneo Abdominal Presente': 'hipo',
                        'Cutaneo Abdominal Ausente': 'hipo'
                    }
} # FIM REFLEXOS SUPERFICIAIS
reflexos = {
    'reflexos Profundos':reflexosProfundos,
    'reflexos Superficiais':reflexosSuperficiais
}
motricidadeInvoluntaria = {
                'Movimentos Coreicos': False,
                'Movimentos Aleatorios': True,
                'Balismo': True,
                'Distonia': False,
                'Câimbras': False,
                'Convulsoes': True,
                'Miocionia': False,
                'Soluços': True,
                'Espasmos': False,
                'Faciculações(Micimias)': False,
                'Tremores': True,
                'Tiques': False
            }# FIM MOTRICIDADE INVOLUNTARIA

atividadesFuncionais = {
                'DD p DLE : DD p DLD': False,
                'DLE p DV : DLD p DV': True,
                '4 apoios': True,
                '4 apoios p ajoelhado': True,
                'Semi ajoelhado p de pe': False,
                'Arastar Cruzado': False,
                'Sentado': True,
                'Ajoelhado p semi ajoelhado': False,
                'Rolar': False,
                'Arastar Homolateral': True
}

coordenacao = {
                'index-index': '+',
                'index-nariz': '-',
                'calcanhar joelho': '+'

}  # FIM COORDENAÇÃO
equilibrio = {
                'Tronco': 'bom',
                'Romberg': True,
                'Romberg Sensibilizado': True
}  # FIM EQUILIBRIO
testesFuncionais = {
                'TUG': f'< 10sec'
} # FIM TESTES FUNCIONAIS

dados = {
    'nome':'Marco',
    'idade':'20',
    'sexo':'masculino',
    'cidade':'Braganaca',
    'telefone':'91985901979',
    'anamnese':anamnese,
    'inspecao':inspecao,
    'palpacao':palpacao,
    'adm':adm,
    'reflexos':reflexos,
    'motricidade Involuntaria':motricidadeInvoluntaria,
    'atividades Funcionais':atividadesFuncionais,
    'coordenacao':coordenacao,
    'equilibrio':equilibrio,
    'AVDs': 'dependente',
    'testes Funcionais':testesFuncionais,
    'Avalialcao Marcha': 'Normal',
    'Observacoes': 'É um macaco msm pqp'
}

requisicao = requests.post(f'{link}Prontuarios/.json', data=json.dumps(dados))
print(requisicao)

pesquisa = requests.get(f'{link}Prontuarios/.json')

dic_pesquisa = pesquisa.json()
for id in dic_pesquisa:
    print(dic_pesquisa[id]["nome"])