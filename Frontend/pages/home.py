import flet as ft

class Home(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.content = ft.Column(
            controls=[
                ft.Text("Home", color="white", size=30, weight=ft.FontWeight.BOLD),
            ]
        )