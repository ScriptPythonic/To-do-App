"""
This is a to do app 
Created By : ScriptPythonic 
"""
import flet
from flet import *
from datetime import datetime
import sqlite3  

def main(page: Page):
    page.horizontal_alignment ='center'
    page.vertical_alignment='center'
    
    __main_column__ = Column(
        scroll='hidden
        expand=True'
    )
    
    #create the backgrund  and  main container
    page.add(
    Container(
        width=1500,
        height=800,
        margin=10,
        bgcolor='bluegrey900',  # Add a comma here
        alignment=alignment.center,
        content=Row(
            alignment=MainAxisAlignment.CENTER,  # Add a comma here
            vertical_alignment=CrossAxisAlignment.CENTER,  # Add a comma here
            controls=[
                Container(
                    width=280, 
                    height=600, 
                    bgcolor='#0f0f0f',
                    border_radius=40,
                        
                )
            ]
        )
    )
)

    page.update()
    
    pass

if __name__ == "__main__":
    flet.app(target=main)
