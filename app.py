"""
This is a to-do app
Created By: ScriptPythonic
"""

import flet
from flet import *
from datetime import datetime
import sqlite3  


class FormContainer(UserControl):
    """
    This class defines a form container for adding tasks.
    """

    def __init__(self, func):
        self.func = func  
        super().__init__()

    def build(self):
        """
        Builds the UI components for the form container.
        """
        return Container(
            width=280, 
            height=80,
            bgcolor="bluegrey500",
            opacity=0,
            border_radius=40,
            margin=margin.only(left=20, right=20),
            animate=animation.Animation(400, "decelerate"),
            animate_opacity=200,
            padding=padding.only(top=45, bottom=45), 
            content=Column(
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    TextField(
                        height=48,
                        width=225,
                        filled=True,
                        hint_text="Description ......",
                        hint_style=TextStyle(size=11, color="black"),
                    ),
                    IconButton(
                        content=Text('Add Task'),
                        width=180, 
                        height=44,
                        on_click=self.func,  # pass the function here 
                        style=ButtonStyle(
                            bgcolor={"": 'black'},
                            shape={"": RoundedRectangleBorder(radius=8)},
                        )
                    ),
                ],
            ),
        )


class CreateTask(UserControl):
    """
    This class defines a task container for displaying tasks.
    """

    def __init__(self, task: str, date: str):
        self.task = task
        self.date = date
        super().__init__()

    def TaskDeleteEdit(self, name, color):
        """
        Creates a button for deleting or editing a task.
        """
        return IconButton(
            icon=name,
            width=30,
            icon_size=18,
            icon_color=color,
            opacity=0,
            animate_opacity=200,
            on_click=None,
        )

    def build(self):
        """
        Builds the UI components for the task container.
        """
        return Container(
            width=280,
            height=60,
            border=border.all(0.85, "white54"),
            border_radius=8,
            on_hover=None,
            clip_behavior=ClipBehavior.HARD_EDGE,
            padding=10,
            content=[
                Column(
                    spacing=1,
                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        Text(value=self.task, size=10),
                        Text(value=self.date, size=9, color="white54"),
                    ],
                ),
                Row(
                    spacing=0,
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                        self.TaskDeleteEdit(icons.DELETE_ROUNDED, "red500"),
                        self.TaskDeleteEdit(icons.EDIT_ROUNDED, "white700"),
                    ]
                )
            ],  
        )


def main(page: Page):
    """
    Main function to set up the page and handle interactions.
    """
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'

    def AddTaskToScreen(e):
        """
        Function to add a task to the screen.
        """
        dateTime = datetime.now().strftime("%b %d,  %Y %I:%M ")
        if form.content.controls[0].value:
            _main_column_.controls.append(
                CreateTask(
                    form.content.controls[0].value,
                    dateTime,
                )
            )
            _main_column_.update()

    def CreateToDoTask(e):
        """
        Function to show and hide the form container.
        """
        if form.height != 200:
            form.height, form.opacity = 200, 1
            form.update()
        else:
            form.height, form.opacity = 80, 0
            form.update()

    _main_column_ = Column(
        scroll='hidden',
        expand=True,
        alignment=MainAxisAlignment.START,
        controls=[
            Row(
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    Text("To-Do Items", size=18, weight="bold"),
                    IconButton(
                        icons.ADD_CIRCLE_ROUNDED,
                        icon_size=18,
                        on_click=lambda e: CreateToDoTask(e),
                    ),
                ],
            ),
            Divider(height=8, color="white24")
        ],
    )

    # Create the background and main container
    page.add(
        Container(
            width=1500,
            height=800,
            margin=10,
            bgcolor='bluegrey900',
            alignment=alignment.center,
            content=Row(
                alignment=MainAxisAlignment.CENTER,
                vertical_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Container(
                        width=280,
                        height=600,
                        bgcolor="#0f0f0f",
                        border_radius=40,
                        border=border.all(0.5, "white"),
                        padding=padding.only(top=35, left=20, right=20),
                        clip_behavior=ClipBehavior.HARD_EDGE,  # Clip content to the container
                        content=Column(
                            alignment=MainAxisAlignment.CENTER,
                            expand=True,
                            controls=[
                                _main_column_,
                                FormContainer(lambda e: AddTaskToScreen),
                            ]
                        )
                    )
                ],
            ),
        )
    )

    # Here is where all functions are being called
    page.update()
    form = page.controls[0].content.controls[0].content.controls[1].controls[0]

if __name__ == "__main__":
    flet.app(target=main)
