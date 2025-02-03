import flet as ft
import asyncio
import requests
from utils.validation import Validation

class SignUp(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        
        self.bgcolor = "white"
        self.expand = True
        self.validation = Validation()
        self.error_border = ft.border.all(color="red", width=1)
        self.error_field = ft.Text("", color="red", size=0)

        self.email = ft.Container(content=ft.TextField(label="Email", color="black"))
        self.name = ft.Container(content=ft.TextField(label="Name", color="black"))
        self.last_name = ft.Container(content=ft.TextField(label="Last Name", color="black"))

        self.password = ft.Container(content=ft.TextField(
            label="Password", 
            password=True, 
            can_reveal_password=True, color="black"))
        
        self.confirm_password = ft.Container(content=ft.TextField(
            label="Confirm Password", 
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
                            ft.Text("Registration", color="black", size=30, weight=ft.FontWeight.BOLD),
                            ft.Divider(color="black", height=1, thickness=1),
                            self.error_field,
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
                                on_click=self.signup,
                            ),
                            ft.Container(
                                alignment=ft.alignment.center,
                                height=40,
                                content=ft.Text("Have an account? login", weight=ft.FontWeight.BOLD, color="black"),
                                on_click=lambda e: page.go("/login")
                            )
                        ]
                    )
                )
            ]
        )

    def signup(self, e):
        print("this is our signup")
        name = self.name.content.value
        last_name = self.last_name.content.value
        email = self.email.content.value
        password = self.password.content.value
        confirm_password = self.confirm_password.content.value

        if not all([name, last_name, email, password, confirm_password]):
            self.show_error("All fields are required")
            return

        if not self.validation.validate_email(email):
            self.show_error("Invalid email", self.email)
            return

        if not self.validation.validate_password(password):
            self.show_error("Invalid Password", self.password)
            return

        if password != confirm_password:
            self.show_error("Passwords do not match", self.confirm_password)
            return

        # Prepare the data to send
        signup_data = {
            "user_name": name,
            "last_name": last_name,
            "email": email,
            "contrasenia": password,
            "imagen_perfil": "default.jpg"
        }

        # Send a POST request to the FastAPI backend
        try:
            response = requests.post("http://localhost:8000/usuarios", json=signup_data)
            if response.status_code == 200:
                self.show_error("Signup successful!", color="green")
                self.page.go("/login")
            else:
                self.show_error(f"Signup failed: {response.json().get('detail', 'Unknown error')}")
        except requests.exceptions.RequestException as e:
            self.show_error(f"An error occurred: {str(e)}")


    def show_error(self, message, field=None, color="red"):
        self.error_field.value = message
        self.error_field.color = color
        self.error_field.size = 12
        if field:
            field.border = self.error_border
            field.update()
        self.error_field.update()
        self.page.update()

        # Reset error message and border after 2 seconds
        if field:
            self.page.run_task(self.reset_field, field)
        self.page.run_task(self.reset_error)

    async def reset_field(self, field):
        await asyncio.sleep(2)
        field.border = None
        field.update()

    async def reset_error(self):
        await asyncio.sleep(2)
        self.error_field.size = 0
        self.error_field.value = ""
        self.error_field.update()

# Note: Ensure that your Validation class is correctly implemented for email and password validation.
