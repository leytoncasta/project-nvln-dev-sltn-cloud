import flet as ft

class TaskCreation(ft.Container):
    def __init__(self):
        super().__init__()

        self.padding=ft.padding.symmetric(horizontal=30, vertical=1)
        self.description = ft.TextField(hint_text="Description", color="white", text_size=12, content_padding=ft.padding.only(left=0))

        self.content = ft.Column(
            controls = [
                ft.Text("New Task", color="white", size=15, weight=ft.FontWeight.BOLD),
                self.description,
                ft.Row(
                    alignment=ft.MainAxisAlignment.START,
                    controls=[
                        ft.Container(
                            content=ft.Row(
                                controls=[
                                    ft.Text("Today", color="green", size=13, weight=ft.FontWeight.BOLD),
                                    ft.Icon(name=ft.Icons.CALENDAR_TODAY, color="green", size=12),
                                ]
                            ),
                            padding=ft.padding.symmetric(horizontal=30, vertical=5),
                            border=ft.border.all(color="white", width=1),
                            border_radius=ft.border_radius.all(10)
                        ),
                        ft.Container(
                            content=ft.Row(
                                controls=[
                                    ft.Text("Category", color="green", size=13, weight=ft.FontWeight.BOLD)
                                ]
                            ),
                            padding=ft.padding.symmetric(horizontal=30, vertical=5),
                            border=ft.border.all(color="white", width=1),
                            border_radius=ft.border_radius.all(10),
                        ),
                        ft.Container(
                            content=ft.Row(
                                controls=[
                                    ft.Text("Status", color="green", size=13, weight=ft.FontWeight.BOLD)
                                ]
                            ),
                            padding=ft.padding.symmetric(horizontal=30, vertical=5),
                            border=ft.border.all(color="white", width=1),
                            border_radius=ft.border_radius.all(10),
                        ),
                    ],
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.END,
                    controls=[
                        ft.ElevatedButton(
                            content=ft.Text("Cancel", color="white", size=15),
                            bgcolor="red",
                        ),
                        ft.ElevatedButton(
                            content=ft.Text("Add", color="white", size=15),
                            bgcolor="green"
                        )
                    ]
                )
            ]
        )
