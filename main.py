import flet as ft
from flet_core import alignment
import json
import requests
from datetime import date

#link para o bd firebase
link = 'https://teste-dbd-default-rtdb.firebaseio.com/'

#Inicio da função main page que gera a interface
def main(page: ft.Page, route="/relatorio_1"):
    page.title = "Relatorio Fisioterapia"
    page.window_width = 400
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = "adaptive"

    #Função para fazer a listview dentro da tela professor
    lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
    count = 1
    for i in range(0, 60):
        lv.controls.append(ft.TextButton(f"Line {count}"))
        count += 1

    #TROCA DE TELAS
    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                #Tela inicial menu botões
                "/",
                [
                    menu_topo,
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Text("Ficha Neurológica", color="BLACK"),
                            adaptive=True,
                            bgcolor="WHITE",
                            on_click=lambda _: page.go("/relatorio_1"),
                            width=200,
                            style=ft.ButtonStyle(
                                padding=30,
                                shape=ft.RoundedRectangleBorder(radius=5),
                            ),
                        ),
                        ft.padding.only(top=50),
                        alignment=ft.alignment.center,

                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Text("Área do Professor", color="BLACK"),
                            adaptive=True,
                            bgcolor="WHITE",
                            width=200,
                            on_click=lambda _: page.go("/professor_login"),
                            style=ft.ButtonStyle(
                                padding=30,
                                shape=ft.RoundedRectangleBorder(radius=5),
                            ),
                        ),
                        ft.padding.only(top=50),
                        alignment=ft.alignment.center,
                    ),
                ],
            )
        )
        #Tela da ficha
        if page.route == "/relatorio_1":
            page.views.append(
                ft.View(
                    "/relatorio_1",
                    scroll=ft.ScrollMode.AUTO,
                    controls=[
                        menu_topo,
                        texto_relatorio,
                        numero_prontuario,
                        nome_paciente,

                        ft.Row([
                            ft.Column(
                                [ft.Container(idade_paciente, width=140)]),
                            ft.Column(
                                [ft.Container(sexo_paciente, width=214)])
                        ]),
                        telefone_paciente,
                        profissao_paciente,
                        endereco_paciente,
                        diagnostico_paciente,

                        ft.Container(texto_anamnese, padding=5, ),

                        HDA_anamnese,

                        ft.Container(texto_sinais_vitais, padding=5, ),

                        ft.Row([
                            ft.Column(
                                [ft.Container(pa, width=177, ), ft.Container(fc, width=177, )]),
                            ft.Column(
                                [ft.Container(fr, width=177, ), ft.Container(sp02, width=177, )])
                        ]),

                        qp,
                        ft.Container(texto_comorbidades, padding=5, ),

                        ft.Row([
                            ft.Column(
                                [ft.Container(has, ), ft.Container(dm, ), ]),
                            ft.Column(
                                [ft.Container(cardiopatia)])
                        ]),

                        outra_comorbidades,
                        af,
                        ft.Container(texto_inspecao, padding=5, ),

                        ft.Row([
                            ft.Column(
                                [ft.Container(hidratado), ft.Container(andador), ft.Container(cicatriz),
                                 ft.Container(locomocao_independente), ft.Container(nao_colaborativo),
                                 ft.Container(hematoma), ft.Container(rubor), ]),
                            ft.Column(
                                [ft.Container(muletas), ft.Container(cadeira_rodas), ft.Container(calor),
                                 ft.Container(colaborativo), ft.Container(corado), ft.Container(edema),
                                 ft.Container(escara)]
                            )
                        ]),

                        local_escara,

                        ft.Container(texto_palpacao, padding=5, ),

                        ft.Container(texto_trofismo, padding=5, ),

                        ft.Row([
                            ft.Column(
                                [ft.Container(atrofia), ft.Container(hipertrofia)]),
                            ft.Column(
                                [ft.Container(hipotrofia), ft.Container(normotrofia)])
                        ]),
                        local_trofismo,

                        ft.Container(texto_tonus, padding=5, ),

                        ft.Row([
                            ft.Column(
                                [ft.Container(atonia), ft.Container(hipotonia), ft.Container(normotonia), ]),
                            ft.Column(
                                [ft.Container(hipertonia), ft.Container(hipertonia_plastica),
                                 ft.Container(hipertonia_elastica), ])
                        ]),

                        ft.Container(intensidade_hipertonia),

                        ft.Container(texto_adm, padding=5, ),

                        ft.Container(adm_valor),
                        movimento_adm,

                        ft.Container(texto_reflexos, padding=5),

                        ft.Container(texto_reflexos_profundos),

                        ft.Container(texto_direito),
                        ft.Container(bicipital_direito),
                        ft.Container(tricipital_direito),
                        ft.Container(estilorradial_direito),
                        ft.Container(cubitopronador_direito),
                        ft.Container(patelar_direito),
                        ft.Container(aquileu_direito),
                        ft.Container(adutor_direito),

                        ft.Container(texto_esquerdo, ),
                        ft.Container(bicipital_esquerdo),
                        ft.Container(tricipital_esquerdo),
                        ft.Container(estilorradial_esquerdo),
                        ft.Container(cubitopronador_esquerdo),
                        ft.Container(patelar_esquerdo),
                        ft.Container(aquileu_esquerdo),
                        ft.Container(adutor_esquerdo),

                        ft.Container(texto_reflexos_superficiais, padding=5),
                        ft.Container(texto_direito),

                        ft.Row([
                            ft.Column(
                                [ft.Container(ft.Text("")), ft.Container(texto_plantar), ft.Container(texto_abdominal)]
                            ),
                            ft.Column(
                                [ft.Container(texto_presente), ft.Container(presente_radiobutton_direito_plantar),
                                 ft.Container(presente_checkbox_abdominal_direito)]
                            ),
                            ft.Column(
                                [ft.Container(texto_ausente), ft.Container(ausente_checkbox_direito_plantar),
                                 ft.Container(ausente_checkbox_abdominal_direito)]
                            )
                        ]),

                        ft.Container(texto_esquerdo),

                        ft.Row([
                            ft.Column(
                                [ft.Container(ft.Text("")), ft.Container(texto_plantar), ft.Container(texto_abdominal)]
                            ),
                            ft.Column(
                                [ft.Container(texto_presente), ft.Container(presente_radiobutton_esquerdo_plantar),
                                 ft.Container(presente_checkbox_abdominal_esquerdo)]
                            ),
                            ft.Column(
                                [ft.Container(texto_ausente), ft.Container(ausente_checkbox_esquerdo_plantar),
                                 ft.Container(ausente_checkbox_abdominal_esquerdo)]
                            )
                        ]),

                        ft.Container(texto_obs),

                        ft.Container(texto_motricidade, padding=5),

                        ft.Row([
                            ft.Column(
                                [ft.Container(balismo), ft.Container(miocionia)]),
                            ft.Column(
                                [ft.Container(distonia), ft.Container(solucos)]),
                            ft.Column(
                                [ft.Container(caimbras), ft.Container(tremores)]
                            )
                        ]),

                        ft.Row([
                            ft.Column(
                                [ft.Container(movimentos_coreicos), ft.Container(movimentos_atetoicos),
                                 ft.Container(fasciculacoes)]),
                            ft.Column(
                                [ft.Container(convulsoes), ft.Container(espasmos), ft.Container(tiques)]),
                        ]),

                        ft.Container(texto_atividades_funcionais),

                        ft.Container(ddp),
                        ft.Row([
                            ft.Column(
                                [ft.Container(quatro_apoios), ft.Container(quatro_ajoelhado),
                                 ft.Container(semi_ajoelhado), ft.Container(arrastar_cruzado)]
                            )
                        ]),

                        ft.Container(dle),
                        ft.Row([
                            ft.Column(
                                [ft.Container(sentado), ft.Container(ajoelhado), ft.Container(rolar),
                                 ft.Container(arrastar)]
                            )
                        ]),

                        ft.Container(texto_coordenacao),

                        ft.Row([
                            ft.Column(
                                [ft.Container(index_index)]),
                            ft.Column(
                                [ft.Container(index_nariz)]),
                        ]),
                        ft.Container(calcanhar_joelho, alignment=ft.alignment.center),

                        ft.Container(texto_equilibrio, padding=5),
                        ft.Container(texto_tronco, padding=5),
                        tronco,
                        ft.Container(texto_romberg, padding=5),
                        romberg,
                        ft.Container(texto_romberg_sensi, padding=5),
                        romberg_sensibilizado,
                        ft.Container(texto_avd, padding=5),
                        avd,
                        ft.Container(texto_testes_funcionais, padding=5),
                        testes_funcionas,
                        ft.Container(texto_avaliacao_marcha, padding=5),
                        avaliacao_marcha,
                        ft.Container(texto_observacoes, padding=5),
                        observacoes,
                        ft.Container(btn_enviar, alignment=ft.alignment.center),
                    ],
                )
            )
        page.update()
        #Tela do professor login
        if page.route == "/professor_login":
            page.views.append(
                ft.View(
                    "/professor_login",
                    scroll=ft.ScrollMode.AUTO,
                    controls=[
                        menu_topo,
                        ft.Container(
                        ft.Text("LOGIN PROFESSOR", size=25, weight=ft.FontWeight.BOLD,),
                        alignment=ft.alignment.center,
                        padding=30
                        ),
                        ft.Row([
                           ft.Column([
                               ft.Container(
                                  ft.Icon(name=ft.icons.PERSON, size=30),
                                   ft.padding.only(bottom=25)
                               ),
                               ft.Container(
                                  ft.Icon(name=ft.icons.KEY, size=30),
                                   ft.padding.only(top=0)
                               )
                           ]),
                           ft.Column([
                               ft.Container(
                                   usuario,
                               ),
                               ft.Container(
                                   senha
                               )
                           ])
                        ]),
                        ft.Container(
                            btn_login,
                            alignment=alignment.center,
                            padding=25
                        )

                    ],
                )
            )
        page.update()
        #tela professor normal
        if page.route == "/professor":
            page.views.append(
                ft.View(
                    "/professor",
                    scroll=ft.ScrollMode.AUTO,
                    controls=[
                        menu_topo,
                        ft.Text("Insira o nome do paciente que deseja procurar:"),
                        ft.Row([
                            ft.Column([
                                pesquisa_prof
                            ]),
                            ft.Column([
                                pesquisa_prof_button
                                #lv
                            ]),
                        ]),
                        ft.Container(
                            #c1,
                            lv,
                            border=ft.border.all(1),

                        ),
                    ],
                )
            )
        page.update()
    #DICIONARIO SALVO PARA ENVIAR OS DADOS AO BD
    dados = {
        'nome': 'nome_paciente.value',
        'idade': 'idade_paciente.value',
        'sexo': 'sexo_paciente.value',
        'cidade': 'endereco_paciente.value',
        'telefone': 'telefone_paciente.value',
        'email': 'email',
        'anamnese': {
            'HDA': 'hda_anamnese.value',
            'Sinais Vitais': {
                'PA': 'pa.value',
                'FC': 'fc.value',
                'FR': 'fr.value',
                'SPO2': 'sp02.value',
                'QP': 'qp.value'
            },
            'Comorbidade': {
                'HAS': 'has.value',
                'DM': 'dm.value',
                'Cardiopatia': 'cardiopatia.valeu',
                'Outra': 'outra_comorbidades.value'
            },
            'AF': 'af.value'
        },
        'Inspeção': {
            'locomoção Independente': 'locomocao_independente.value',
            'Muleta': 'muletas.value',
            'Andador': 'andador.value',
            'Cadeira de Rodas': 'cadeira_rodas.value',
            'Cicatriz': 'cicatriz.value',
            'Escara Local': 'escara.value',
            'Colaborativo': 'colaborativo.value',
            'Não Colaborativo': 'nao_colaborativo.value',
            'Hidratado': 'hidratado.value',
            'Corado': 'corado.value',
            'Hematoma': 'hematoma.value',
            'Edema': 'edema.value',
            'Calor': 'calor.value',
            'Rubor': 'rubor.value'
        },
        'Palpação': {
            'Trofismo': {
                'Tipo': 'atrofia.value || hipertrofia.value || normotrofia.value',
                'Local': 'local_trofismo.value'
            },  # FIM TROFISMO
            'Tônus': {
                'Tipo': 'atonia.value || hipotonia.value || normotonia.value || normotonia.value',
                'Normotonia': 'hipertonia_plastica.value || hipertonia_elastica.value'  # NORMOTONIA VAI NO TIPO, MAS EXISTE ESSES DOIS TIPOS
            },  # FIM TONUS
            'Intensidade da Hipertonia': 'intensidade_hipertonia.value'
        },  # FIM PALPAÇÃO
        'ADM': {
            'Assegurada?': 'Preservado || Limitado',
            'Movimento': 'movimento_adm.value'
        },  # FIM ADM
        'Reflexos': {
            'Reflexos Profundo': {
                'Direito': {
                    'Bicipatal': 'bicipital_direito.value',
                    'Triciptal': 'tricipital_direito.value',
                    'Cúbitopronador': 'cubitopronador_direito.value',
                    'Patelar': 'patelar_direito.value',
                    'Aquileu': 'aquileu_direito.value',
                    'Adutor': 'adutor_direito.value'
                },  # FIM REFLEXOS PROFUNDOS DIREITO
                'Esquerdo': {
                    'Bicipatal': 'bicipital_esquerdo.value',
                    'Triciptal': 'tricipital_esquerdo.value',
                    'Cúbitopronador': 'cubitopronador_esquerdo.value',
                    'Patelar': 'patelar_esquerdo.value',
                    'Aquileu': 'aquileu_esquerdo.value',
                    'Adutor': 'adutor_esquerdo.value'
                }  # FIM REFLEXOS PROFUNDOS ESQUERDO
            },  # FIM REFLEXOS PROFUNDOS
            'Reflexos Superficiasi': {
                'Direito': {
                    'Cutaneo Planar': 'Presente(presente_radiobutton_direito_plantar.value) || ausente_checkbox_direito_plantar.value',
                    'Cutaneo Abdominal': 'presente_checkbox_abdominal_direito.value || ausente_checkbox_abdominal_direito.value'
                },  # FIM REFLEXOS SUPERFICIAIS DIREITO
                'Esquerdo': {
                    'Cutaneo Planar': 'Presente(presente_radiobutton_esquerdo_plantar.value) || ausente_checkbox_esquerdo_plantar.value',
                    'Cutaneo Abdominal': 'presente_checkbox_abdominal_esquerdo.value || ausente_checkbox_abdominal_esquerdo.value'
                }  # FIM REFLEXOS SUPERFICIAIS ESQUERDO
            }  # FIM REFLEXOS SUPERFICIAIS
        },  # FIM REFLEXOS
        'Motricidade Involuntaria': {
            'Movimentos Coreicos': 'movimentos_coreicos.value',
            'Movimentos Aleatorios': 'movimentos_atetoicos.value',
            'Balismo': 'balismo.value',
            'Distonia': 'distonia.value',
            'Câimbras': 'caimbras.value',
            'Convulsoes': 'convulsoes.value',
            'Miocionia': 'miocionia.value',
            'Soluços': 'solucos.value',
            'Espasmos': 'espasmos.value',
            'Faciculações(Micimias)': 'fasciculacoes.value',
            'Tremores': 'tremores.value',
            'Tiques': 'tiques.value'
        },  # FIM MOTRICIDADE INVOLUNTARIA
        'Atividades Funcionais': {
            'D.D p/ D.L.E : D.D p/ D.L.D': 'ddp.value',
            'D.L.E p/ D.V : D.L.D p/ D.V': 'dle.value',
            '4 apoios': 'quatro_apoios.value',
            '4 apoios p/ ajoelhado': 'quatro_ajoelhado.value',
            'Semi ajoelhado /p de pe': 'semi_ajoelhado.value',
            'Arastar Cruzado': 'arrastar_cruzado.value',
            'Sentado': 'sentado.value',
            'Ajoelhado p/ semi ajoelhado': 'ajoelhado.value',
            'Rolar': 'rolar.value',
            'Arastar Homolateral': 'arrastar.value'
        },  # FIM ATIVIDADES FUNCIONAIS
        'Coordenação': {
            'index-index': 'index_index.value',
            'index-nariz': 'index_nariz.value',
            'calcanhar-joelho': 'calcanhar_joelho.value'
        },  # FIM COORDENAÇÃO
        'Equilibrio': {
            'Tronco': 'tronco.value',
            'Romberg': 'romber.value',
            'Romberg Sensibilizado': 'romberg_sensibilizado.value'
        },  # FIM EQUILIBRIO
        "AVD's": 'avd.value',
        'Testes Funcionais': {
            'TUG': 'testes_funcionas.value'
        },  # FIM TESTES FUNCIONAIS
        'Avalialção Marcha': 'avaliacao_marcha.value'
    }  # FIM FICHA

    # duas funções para a caixa de dialogo no final do código, quando o cliente aperta enviar relatorio
    def open_dlg(e):
        page.dialog = dlg
        dlg.open = True
        page.update()

    dlg = ft.AlertDialog(
        title=ft.Text("Relatório enviado com sucesso!"), on_dismiss=lambda e: print("Dialog dismissed!")
    )

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.scroll = ft.ScrollMode.ALWAYS
    page.go(page.route)

    # Topo do programa, onde fica escrito Laboratorio fisioterapia com um fundo verde
    menu_topo = ft.AppBar(
        title=ft.Text("Laboratório Fisioterapia", size=20, color="WHITE"),
        center_title=True,
        bgcolor=ft.colors.GREEN_ACCENT_700,
    )

    def teste():
        print(nome_paciente.value)
        print(has.value)

    #Função do login do prof, onde pode mudar a senha e login
    def login_prof():
        if usuario.value == "adm" and senha.value == "123":
            page.go("/professor")
        else:
            page.go("/")

    #variaveis para a tela de login do prof
    usuario = ft.TextField(label="Usuário", width=330)
    senha = ft.TextField(label="Senha", width=330, password=True)
    pesquisa_prof = ft.TextField(label="INSIRA AQUI")
    pesquisa_prof_button = ft.IconButton(icon=ft.icons.SEARCH,icon_color="blue400",icon_size=30,tooltip="Buscar")

    c1 = ft.Column(
        spacing=10,
        height=550,
        width=360,
        scroll=ft.ScrollMode.ALWAYS,
        controls=[
            ft.TextButton(text="teste")
        ]
    )
    #BOtão Enviar da tela da ficha ATENçÃO PARA A FUNçÂO DO ON_CLICK
    btn_enviar = ft.ElevatedButton(
        content=ft.Text("Enviar relatório", color="BLACK"),
        adaptive=True,
        bgcolor="WHITE",
        on_click=lambda _: teste(),
        style=ft.ButtonStyle(
            padding=30,
            shape=ft.RoundedRectangleBorder(radius=5),
        ),
    )
    #BOTÃO LOGIN DO PROF
    btn_login = ft.ElevatedButton(
        content=ft.Text("Entrar", color="BLACK"),
        adaptive=True,
        bgcolor="WHITE",
        width=100,
        height=50,
        on_click=lambda _: login_prof(),
        style=ft.ButtonStyle(
            padding=15,
            shape=ft.RoundedRectangleBorder(radius=5),
        ),
    )
    # Todas as variaveis com "texto_" no nome, são textos que indicam algo no app
    texto_relatorio = ft.Text(
        "Avaliação Neurofuncional",
        size=25,
        weight=ft.FontWeight.BOLD,
    )
    # Aqui para baixo são todas as info do cliente, termina antes de anmasseses la
    numero_prontuario = ft.TextField(
        label="Nº do Prontuário",
        disabled=True,
        value="123"
    )
    nome_paciente = ft.TextField(
        label="Nome do paciente",
        max_length=60,

    )
    idade_paciente = ft.TextField(
        label="Idade do Paciente",
        input_filter=ft.NumbersOnlyInputFilter()
    )
    sexo_paciente = ft.Dropdown(
        label="Sexo do Paciente",
        width=205,
        options=[
            ft.dropdown.Option("Masculino", "Masculino"),
            ft.dropdown.Option("Feminino", "Feminino")
        ]
    )
    telefone_paciente = ft.TextField(
        label="Telefone de Paciente",
        prefix_text="(91)",
        max_length=9,
        input_filter=ft.NumbersOnlyInputFilter()
    )
    profissao_paciente = ft.TextField(
        label="Profissao do paciente",
    )
    endereco_paciente = ft.TextField(
        label="Endereço do paciente"
    )
    diagnostico_paciente = ft.TextField(
        label="Diagnostico do paciente",
        multiline="true"
    )

    # Aqui começa a parte "I" de anamnese
    texto_anamnese = ft.Text(
        "I-Anamnese",
        size=25,
        weight=ft.FontWeight.BOLD,
    )
    HDA_anamnese = ft.TextField(
        label="HDA",
        multiline="true",
    )
    texto_sinais_vitais = ft.Text(
        "Sinais vitais:",
        size=20,
        weight=ft.FontWeight.BOLD,
    )
    pa = ft.TextField(
        label="PA"
    )
    fc = ft.TextField(
        label="FC"
    )
    fr = ft.TextField(
        label="FR"
    )
    sp02 = ft.TextField(
        label="Sp02"
    )
    qp = ft.TextField(
        label="QP",
        multiline="true",
    )
    texto_comorbidades = ft.Text(
        "Comorbidades:",
        size=20,
        weight=ft.FontWeight.BOLD,
    )
    has = ft.Checkbox(
        label="HAS", value=False
    )
    dm = ft.Checkbox(
        label="DM", value=False
    )
    cardiopatia = ft.Checkbox(
        label="Cardiopatia", value=False
    )
    outra_comorbidades = ft.TextField(
        label="Outra:"
    )
    af = ft.TextField(
        label="AF"
    )
    medicamentos_uso = ft.TextField(
        label="Medicamentos em uso:",
        multiline="true",
    )
    # Aqui começa "II" de Inspeção
    texto_inspecao = ft.Text(
        "II-Inspeção",
        size=25,
        weight=ft.FontWeight.BOLD,
    )
    locomocao_independente = ft.Checkbox(
        label="Locomoção independente", value=False
    )
    muletas = ft.Checkbox(
        label="Muletas", value=False
    )
    andador = ft.Checkbox(
        label="Andador", value=False
    )
    cadeira_rodas = ft.Checkbox(
        label="Cadeira de rodas", value=False
    )
    cicatriz = ft.Checkbox(
        label="Cicatriz", value=False
    )
    colaborativo = ft.Checkbox(
        label="Colaborativo", value=False
    )
    nao_colaborativo = ft.Checkbox(
        label="Não Colaborativo", value=False
    )
    hidratado = ft.Checkbox(
        label="Hidratado", value=False
    )
    corado = ft.Checkbox(
        label="Corado", value=False
    )
    hematoma = ft.Checkbox(
        label="Hematoma", value=False
    )
    edema = ft.Checkbox(
        label="Edema", value=False
    )
    calor = ft.Checkbox(
        label="Calor", value=False
    )
    rubor = ft.Checkbox(
        label="Rubor", value=False
    )
    escara = ft.Checkbox(
        label="Escara", value=False
    )
    local_escara = ft.TextField(
        label="Local escara:"
    )

    # Aqui começa "III" de palpação
    texto_palpacao = ft.Text(
        "III-Palpação",
        size=25,
        weight=ft.FontWeight.BOLD,
    )
    texto_trofismo = ft.Text(
        "Trofismo:",
        size=20,
        weight=ft.FontWeight.BOLD,
    )
    atrofia = ft.Checkbox(
        label="Atrofia", value=False
    )
    hipertrofia = ft.Checkbox(
        label="Hipertrofia", value=False
    )
    hipotrofia = ft.Checkbox(
        label="Hipotrofia", value=False
    )
    normotrofia = ft.Checkbox(
        label="Normotrofia", value=False
    )
    local_trofismo = ft.TextField(
        label="Local:"
    )
    texto_tonus = ft.Text(
        "Tônus:",
        size=20,
        weight=ft.FontWeight.BOLD,
    )
    atonia = ft.Checkbox(
        label="Atonia", value=False
    )
    hipotonia = ft.Checkbox(
        label="Hipotonia", value=False
    )
    normotonia = ft.Checkbox(
        label="Normotonia", value=False
    )
    hipertonia = ft.Checkbox(
        label="Hipertonia:", value=False
    )
    hipertonia_plastica = ft.Checkbox(
        label="Plástica", value=False
    )
    hipertonia_elastica = ft.Checkbox(
        label="Elástica", value=False
    )
    intensidade_hipertonia = ft.Dropdown(
        label="Instensidade da hipertonia",
        options=[
            ft.dropdown.Option("Pequena", "Pequena"),
            ft.dropdown.Option("Média", "Média"),
            ft.dropdown.Option("Grande", "Grande")
        ]
    )

    # Aqui começa o "IV" de ADM
    texto_adm = ft.Text(
        "IV-ADM",
        size=25,
        weight=ft.FontWeight.BOLD,
    )
    adm_valor = ft.RadioGroup(content=ft.Column([ft.Row([
        ft.Column([ft.Radio(value="Preservada", label="Preservada")]),
        ft.Column([ft.Radio(value="Ilimitada", label="Ilimitada")])
    ])
    ])
    )
    movimento_adm = ft.TextField(
        label="Movimento:"
    )

    # Aqui começa "V" de reflexos
    texto_reflexos = ft.Text(
        "V-Reflexos",
        size=25,
        weight=ft.FontWeight.BOLD,
    )

    # Aqui é o reflexos profundos
    texto_reflexos_profundos = ft.Text(
        "Reflexos Profundos",
        size=20,
        weight=ft.FontWeight.BOLD,
    )

    # Aqui é a parte do direito
    texto_direito = ft.Text(
        ">Direito",
        size=25,
        weight=ft.FontWeight.BOLD,
    )
    bicipital_direito = ft.Dropdown(
        label="Bicipital",
        options=[
            ft.dropdown.Option("Ausente", "Ausente"),
            ft.dropdown.Option("Hiper", "Hiper"),
            ft.dropdown.Option("Hipo", "Hipo"),
            ft.dropdown.Option("Normo", "Normo")
        ]
    )
    tricipital_direito = ft.Dropdown(
        label="Tricipital",
        options=[
            ft.dropdown.Option("Ausente", "Ausente"),
            ft.dropdown.Option("Hiper", "Hiper"),
            ft.dropdown.Option("Hipo", "Hipo"),
            ft.dropdown.Option("Normo", "Normo")
        ]
    )
    estilorradial_direito = ft.Dropdown(
        label="Estilorradial",
        options=[
            ft.dropdown.Option("Ausente", "Ausente"),
            ft.dropdown.Option("Hiper", "Hiper"),
            ft.dropdown.Option("Hipo", "Hipo"),
            ft.dropdown.Option("Normo", "Normo")
        ]
    )
    cubitopronador_direito = ft.Dropdown(
        label="Cúbitopronador",
        options=[
            ft.dropdown.Option("Ausente", "Ausente"),
            ft.dropdown.Option("Hiper", "Hiper"),
            ft.dropdown.Option("Hipo", "Hipo"),
            ft.dropdown.Option("Normo", "Normo")
        ]
    )
    patelar_direito = ft.Dropdown(
        label="Patelar",
        options=[
            ft.dropdown.Option("Ausente", "Ausente"),
            ft.dropdown.Option("Hiper", "Hiper"),
            ft.dropdown.Option("Hipo", "Hipo"),
            ft.dropdown.Option("Normo", "Normo")
        ]
    )
    aquileu_direito = ft.Dropdown(
        label="Aquileu",
        options=[
            ft.dropdown.Option("Ausente", "Ausente"),
            ft.dropdown.Option("Hiper", "Hiper"),
            ft.dropdown.Option("Hipo", "Hipo"),
            ft.dropdown.Option("Normo", "Normo")
        ]
    )
    adutor_direito = ft.Dropdown(
        label="Adutor",
        options=[
            ft.dropdown.Option("Ausente", "Ausente"),
            ft.dropdown.Option("Hiper", "Hiper"),
            ft.dropdown.Option("Hipo", "Hipo"),
            ft.dropdown.Option("Normo", "Normo")
        ]
    )

    # Aqui é a parte do esquerdo
    texto_esquerdo = ft.Text(
        ">Esquerdo",
        size=25,
        weight=ft.FontWeight.BOLD,
    )
    bicipital_esquerdo = ft.Dropdown(
        label="Bicipital",
        options=[
            ft.dropdown.Option("Ausente", "Ausente"),
            ft.dropdown.Option("Hiper", "Hiper"),
            ft.dropdown.Option("Hipo", "Hipo"),
            ft.dropdown.Option("Normo", "Normo")
        ]
    )
    tricipital_esquerdo = ft.Dropdown(
        label="Tricipital",
        options=[
            ft.dropdown.Option("Ausente", "Ausente"),
            ft.dropdown.Option("Hiper", "Hiper"),
            ft.dropdown.Option("Hipo", "Hipo"),
            ft.dropdown.Option("Normo", "Normo")
        ]
    )
    estilorradial_esquerdo = ft.Dropdown(
        label="Estilorradial",
        options=[
            ft.dropdown.Option("Ausente", "Ausente"),
            ft.dropdown.Option("Hiper", "Hiper"),
            ft.dropdown.Option("Hipo", "Hipo"),
            ft.dropdown.Option("Normo", "Normo")
        ]
    )
    cubitopronador_esquerdo = ft.Dropdown(
        label="Cúbitopronador",
        options=[
            ft.dropdown.Option("Ausente", "Ausente"),
            ft.dropdown.Option("Hiper", "Hiper"),
            ft.dropdown.Option("Hipo", "Hipo"),
            ft.dropdown.Option("Normo", "Normo")
        ]
    )
    patelar_esquerdo = ft.Dropdown(
        label="Patelar",
        options=[
            ft.dropdown.Option("Ausente", "Ausente"),
            ft.dropdown.Option("Hiper", "Hiper"),
            ft.dropdown.Option("Hipo", "Hipo"),
            ft.dropdown.Option("Normo", "Normo")
        ]
    )
    aquileu_esquerdo = ft.Dropdown(
        label="Aquileu",
        options=[
            ft.dropdown.Option("Ausente", "Ausente"),
            ft.dropdown.Option("Hiper", "Hiper"),
            ft.dropdown.Option("Hipo", "Hipo"),
            ft.dropdown.Option("Normo", "Normo")
        ]
    )
    adutor_esquerdo = ft.Dropdown(
        label="Adutor",
        options=[
            ft.dropdown.Option("Ausente", "Ausente"),
            ft.dropdown.Option("Hiper", "Hiper"),
            ft.dropdown.Option("Hipo", "Hipo"),
            ft.dropdown.Option("Normo", "Normo")
        ]
    )
    # Aqui é a parte dos reflexos superficiais
    texto_reflexos_superficiais = ft.Text(
        "Reflexos superficiais",
        size=20,
        weight=ft.FontWeight.BOLD,
    )
    texto_presente = ft.Text(
        "Presente",
        size=15,
        weight=ft.FontWeight.BOLD,
    )
    texto_ausente = ft.Text(
        "Ausente",
        size=15,
        weight=ft.FontWeight.BOLD,
    )
    texto_plantar = ft.Text(
        "Cutâneo plantar",
        size=15,
        weight=ft.FontWeight.BOLD,
    )
    presente_radiobutton_direito_plantar = ft.RadioGroup(content=ft.Column([ft.Row([
        ft.Column([ft.Radio(value="F", label="F")]),
        ft.Column([ft.Radio(value="E", label="E")])
    ])
    ])
    )
    ausente_checkbox_direito_plantar = ft.Checkbox(
        label="", value=False
    )
    texto_abdominal = ft.Text(
        "Cutâneo abdominal",
        size=15,
        weight=ft.FontWeight.BOLD,
    )
    presente_checkbox_abdominal_direito = ft.Checkbox(
        label="", value=False
    )
    ausente_checkbox_abdominal_direito = ft.Checkbox(
        label="", value=False
    )

    presente_radiobutton_esquerdo_plantar = ft.RadioGroup(content=ft.Column([ft.Row([
        ft.Column([ft.Radio(value="F", label="F")]),
        ft.Column([ft.Radio(value="E", label="E")])
    ])
    ])
    )
    ausente_checkbox_esquerdo_plantar = ft.Checkbox(
        label="", value=False
    )
    presente_checkbox_abdominal_esquerdo = ft.Checkbox(
        label="", value=False
    )
    ausente_checkbox_abdominal_esquerdo = ft.Checkbox(
        label="", value=False
    )
    texto_obs = ft.Text(
        "F: flexão E:extensão (Babinski +)",
        size=12,
        weight=ft.FontWeight.BOLD,
    )

    texto_motricidade = ft.Text(
        "VI-Motricidade Involuntária",
        size=25,
        weight=ft.FontWeight.BOLD,
    )
    movimentos_coreicos = ft.Checkbox(
        label="Movimentos coreicos", value=False
    )
    movimentos_atetoicos = ft.Checkbox(
        label="Movimentos atetoicos", value=False
    )
    balismo = ft.Checkbox(
        label="Balismo", value=False
    )
    distonia = ft.Checkbox(
        label="Distonia", value=False
    )
    caimbras = ft.Checkbox(
        label="Caimbras", value=False
    )
    convulsoes = ft.Checkbox(
        label="Convulsoes", value=False
    )
    miocionia = ft.Checkbox(
        label="Miocionia", value=False
    )
    solucos = ft.Checkbox(
        label="Soluços", value=False
    )
    espasmos = ft.Checkbox(
        label="Espasmos", value=False
    )
    fasciculacoes = ft.Checkbox(
        label="Fasciculações(micimias)", value=False
    )
    tremores = ft.Checkbox(
        label="Tremores", value=False
    )
    tiques = ft.Checkbox(
        label="Tiques", value=False
    )
    texto_atividades_funcionais = ft.Text(
        "VII-Atividades funcionais",
        size=25,
        weight=ft.FontWeight.BOLD,
    )
    ddp = ft.Checkbox(
        label="D.D p/ D.L.E.: D.D p/ D.L.D"
    )
    quatro_apoios = ft.Checkbox(
        label="4 apoios"
    )
    quatro_ajoelhado = ft.Checkbox(
        label="4 apoios p/ajoelhado"
    )
    semi_ajoelhado = ft.Checkbox(
        label="Semi ajoelhado p/ de pé"
    )
    arrastar_cruzado = ft.Checkbox(
        label="Arrastar cruzado"
    )
    dle = ft.Checkbox(
        label="D.L.E. p/ D.V.: D.L.D. p/ D.V"
    )
    sentado = ft.Checkbox(
        label="Sentado"
    )
    ajoelhado = ft.Checkbox(
        label="Ajoelhado p/semi ajoelhado"
    )
    rolar = ft.Checkbox(
        label="Rolar"
    )
    arrastar = ft.Checkbox(
        label="Arrastar homolateral"
    )
    texto_coordenacao = ft.Text(
        "VIII-Coordenação(presente ou ausente)",
        size=25,
        weight=ft.FontWeight.BOLD,
    )
    index_index = ft.Dropdown(
        label="Index-Index",
        width=175,
        options=[
            ft.dropdown.Option("+", "+"),
            ft.dropdown.Option("-", "-")
        ]
    )
    index_nariz = ft.Dropdown(
        label="Index-Nariz",
        width=175,
        options=[
            ft.dropdown.Option("+", "+"),
            ft.dropdown.Option("-", "-")
        ]
    )
    calcanhar_joelho = ft.Dropdown(
        label="Calcanhar-Joelho",
        width=175,
        options=[
            ft.dropdown.Option("+", "+"),
            ft.dropdown.Option("-", "-")
        ]
    )
    texto_equilibrio = ft.Text(
        "IX-Equilíbrio",
        size=25,
        weight=ft.FontWeight.BOLD,
    )
    texto_tronco = ft.Text(
        "Tronco:",
        size=20,
        weight=ft.FontWeight.BOLD,
    )
    tronco = ft.Dropdown(
        label="",
        options=[
            ft.dropdown.Option("Bom", "Bom"),
            ft.dropdown.Option("Regular", "Regular"),
            ft.dropdown.Option("Ruim", "Ruim")
        ]
    )
    texto_romberg = ft.Text(
        "Romberg:",
        size=20,
        weight=ft.FontWeight.BOLD,
    )
    romberg = ft.Dropdown(
        label="",
        options=[
            ft.dropdown.Option("Positivo", "Positivo"),
            ft.dropdown.Option("Negativo", "Negativo")
        ]
    )
    texto_romberg_sensi = ft.Text(
        "Romberg Sensibilizado:",
        size=20,
        weight=ft.FontWeight.BOLD,
    )
    romberg_sensibilizado = ft.Dropdown(
        label="",
        options=[
            ft.dropdown.Option("Positivo", "Positivo"),
            ft.dropdown.Option("Negativo", "Negativo")
        ]
    )
    texto_avd = ft.Text(
        "X-AVD's",
        size=25,
        weight=ft.FontWeight.BOLD,
    )
    avd = ft.Dropdown(
        label="",
        options=[
            ft.dropdown.Option("Dependente", "Dependente"),
            ft.dropdown.Option("Semidependente", "Semidependente"),
            ft.dropdown.Option("Independente", "Independente")
        ]
    )
    texto_testes_funcionais = ft.Text(
        "XI-Testes Funcionais",
        size=25,
        weight=ft.FontWeight.BOLD,
    )
    testes_funcionas = ft.Dropdown(
        options=[
            ft.dropdown.Option("< 10 segundos", "< 10 segundos"),
            ft.dropdown.Option("10 a 19 segundos", "10 a 19 segundos"),
            ft.dropdown.Option("20 a 29 segundos", "20 a 29 segundos"),
            ft.dropdown.Option(">= 30 segundos", ">= 30 segundos")
        ]
    )
    texto_avaliacao_marcha = ft.Text(
        "XII-Avaliação da Marcha",
        size=25,
        weight=ft.FontWeight.BOLD,
    )
    avaliacao_marcha = ft.Dropdown(
        label="",
        options=[
            ft.dropdown.Option("Normal", "Normal"),
            ft.dropdown.Option("Atáxica", "Atáxica"),
            ft.dropdown.Option("Escarvante", "Escarvante"),
            ft.dropdown.Option("Parkinsoniana", "Parkinsoniana"),
            ft.dropdown.Option("Anserina", "Anserina"),
            ft.dropdown.Option("Em tesoura", "Em tesoura")
        ]
    )
    texto_observacoes = ft.Text(
        "Observações:",
        size=25,
        weight=ft.FontWeight.BOLD,
    )
    observacoes = ft.TextField(
        label="Observações:",
        multiline="true",
        max_length=500
    )
#Fim do código =D
ft.app(target=main, view=ft.AppView.FLET_APP)