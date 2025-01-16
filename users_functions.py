import pandas as pd 
from datetime import date 
import os
import hashlib


def display_menu() : 
    print("\n Menu interactif : ")
    print("1. Connexion")
    print("2. Creer un compte ")
    option = input("Saisissez votre choix : ")
    return option


def load_hashed_user_data():
    user_data = {}
    df = pd.read_csv('users_hashed.csv')
    for _, row in df.iterrows() :
        user_data[row['username']] = {
            'password': row['password']
        }
    return user_data

def login() : 
    hashed_user_data = load_hashed_user_data()
    input_username = input("Saisissez votre nom d'utilisateur : ").strip()
    if input_username in hashed_user_data :
        input_password = input("Saisissez votre mot de passe : ").strip()
        hashed_password = hashed_user_data[input_username]['password']
        input_password_hash = hashlib.sha256(input_password.encode()).hexdigest()
        if input_password_hash == hashed_password :
            print("Connexion reussie ! ")

            user_main(input_username)
        else :
            print("Mot de passe incorrect.")
    else :
        print("Nom d'utilisateur introuvable, veuillez ressaisir ce champ : ")


def get_last_ID() : 
    df = pd.read_csv('users_hashed.csv')
    if not df.empty :
        last_id = df['ID'].iloc[-1]
        return last_id
    else :
        print("Le fichier csv est vide")
        return 0


def new_user() :
    last_id = get_last_ID()
    try :
        users_df = pd.read_csv('users_hashed.csv')
    except :
        users_df = pd.DataFrame(columns=["ID", "first_name", "last_name", "username", "password", "order_date"])

    new_name = input("Saisissez votre prenom : ")
    new_username = input("Saisissez votre nom d'utilisateur : ")
    new_password = input("Saisissez votre mot de passe : ")
    new_date = 'NA'
    new_id = last_id + 1

    folder_path = 'csv_files'
    if not os.path.exists(folder_path) :
        os.makedirs(folder_path)

    if new_username in users_df['username'].values :
        print("Ce nom d'utilisateur est deja prit")
        return 
    hashed_salted_password = hashlib.sha256(new_password.encode())

    new_user_data = {
        'ID': [new_id],
        'first_name': [new_name],
        'username': [new_username],
        'password': [hashed_salted_password],
    }
    new_df = pd.DataFrame(new_user_data)

    if not users_df.empty :
        new_df.to_csv('users_hashed.csv', mode='a',index=False, header=False)
    else :
        new_df.to_csv('users_hashed.csv', mode='w',index=False, header=True)
    print("Nouvel utilisateur ajouté avec succes !")

