"""
This is a to do app 
Created By : ScriptPythonic 
"""
import flet
from flet import *
from datetime import datetime
import sqlite3  


class FormContainer(UserControl):
    def __init__(self):
        super().__init__()
        
    def build(self):
        return Container(
            width=280, 
            height=80,
            bgcolor="bluegrey500",
            opacity=1,
            border_radius=40,
            margin=margin.only(left=20, right=20),
            animate=animation.Animation(400,"decelerate"),
            animate_opacity=200,
            padding=padding.only(top=45,bottom=45), 
            content=Column(
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    TextField(
                        height=48,
                        width=225,
                        filled=True,
                        #border_color="transparent",
                        hint_text="Description ......",
                        hint_style=TextStyle(size=11, color="black"),
                    ),
                    IconButton(
                        content=Text('Add Task', width=180, 
                                     height=44,
                                     style=ButtonStyle(
                                         bgcolor={"": 'black'},
                                         shape={"": RoundedRectangleBorder(radius=8)},
                                     ))
                    ),
                ],
            ),
        )
        
def main(page: Page):
    page.horizontal_alignment ='center'
    page.vertical_alignment='center'
    
    #function to show and hide the form container
    
    def CreateToDoTask(e):
        if form.height != 200:
            form.height = 200
            form.update()
        else:
            form.height = 80
            form.update()
        pass
    
    __main_column__ = Column(
        scroll='hidden',
        expand=True,
        alignment=MainAxisAlignment.START,
        controls=[
            Row(
                alignment=MainAxisAlignment.SPACE_BETWEEN,  # Assuming your framework uses 'space-between' instead of MainAxisAlignment.SPACE_BETWEEN
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
    
    #create the backgrund  and  main container
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
                        border=border.all(0.5,"white"),
                        padding=padding.only(top=35,left=20,right=20),
                        clip_behavior=ClipBehavior.HARD_EDGE ,#clip content to the container
                        content= Column(
                            alignment=MainAxisAlignment.CENTER, 
                            expand=True,
                            controls=[
                                __main_column__,
                                FormContainer(),
                            ]
                        )
                    )
                ],
            ),
        )
    )

    page.update()
    form =page.controls[0].content.controls[0].content.controls[1].controls[0]

if __name__ == "__main__":
    flet.app(target=main)
