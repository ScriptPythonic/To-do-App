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
    
    #create the backgrund  and  main container
    page.add(
        Container(
            width=1500,
            height=800,
            margin=10,
            bgcolor='bluegrey900'
        )
    )
    page.update()
    
    pass

if __name__ == "__main__":
    flet.app(target=main)
