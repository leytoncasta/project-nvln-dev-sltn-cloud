import flet as ft
from router import views_handler
from pages.login import Login
from pages.signup import SignUp
from pages.home import Home

def main(page: ft.Page):

    def route_change(route):
        page.clean()

        if page.route == "/login":
            page.add(Login(page))

        if page.route == "/signup":
            page.add(SignUp(page))
        
        if page.route == "/home":
            page.add(Home(page))

    page.on_route_change = route_change

    page.go("/login")

ft.app(target=main, view=None, port=60236, host="0.0.0.0")