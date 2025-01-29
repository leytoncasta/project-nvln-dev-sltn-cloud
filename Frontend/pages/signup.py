import flet as ft
from utils.validation import Validation
import time

class SignUp(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

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

        if name and last_name and email and password and confirm_password:
            if not self.validation.validate_email(email):
                self.email.border = self.error_border
                self.error_field.value = "Invalid email"
                self.error_field.size = 12
                self.error_field.update()
                self.email.update()
                time.sleep(1)
                self.email.border = ft.border.all(color="red", width=1)
                self.error_field.size = 0
                self.error_field.update()
                self.email.update()

        else:
            self.error_field.value = "All fields are required"
            self.error_field.size=12
            self.error_field.update()
            time.sleep(1)
            self.error_field.size = 0
            self.error_field.update()