import csv
import pandas as pd 
from livre_menu_inter import * 


def menu_interactif():
    book = f'books_data.csv'
    print("Choisissez une option :")
    while True:
        input = livre_menu_inter()
        if input == "1":
            view_books(livres)
        elif input == "2": 
            new_book(livres)
        elif input == "3":
            search_book(livres)
        elif input == "4":
            choix_tri = menu_tri(livres)



