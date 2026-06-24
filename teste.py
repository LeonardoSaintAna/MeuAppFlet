import flet as ft


def main(page: ft.Page):
    page.title = "Smart Home"

    # 🌙 Tema escuro confortável
    page.padding = 0
    page.bgcolor = "#0F172A"  # azul escuro suave (não preto puro)
    page.scroll = ft.ScrollMode.AUTO

    # -----------------------
    # Sensores simulados
    # -----------------------
    temperatura = ft.Text("24 °C", size=16, color="white", weight=ft.FontWeight.BOLD)
    umidade = ft.Text("65 %", size=16, color="white", weight=ft.FontWeight.BOLD)
    distancia = ft.Text("120 cm", size=16, color="white", weight=ft.FontWeight.BOLD)

    # -----------------------
    # SWITCH (visual moderno)
    # -----------------------
    def mudar_status(e):
        page.update()

    tomada_sala = ft.Switch(active_color="#22C55E", on_change=mudar_status)
    tomada_quarto = ft.Switch(active_color="#F59E0B", on_change=mudar_status)
    tomada_cozinha = ft.Switch(active_color="#EF4444", on_change=mudar_status)

    # -----------------------
    # CARD PADRÃO (dark)
    # -----------------------
    def card(content):
        return ft.Container(
            margin=ft.margin.only(bottom=12),
            padding=15,
            border_radius=16,
            bgcolor="#1E293B",  # azul escuro claro
            content=content,
        )

    # -----------------------
    # HEADER
    # -----------------------
    header = card(
        ft.Column(
            [
                ft.Text(
                    "🏠 Smart Home",
                    size=22,
                    weight=ft.FontWeight.BOLD,
                    color="#38BDF8",  # azul neon suave
                ),
                ft.Text(
                    "Controle residencial inteligente",
                    size=12,
                    color="#94A3B8",
                ),
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
                ft.Text("📡 Sensores", size=18, weight=ft.FontWeight.BOLD, color="#38BDF8"),
                ft.Divider(color="#334155"),

                ft.Row(
                    [ft.Icon(ft.icons.THERMOSTAT, color="#F97316"), ft.Text("Temperatura", color="white"), ft.Container(expand=True), temperatura]
                ),

                ft.Row(
                    [ft.Icon(ft.icons.WATER_DROP, color="#22C55E"), ft.Text("Umidade", color="white"), ft.Container(expand=True), umidade]
                ),

                ft.Row(
                    [ft.Icon(ft.icons.STRAIGHTEN, color="#38BDF8"), ft.Text("Distância", color="white"), ft.Container(expand=True), distancia]
                ),
            ]
        )
    )

    # -----------------------
    # TOMADAS
    # -----------------------
    tomadas = card(
        ft.Column(
            [
                ft.Text("🔌 Tomadas", size=18, weight=ft.FontWeight.BOLD, color="#38BDF8"),
                ft.Divider(color="#334155"),

                ft.Row(
                    [ft.Text("Sala", color="white"), ft.Container(expand=True), tomada_sala]
                ),

                ft.Divider(color="#334155", height=1),

                ft.Row(
                    [ft.Text("Quarto", color="white"), ft.Container(expand=True), tomada_quarto]
                ),

                ft.Divider(color="#334155", height=1),

                ft.Row(
                    [ft.Text("Cozinha", color="white"), ft.Container(expand=True), tomada_cozinha]
                ),
            ]
        )
    )

    # -----------------------
    # LAYOUT MOBILE
    # -----------------------
    page.add(
        ft.SafeArea(
            content=ft.Container(
                width=420,
                alignment=ft.alignment.center,
                content=ft.Column(
                    controls=[header, sensores, tomadas],
                    spacing=0,
                ),
            )
        )
    )


ft.app(target=main)
