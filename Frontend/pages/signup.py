import flet as ft

class SignUp(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.expand = True

        self.email = ft.Container(content=ft.TextField(label="Email"))
        self.name = ft.Container(content=ft.TextField(label="Name"))
        self.last_name = ft.Container(content=ft.TextField(label="Last Name"))

        self.password = ft.Container(content=ft.TextField(
            label="Password", 
            password=True, 
            can_reveal_password=True))
        
        self.confirm_password = ft.Container(content=ft.TextField(
            label="Confirm Password", 
            password=True, 
            can_reveal_password=True))

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
                            ft.Text("Registration", color="black", size=30, weight=ft.FontWeight.BOLD),
                            ft.Divider(color="black", height=1, thickness=1),
                            self.name,
                            self.last_name,
                            self.email,
                            self.password,
                            self.confirm_password,
                            ft.Container(
                                alignment=ft.alignment.center,
                                width=200,
                                height=40,
                                bgcolor="blue",
                                content=ft.Text("Signup", weight=ft.FontWeight.BOLD),
                                on_click=lambda e: page.go("/login")
                            )
                        ]
                    )
                )

            ]
        )