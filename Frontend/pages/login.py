import flet as ft

class Login(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.expand = True

        self.email = ft.Container(content=ft.TextField(label="Email", color="black"))

        self.password = ft.Container(content=ft.TextField(
            label="Password", 
            password=True, 
            can_reveal_password=True, color="black"))

        self.content = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    alignment=ft.alignment.center,
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls = [
                            ft.Text("Login To Do List", color="blue", size=30, weight=ft.FontWeight.BOLD),
                            self.email,
                            self.password,
                            ft.Container(
                                alignment=ft.alignment.center,
                                width=200,
                                height=40,
                                bgcolor="blue",
                                content=ft.Text("Login", weight=ft.FontWeight.BOLD),
                                on_click=lambda e: page.go("/home")
                            ),
                            ft.Container(
                                alignment=ft.alignment.center,
                                height=40,
                                content=ft.Text("Create Account", weight=ft.FontWeight.BOLD, color="black"),
                                on_click=lambda e: page.go("/signup")
                            )
                        ]
                    )
                )

            ]
        )