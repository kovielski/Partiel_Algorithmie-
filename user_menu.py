import pandas as pd
import csv
from users_functions import * 
from users_db import * 

def user_main(username):
    users = 'users_hashed.csv'
    while True : 
        input = display_menu()
        if input == "1" :
            login()
        elif input == "2":
            new_user()
        elif input == "3":
            print("Fermeture du programme")
            break 
        else : 
            print("Champ invalide !")
