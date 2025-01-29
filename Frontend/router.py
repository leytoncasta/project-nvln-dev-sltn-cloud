import flet as ft
from pages.login import Login
from pages.signup import SignUp
from pages.home import Home

def views_handler(page):
    return{
        "/login": ft.View(route="/login", bgcolor="white", padding=ft.padding.all(0), controls=[Login(page)]),
        "/signup": ft.View(route="/signup", bgcolor="white", padding=ft.padding.all(0), controls=[SignUp(page)]),
        "/home": ft.View(route="/home", bgcolor="black", padding=ft.padding.all(0), controls=[Home(page)]),
    }