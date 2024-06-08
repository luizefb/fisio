import json
import requests
from datetime import date

#Link para se comunicar cm o banco de dados
link = 'https://teste-dbd-default-rtdb.firebaseio.com/'

#Dicionario Completo que será enviado para o banco
dados = {
    'nome':'nome do paciente aq',
    'idade':'idade do paciente aq',
    'sexo':'sexo do paciente aq',
    'cidade':'cidade do paciente aq',
    'telefone':'telefone do paciente aq',
    'email':'email do paciente aq',
    'anamnese': {
        'HDA': 'HDA AQ',
        'Sinais Vitais':{
            'PA':'PA AQ',
            'FC':'FC AQ',
            'FR':'FR AQ',
            'SPO2':'SPO2 AQ',
            'QP':'QP AQ'
                        },
    'Comorbidade':{
        'HAS':'HAS AQ',
        'DM':'DM AQ',
        'Cardiopatia':'Cardiopatia AQ',
        'Outra':'OUTRA AQ'
        },
    'AF':'AF AQ'
    },
    'Inspeção':{
        'locomoção Independente': False,
        'Muleta': False,
        'Andador': False,
        'Cadeira de Rodas': False,
        'Cicatriz': False,
        'Escara Local': False,
        'Colaborativo': False,
        'Não Colaborativo': False,
        'Hidratado': False,
        'Corado': False,
        'Hematoma': False,
        'Edema': False,
        'Calor': False,
        'Rubor': False
    },
    'Palpação':{
        'Trofismo':{
            'Tipo':'atrofia || hipertrofia || normotrofia',
            'Local':'Local do trofismo'
        },#FIM TROFISMO
        'Tônus':{
            'Tipo':'atonia || hipotonia || normotonia || normotonia',
            'Normotonia':'Plastica || Elastica' #NORMOTONIA VAI NO TIPO, MAS EXISTE ESSES DOIS TIPOS
        },#FIM TONUS
        'Intensidade da Hipertonia':'Pequena || Media || Grande'
        },#FIM PALPAÇÃO
        'ADM':{
            'Assegurada?':'Preservado || Limitado',
            'Movimento':'Movimento analisado'
        },#FIM ADM
        'Reflexos':{
            'Reflexos Profundo':{
                'Direito':{
                    'Bicipatal': 'Ausente || Hipo || Hiper || Normo',
                    'Triciptal': 'Ausente || Hipo || Hiper || Normo',
                    'Cúbitopronador': 'Ausente || Hipo || Hiper || Normo',
                    'Patelar': 'Ausente || Hipo || Hiper || Normo',
                    'Aquileu': 'Ausente || Hipo || Hiper || Normo',
                    'Adutor': 'Ausente || Hipo || Hiper || Normo'
                },#FIM REFLEXOS PROFUNDOS DIREITO
                'Esquerdo':{
                    'Bicipatal': 'Ausente || Hipo || Hiper || Normo',
                    'Triciptal': 'Ausente || Hipo || Hiper || Normo',
                    'Cúbitopronador': 'Ausente || Hipo || Hiper || Normo',
                    'Patelar': 'Ausente || Hipo || Hiper || Normo',
                    'Aquileu': 'Ausente || Hipo || Hiper || Normo',
                    'Adutor': 'Ausente || Hipo || Hiper || Normo'
                }#FIM REFLEXOS PROFUNDOS ESQUERDO
            },#FIM REFLEXOS PROFUNDOS
            'Reflexos Superficiasi':{
                'Direito':{
                    'Cutaneo Planar':'Presente(Flexao || Extensão) || Ausente',
                    'Cutaneo Abdominal':'Presente || Ausente'
                },#FIM REFLEXOS SUPERFICIAIS DIREITO
                'Esquerdo':{
                    'Cutaneo Planar':'Presente(Flexao || Extensão) || Ausente',
                    'Cutaneo Abdominal':'Presente || Ausente'
                }#FIM REFLEXOS SUPERFICIAIS ESQUERDO
            }#FIM REFLEXOS SUPERFICIAIS
        },#FIM REFLEXOS
        'Motricidade Involuntaria':{
            'Movimentos Coreicos':False,
            'Movimentos Aleatorios':False,
            'Balismo':False,
            'Distonia':False,
            'Câimbras':False,
            'Convulsoes':False,
            'Miocionia':False,
            'Soluços':False,
            'Espasmos':False,
            'Faciculações(Micimias)':False,
            'Tremores':False,
            'Tiques':False
        },#FIM MOTRICIDADE INVOLUNTARIA
        'Atividades Funcionais':{
            'D.D p/ D.L.E : D.D p/ D.L.D':False,
            'D.L.E p/ D.V : D.L.D p/ D.V':False,
            '4 apoios':False,
            '4 apoios p/ ajoelhado':False,
            'Semi ajoelhado /p de pe':False,
            'Arastar Cruzado':False,
            'Sentado':False,
            'Ajoelhado p/ semi ajoelhado':False,
            'Rolar':False,
            'Arastar Homolateral':False
        },#FIM ATIVIDADES FUNCIONAIS
        'Coordenação':{
            'index-index':False,
            'index-nariz':False,
            'calcanhar-joelho':False
        },#FIM COORDENAÇÃO
        'Equilibrio':{
            'Tronco': 'Bom || Regular || Ruim',
            'Romberg': False,
            'Romberg Sensibilizado': False
        },#FIM EQUILIBRIO
        "AVD's":'Dependente || Semidependente || Independente',
        'Testes Funcionais':{
            'TUG': '< 10sec || 10 a 19 sec || 20 a 29 sec || >= 30 sec'
        },#FIM TESTES FUNCIONAIS
        'Avalialção Marcha':'Normal || Ataxia || Escarvante || Parksoniana || Arserina || Em tesoura'
    }#FIM FICHA

def Insert(link):

    def macacasasaso(nome):
        print(nome)

