import flet as ft


def main(page: ft.Page):
    page.title = "Smart Home"

    # 🌙 fundo
    page.bgcolor = "#0F172A"
    page.padding = 10

    # 🔥 IMPORTANTE: garante render no mobile
    page.scroll = None

    # -----------------------
    # Sensores
    # -----------------------
    temperatura = ft.Text("24 °C", color="white", weight=ft.FontWeight.BOLD)
    umidade = ft.Text("65 %", color="white", weight=ft.FontWeight.BOLD)
    distancia = ft.Text("120 cm", color="white", weight=ft.FontWeight.BOLD)

    # -----------------------
    # Switch
    # -----------------------
    def mudar_status(e):
        page.update()

    tomada_sala = ft.Switch(active_color="#22C55E", on_change=mudar_status)
    tomada_quarto = ft.Switch(active_color="#F59E0B", on_change=mudar_status)
    tomada_cozinha = ft.Switch(active_color="#EF4444", on_change=mudar_status)

    # -----------------------
    # CARD PADRÃO
    # -----------------------
    def card(content):
        return ft.Container(
            padding=15,
            margin=ft.margin.only(bottom=12),
            border_radius=16,
            bgcolor="#1E293B",
            content=content,
        )

    # -----------------------
    # HEADER
    # -----------------------
    header = card(
        ft.Column(
            [
                ft.Text("🏠 Smart Home", size=22, color="#38BDF8", weight=ft.FontWeight.BOLD),
                ft.Text("Controle residencial inteligente", color="#94A3B8"),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

    # -----------------------
    # SENSORES
    # -----------------------
    sensores = card(
        ft.Column(
            [
                ft.Text("📡 Sensores", size=18, color="#38BDF8", weight=ft.FontWeight.BOLD),
                ft.Divider(color="#334155"),

                ft.Row([ft.Icon(ft.icons.THERMOSTAT, color="#F97316"), ft.Text("Temperatura", color="white"), ft.Container(expand=True), temperatura]),
                ft.Row([ft.Icon(ft.icons.WATER_DROP, color="#22C55E"), ft.Text("Umidade", color="white"), ft.Container(expand=True), umidade]),
                ft.Row([ft.Icon(ft.icons.STRAIGHTEN, color="#38BDF8"), ft.Text("Distância", color="white"), ft.Container(expand=True), distancia]),
            ]
        )
    )

    # -----------------------
    # TOMADAS
    # -----------------------
    tomadas = card(
        ft.Column(
            [
                ft.Text("🔌 Tomadas", size=18, color="#38BDF8", weight=ft.FontWeight.BOLD),
                ft.Divider(color="#334155"),

                ft.Row([ft.Text("Sala", color="white"), ft.Container(expand=True), tomada_sala]),
                ft.Divider(height=1, color="#334155"),

                ft.Row([ft.Text("Quarto", color="white"), ft.Container(expand=True), tomada_quarto]),
                ft.Divider(height=1, color="#334155"),

                ft.Row([ft.Text("Cozinha", color="white"), ft.Container(expand=True), tomada_cozinha]),
            ]
        )
    )

    # -----------------------
    # 🔥 ROOT (ISS OQUE FAZ FUNCIONAR NO CELULAR)
    # -----------------------
    page.add(
        ft.SafeArea(
            content=ft.Container(
                expand=True,
                content=ft.ListView(
                    expand=True,
                    spacing=10,
                    controls=[
                        header,
                        sensores,
                        tomadas,
                    ],
                ),
            )
        )
    )


ft.app(target=main)
