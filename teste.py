import flet as ft


def main(page: ft.Page):
    page.title = "Smart Home"

    # 📱 base mobile
    page.bgcolor = "#0F172A"
    page.padding = 10

    # 🔥 IMPORTANTE: NÃO use page.scroll nem Column scroll aqui
    page.scroll = None

    # -----------------------
    # SENSOR DATA
    # -----------------------
    temperatura = ft.Text("24 °C", color="white", size=14, weight=ft.FontWeight.BOLD)
    umidade = ft.Text("65 %", color="white", size=14, weight=ft.FontWeight.BOLD)
    distancia = ft.Text("120 cm", color="white", size=14, weight=ft.FontWeight.BOLD)

    def mudar_status(e):
        page.update()

    tomada_sala = ft.Switch(active_color="#22C55E", on_change=mudar_status)
    tomada_quarto = ft.Switch(active_color="#F59E0B", on_change=mudar_status)
    tomada_cozinha = ft.Switch(active_color="#EF4444", on_change=mudar_status)

    # -----------------------
    # CARD BASE
    # -----------------------
    def card(content):
        return ft.Container(
            padding=12,
            margin=ft.margin.only(bottom=12),
            border_radius=14,
            bgcolor="#1E293B",
            content=content,
        )

    # -----------------------
    # HEADER
    # -----------------------
    header = card(
        ft.Column(
            [
                ft.Text("🏠 Smart Home", size=20, color="#38BDF8", weight=ft.FontWeight.BOLD),
                ft.Text("Controle residencial", size=11, color="#94A3B8"),
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
                ft.Text("📡 Sensores", size=16, color="#38BDF8", weight=ft.FontWeight.BOLD),
                ft.Divider(color="#334155"),
                ft.Row([ft.Text("Temp", color="white"), ft.Container(expand=True), temperatura]),
                ft.Row([ft.Text("Umid", color="white"), ft.Container(expand=True), umidade]),
                ft.Row([ft.Text("Dist", color="white"), ft.Container(expand=True), distancia]),
            ]
        )
    )

    # -----------------------
    # TOMADAS
    # -----------------------
    tomadas = card(
        ft.Column(
            [
                ft.Text("🔌 Tomadas", size=16, color="#38BDF8", weight=ft.FontWeight.BOLD),
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
    # 🔥 ROOT (VERSÃO QUE FUNCIONA NO ANDROID 0.22.1)
    # -----------------------
    page.add(
        ft.Column(
            expand=True,
            controls=[
                header,
                sensores,
                tomadas,
            ],
        )
    )


ft.app(target=main)
