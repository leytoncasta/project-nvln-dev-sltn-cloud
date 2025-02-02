import datetime
import flet as ft

class Home(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.bgcolor = "black"
        self.expand = True
        self.description = ft.TextField(hint_text="Description", color="white", text_size=12, content_padding=ft.padding.only(left=0))
        self.title_page = ft.Container(
            alignment=ft.alignment.top_left,
            bgcolor="black",
            padding=ft.padding.symmetric(horizontal=30, vertical=5),
            content=ft.Text("Today", color="white", size=40, weight=ft.FontWeight.BOLD),
        )
        self.button_add_task = ft.Container(
            alignment=ft.alignment.center_left,
            padding=ft.padding.symmetric(horizontal=30, vertical=5),
            content=ft.Button(
                content=ft.Text("+ Add Task", color="white", size=15),
                style=ft.ButtonStyle(
                    padding=ft.Padding(20, 10, 20, 10),
                    side=ft.BorderSide(color="red", width=2),
                    alignment=ft.alignment.center_left,
                    bgcolor="red",
                    color="white"
                ),
                on_click=self.task_creation
            )
        )
        self.controls = [self.title_page, self.button_add_task]
        self.content = ft.Column(self.controls)

    def task_creation(self, e):
        print("Elements: ", len(self.controls))
        self.controls[1].visible = False
        self.controls[1].update()
        window_task = ft.Column(
            controls=[
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
                            border_radius=ft.border_radius.all(10),
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
                            on_click=self.cancel_task_creation
                        ),
                        ft.ElevatedButton(
                            content=ft.Text("Add", color="white", size=15),
                            bgcolor="green",
                        )
                    ]
                )
            ]
        )
        self.controls.append(window_task)
        self.content.controls = self.controls
        self.update()
        print("Elements: ", len(self.controls))

    def cancel_task_creation(self, e):
        self.controls.remove(self.controls[2])
        self.controls[1].visible = True
        self.content.controls = self.controls
        self.update()

        