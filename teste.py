import flet as ft

def main(page: ft.Page):
    page.title = "Meu Primeiro App"
    page.padding = 16

    texto = ft.Text(
        "Olá Mundo!",
        size=32,
        weight=ft.FontWeight.BOLD
    )

    def mudar_texto(e):
        texto.value = "Botão clicado!"
        page.update()

    page.add(
        ft.Column(
            [
                texto,
                ft.ElevatedButton(
                    "Clique Aqui",
                    on_click=mudar_texto,
                    expand=True
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
        )
    )

ft.app(target=main)
