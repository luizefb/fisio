import flet as ft

def main(page: ft.Page, route="/relatorio_1"):
    page.title = "Relatorio Fisioterapia"
    page.window_width = 400
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = "adaptive"

    # TESTE TROCA DE TELAS!!!!!!!!!
    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    menu_topo,
                    ft.ElevatedButton("Ficha avaliação neurológica", on_click=lambda _: page.go("/relatorio_1")),
                ],
            )
        )
        #AQUI É A PARTE ONDE EU ADICIONO NA TELA A FICHA
        if page.route == "/relatorio_1":
            page.views.append(
                ft.View(

                    "/relatorio_1",
                    [

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
                        medicamentos_uso,
                        queda_12meses,

                        ft.Row([
                            ft.Column(
                                [ft.Container(queda_sim_nao)]),
                            ft.Column(
                                [ft.Container(quantas_quedas, width=200)])
                        ]),

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

                        ft.Row([
                            ft.Column(
                                [ft.Container(preservada)]),
                            ft.Column(
                                [ft.Container(ilimitada)])
                        ]),
                        movimento_adm,

                        ft.Container(texto_reflexos, padding=5),

                        ft.Container(texto_reflexos_profundos),

                        ft.Container(texto_direito),
                        ft.Container(texto_direito_bicipital),
                        ft.Container(bicipital_direito),
                        ft.Container(texto_direito_tricciptal),
                        ft.Container(tricipital_direito),
                        ft.Container(texto_direito_estilorradial),
                        ft.Container(estilorradial_direito),
                        ft.Container(texto_direito_cubitopronador),
                        ft.Container(cubitopronador_direito),
                        ft.Container(texto_direito_patelar),
                        ft.Container(patelar_direito),
                        ft.Container(texto_direito_aquileu),
                        ft.Container(aquileu_direito),
                        ft.Container(texto_direito_adutor),
                        ft.Container(adutor_direito),

                        ft.Container(texto_esquerdo, ),
                        ft.Container(texto_esquerdo_bicipital),
                        ft.Container(bicipital_esquerdo),
                        ft.Container(texto_esquerdo_tricciptal),
                        ft.Container(tricipital_esquerdo),
                        ft.Container(texto_esquerdo_estilorradial),
                        ft.Container(estilorradial_esquerdo),
                        ft.Container(texto_esquerdo_cubitopronador),
                        ft.Container(cubitopronador_esquerdo),
                        ft.Container(texto_esquerdo_patelar),
                        ft.Container(patelar_esquerdo),
                        ft.Container(texto_esquerdo_aquileu),
                        ft.Container(aquileu_esquerdo),
                        ft.Container(texto_esquerdo_adutor),
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

    # Botão de enviar o relatorio e salvar
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
        input_filter=ft.TextOnlyInputFilter(),

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
        input_filter=ft.TextOnlyInputFilter()
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
    queda_12meses = ft.Text(
        "Queda nos últimos 12 meses?",
        size=20,
        weight=ft.FontWeight.BOLD,
    )
    queda_sim_nao = ft.Dropdown(
        label="Sim ou não",
        width=150,
        options=[
            ft.dropdown.Option("Sim", "Sim"),
            ft.dropdown.Option("Não", "Não")
        ]
    )
    quantas_quedas = ft.TextField(
        label="Quantas?"
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
        label="Local:"
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
    preservada = ft.Checkbox(
        label="Preservada", value=False
    )
    ilimitada = ft.Checkbox(
        label="Ilimitada", value=False
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
    texto_direito_bicipital = ft.Text(
        "Bicipital",
        size=15,
        weight=ft.FontWeight.BOLD,
    )
    bicipital_direito = ft.Dropdown(
        label="",
        options=[
            ft.dropdown.Option("Ausente", "Ausente"),
            ft.dropdown.Option("Hiper", "Hiper"),
            ft.dropdown.Option("Hipo", "Hipo"),
            ft.dropdown.Option("Normo", "Normo")
        ]
    )
    texto_direito_tricciptal = ft.Text(
        "Triciptal",
        size=15,
        weight=ft.FontWeight.BOLD,
    )
    tricipital_direito = ft.Dropdown(
        label="",
        options=[
            ft.dropdown.Option("Ausente", "Ausente"),
            ft.dropdown.Option("Hiper", "Hiper"),
            ft.dropdown.Option("Hipo", "Hipo"),
            ft.dropdown.Option("Normo", "Normo")
        ]
    )

    texto_direito_estilorradial = ft.Text(
        "Estilorradial",
        size=15,
        weight=ft.FontWeight.BOLD,
    )
    estilorradial_direito = ft.Dropdown(
        label="",
        options=[
            ft.dropdown.Option("Ausente", "Ausente"),
            ft.dropdown.Option("Hiper", "Hiper"),
            ft.dropdown.Option("Hipo", "Hipo"),
            ft.dropdown.Option("Normo", "Normo")
        ]
    )
    texto_direito_cubitopronador = ft.Text(
        "Cúbitopronador",
        size=15,
        weight=ft.FontWeight.BOLD,
    )
    cubitopronador_direito = ft.Dropdown(
        label="",
        options=[
            ft.dropdown.Option("Ausente", "Ausente"),
            ft.dropdown.Option("Hiper", "Hiper"),
            ft.dropdown.Option("Hipo", "Hipo"),
            ft.dropdown.Option("Normo", "Normo")
        ]
    )
    texto_direito_patelar = ft.Text(
        "Patelar",
        size=15,
        weight=ft.FontWeight.BOLD,
    )
    patelar_direito = ft.Dropdown(
        label="",
        options=[
            ft.dropdown.Option("Ausente", "Ausente"),
            ft.dropdown.Option("Hiper", "Hiper"),
            ft.dropdown.Option("Hipo", "Hipo"),
            ft.dropdown.Option("Normo", "Normo")
        ]
    )
    texto_direito_aquileu = ft.Text(
        "Aquileu",
        size=15,
        weight=ft.FontWeight.BOLD,
    )
    aquileu_direito = ft.Dropdown(
        label="",
        options=[
            ft.dropdown.Option("Ausente", "Ausente"),
            ft.dropdown.Option("Hiper", "Hiper"),
            ft.dropdown.Option("Hipo", "Hipo"),
            ft.dropdown.Option("Normo", "Normo")
        ]
    )
    texto_direito_adutor = ft.Text(
        "Adutor",
        size=15,
        weight=ft.FontWeight.BOLD,
    )
    adutor_direito = ft.Dropdown(
        label="",
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
    texto_esquerdo_bicipital = ft.Text(
        "Bicipital",
        size=15,
        weight=ft.FontWeight.BOLD,
    )
    bicipital_esquerdo = ft.Dropdown(
        label="",
        options=[
            ft.dropdown.Option("Ausente", "Ausente"),
            ft.dropdown.Option("Hiper", "Hiper"),
            ft.dropdown.Option("Hipo", "Hipo"),
            ft.dropdown.Option("Normo", "Normo")
        ]
    )
    texto_esquerdo_tricciptal = ft.Text(
        "Tricciptal",
        size=15,
        weight=ft.FontWeight.BOLD,
    )
    tricipital_esquerdo = ft.Dropdown(
        label="",
        options=[
            ft.dropdown.Option("Ausente", "Ausente"),
            ft.dropdown.Option("Hiper", "Hiper"),
            ft.dropdown.Option("Hipo", "Hipo"),
            ft.dropdown.Option("Normo", "Normo")
        ]
    )

    texto_esquerdo_estilorradial = ft.Text(
        "Estilorradial",
        size=15,
        weight=ft.FontWeight.BOLD,
    )
    estilorradial_esquerdo = ft.Dropdown(
        label="",
        options=[
            ft.dropdown.Option("Ausente", "Ausente"),
            ft.dropdown.Option("Hiper", "Hiper"),
            ft.dropdown.Option("Hipo", "Hipo"),
            ft.dropdown.Option("Normo", "Normo")
        ]
    )
    texto_esquerdo_cubitopronador = ft.Text(
        "Cúbitopronador",
        size=15,
        weight=ft.FontWeight.BOLD,
    )
    cubitopronador_esquerdo = ft.Dropdown(
        label="",
        options=[
            ft.dropdown.Option("Ausente", "Ausente"),
            ft.dropdown.Option("Hiper", "Hiper"),
            ft.dropdown.Option("Hipo", "Hipo"),
            ft.dropdown.Option("Normo", "Normo")
        ]
    )
    texto_esquerdo_patelar = ft.Text(
        "Patelar",
        size=15,
        weight=ft.FontWeight.BOLD,
    )
    patelar_esquerdo = ft.Dropdown(
        label="",
        options=[
            ft.dropdown.Option("Ausente", "Ausente"),
            ft.dropdown.Option("Hiper", "Hiper"),
            ft.dropdown.Option("Hipo", "Hipo"),
            ft.dropdown.Option("Normo", "Normo")
        ]
    )
    texto_esquerdo_aquileu = ft.Text(
        "Aquileu",
        size=15,
        weight=ft.FontWeight.BOLD,
    )
    aquileu_esquerdo = ft.Dropdown(
        label="",
        options=[
            ft.dropdown.Option("Ausente", "Ausente"),
            ft.dropdown.Option("Hiper", "Hiper"),
            ft.dropdown.Option("Hipo", "Hipo"),
            ft.dropdown.Option("Normo", "Normo")
        ]
    )
    texto_esquerdo_adutor = ft.Text(
        "Adutor",
        size=15,
        weight=ft.FontWeight.BOLD,
    )
    adutor_esquerdo = ft.Dropdown(
        label="",
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
        label="D.D p/ D.L.E.: D.D p/ D.L.D", tristate=True
    )
    quatro_apoios = ft.Checkbox(
        label="4 apoios", tristate=True
    )
    quatro_ajoelhado = ft.Checkbox(
        label="4 apoios p/ajoelhado", tristate=True
    )
    semi_ajoelhado = ft.Checkbox(
        label="Semi ajoelhado p/ de pé", tristate=True
    )
    arrastar_cruzado = ft.Checkbox(
        label="Arrastar cruzado", tristate=True
    )
    dle = ft.Checkbox(
        label="D.L.E. p/ D.V.: D.L.D. p/ D.V", tristate=True
    )
    sentado = ft.Checkbox(
        label="Sentado", tristate=True
    )
    ajoelhado = ft.Checkbox(
        label="Ajoelhado p/semi ajoelhado", tristate=True
    )
    rolar = ft.Checkbox(
        label="Rolar", tristate=True
    )
    arrastar = ft.Checkbox(
        label="Arrastar homolateral", tristate=True
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

    # Adicionando os elementos na page
    """page.add(

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
        medicamentos_uso,
        queda_12meses,

        ft.Row([
            ft.Column(
                [ft.Container(queda_sim_nao)]),
            ft.Column(
                [ft.Container(quantas_quedas, width=200)])
        ]),

        ft.Container(texto_inspecao, padding=5, ),

        ft.Row([
            ft.Column(
                [ft.Container(hidratado), ft.Container(andador), ft.Container(cicatriz),
                 ft.Container(locomocao_independente), ft.Container(nao_colaborativo), ft.Container(hematoma),
                 ft.Container(rubor), ]),
            ft.Column(
                [ft.Container(muletas), ft.Container(cadeira_rodas), ft.Container(calor), ft.Container(colaborativo),
                 ft.Container(corado), ft.Container(edema), ft.Container(escara)]
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
                [ft.Container(hipertonia), ft.Container(hipertonia_plastica), ft.Container(hipertonia_elastica), ])
        ]),

        ft.Container(intensidade_hipertonia),

        ft.Container(texto_adm, padding=5, ),

        ft.Row([
            ft.Column(
                [ft.Container(preservada)]),
            ft.Column(
                [ft.Container(ilimitada)])
        ]),
        movimento_adm,

        ft.Container(texto_reflexos, padding=5),

        ft.Container(texto_reflexos_profundos),

        ft.Container(texto_direito),
        ft.Container(texto_direito_bicipital),
        ft.Container(bicipital_direito),
        ft.Container(texto_direito_tricciptal),
        ft.Container(tricipital_direito),
        ft.Container(texto_direito_estilorradial),
        ft.Container(estilorradial_direito),
        ft.Container(texto_direito_cubitopronador),
        ft.Container(cubitopronador_direito),
        ft.Container(texto_direito_patelar),
        ft.Container(patelar_direito),
        ft.Container(texto_direito_aquileu),
        ft.Container(aquileu_direito),
        ft.Container(texto_direito_adutor),
        ft.Container(adutor_direito),

        ft.Container(texto_esquerdo, ),
        ft.Container(texto_esquerdo_bicipital),
        ft.Container(bicipital_esquerdo),
        ft.Container(texto_esquerdo_tricciptal),
        ft.Container(tricipital_esquerdo),
        ft.Container(texto_esquerdo_estilorradial),
        ft.Container(estilorradial_esquerdo),
        ft.Container(texto_esquerdo_cubitopronador),
        ft.Container(cubitopronador_esquerdo),
        ft.Container(texto_esquerdo_patelar),
        ft.Container(patelar_esquerdo),
        ft.Container(texto_esquerdo_aquileu),
        ft.Container(aquileu_esquerdo),
        ft.Container(texto_esquerdo_adutor),
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
                [ft.Container(movimentos_coreicos), ft.Container(movimentos_atetoicos), ft.Container(fasciculacoes)]),
            ft.Column(
                [ft.Container(convulsoes), ft.Container(espasmos), ft.Container(tiques)]),
        ]),

        ft.Container(texto_atividades_funcionais),

        ft.Container(ddp),
        ft.Row([
            ft.Column(
                [ft.Container(quatro_apoios), ft.Container(quatro_ajoelhado), ft.Container(semi_ajoelhado),
                 ft.Container(arrastar_cruzado)]
            )
        ]),

        ft.Container(dle),
        ft.Row([
            ft.Column(
                [ft.Container(sentado), ft.Container(ajoelhado), ft.Container(rolar), ft.Container(arrastar)]
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
    )"""


ft.app(target=main, view=ft.AppView.FLET_APP)
