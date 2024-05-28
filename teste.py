import flet as ft

def main(page: ft.Page):
    page.title = "Relatorio Fisioterapia"
    page.window_width = 400
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = "adaptive"

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

    menu_topo = ft.AppBar(
        title=ft.Text("test", size=20, color="WHITE"),
        center_title=True,
        bgcolor=ft.colors.GREEN_ACCENT_700,
    )

    btn_enviar = ft.ElevatedButton(
        content=ft.Text("Enviar relatório", color="BLACK"),
        adaptive=True,
        bgcolor="WHITE",
        on_click=open_dlg,
        style=ft.ButtonStyle(
            padding=30,
            shape=ft.RoundedRectangleBorder(radius=5),
        ),
    )

    texto_relatorio = ft.Text(
        "test",
        size=25,
        weight=ft.FontWeight.BOLD,
    )
    numero_prontuario = ft.TextField(
        label="Nº do Prontuário"
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
  #AQUI EU TENTEI BOTAR TUDO EM UMA COLUNA, E NA COLUNA BOTAR O PARAMENTRO SCROLLMODE, DEU CERTO, POREM DENTRO DO VIEW NAO FUNCIONA, Só FORA,...
    coluna = ft.Column(
        [texto_relatorio,
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
         ft.Container(btn_enviar, alignment=ft.alignment.center),
         ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/"))],
        scroll=ft.ScrollMode.ADAPTIVE
    )

    # TESTE
    """def route_change(route):
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

        if page.route == "/relatorio_1":
            page.views.append(
                ft.View(

                    "/relatorio_1",
                    [
                        menu_topo,
                        coluna,

                    ],
                )
            )
        page.update()

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.scroll = ft.ScrollMode.ALWAYS
    page.go(page.route)"""
    page.add(
        coluna
    )

ft.app(target=main, view=ft.AppView.FLET_APP)
