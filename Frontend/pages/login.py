import flet as ft
import httpx

class Login(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.bgcolor = "white"
        self.expand = True

        self.email = ft.TextField(label="Email", color="black")
        self.password = ft.TextField(
            label="Password", 
            password=True, 
            can_reveal_password=True, 
            color="black"
        )

        self.content = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    alignment=ft.alignment.center,
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Text("Login To Do List", color="blue", size=30, weight=ft.FontWeight.BOLD),
                            self.email,
                            self.password,
                            ft.Container(
                                alignment=ft.alignment.center,
                                width=200,
                                height=40,
                                bgcolor="blue",
                                content=ft.Text("Login", weight=ft.FontWeight.BOLD),
                                on_click=self.login_user
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

    async def login_user(self, e):
        email = self.email.value
        password = self.password.value

        # Prepare the payload for the API request
        payload = {
            "email": email,
            "contrasenia": password
        }

        # Make an asynchronous POST request to the FastAPI endpoint
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post("http://127.0.0.1:8000/usuarios/iniciar-sesion", json=payload)
                if response.status_code == 200:
                    # Successful login, navigate to the home page
                    self.page.go("/home")
                else:
                    # Handle login failure (e.g., show an error message)
                    self.page.snack_bar = ft.SnackBar(
                        content=ft.Text("Invalid credentials. Please try again."),
                        bgcolor="red"
                    )
                    self.page.snack_bar.open = True
                    self.page.update()
            except Exception as ex:
                # Handle any exceptions during the API call
                self.page.snack_bar = ft.SnackBar(
                    content=ft.Text(f"An error occurred: {str(ex)}"),
                    bgcolor="red"
                )
                self.page.snack_bar.open = True
                self.page.update()
