import flet as ft
import components.taskCreation as tc

class Home(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.bgcolor = "black"
        self.expand = True
        self.description = ft.TextField(hint_text="Description", color="white", text_size=12, content_padding=ft.padding.only(left=0))

        self.content = ft.Column(
            controls=[
                ft.Container(
                    alignment=ft.alignment.top_left,
                    bgcolor="black",
                    padding=ft.padding.symmetric(horizontal=30, vertical=5),
                    content=ft.Text("Today", color="white", size=40, weight=ft.FontWeight.BOLD),
                ),
                ft.Container(
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
                        on_click=self.remove_button
                    ),
                ),
                ft.Container(
                    ft.Divider(color="white", height=1, thickness=1),
                    padding=ft.padding.symmetric(horizontal=30, vertical=5)
                ),

                #-----------------------------------------
                
                #-----------------------------------------
            ]
        )
    
    def remove_button(self, e):
        # Remove the button container from the controls list
        self.content.controls.pop(1)
        self.content.controls.append(self.task_creation())
        # Update the UI
        self.update()
    
    def task_creation(self):
        ft.Column(
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
        