import flet as ft


def main(page: ft.Page):
    page.title = "Meu Primeiro App"
    page.theme_mode = ft.ThemeMode.LIGHT

    texto = ft.Text(
        value="Olá Mundo!",
        size=30
    )

    def mudar_texto(e):
        texto.value = "Botão clicado!"
        page.update()

    botao = ft.ElevatedButton(
        text="Clique Aqui",
        on_click=mudar_texto
    )

    page.add(
        texto,
        botao
    )


ft.app(target=main)
