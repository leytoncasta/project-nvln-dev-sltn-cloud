import flet as ft
from flet import CircleBorder

def main(page: ft.Page):
    page.title = "Gestión de Listas y Tareas"

    header = ft.Text("Today", size=50, weight="bold")
    spacer = ft.Container(height=20)

      # Create a circular container with the icon inside
    icon_container = ft.Container(
        content=ft.Icon(name=ft.Icons.ADD, color="white"),
        width=40,
        height=40,
        bgcolor="red",
        border_radius=20,
        alignment=ft.alignment.center
    )

    # Create a row with the icon container and the text
    button_content = ft.Row(
        controls=[
            icon_container,
            ft.Text("Add Task", color="white")
        ],
        alignment=ft.MainAxisAlignment.START,
        vertical_alignment=ft.CrossAxisAlignment.CENTER
    )

    task_button = ft.ElevatedButton(
        content=button_content,
        style=ft.ButtonStyle(
            padding=ft.Padding(20, 10, 10, 10),
            side=ft.BorderSide(color="red", width=2),
            alignment=ft.alignment.center_left,
            bgcolor="red",
            color="white"
        ),
        on_click=lambda e: print("Button Add Task clicked!")
    )

    button_container = ft.Container(
        content=task_button,
        alignment=ft.alignment.center_left,
        width=180  # Set the width of the button container
    )
    
    page.add(header, spacer, button_container)

ft.app(target=main)
