import csv
import pandas as pd 
from book_menu import * 

def menu_inter():
    print("\n Menu Interactif :")
    print("1 : Afficher les livres")
    print("2 : Ajouter un livre")
    print("3 : Rechercher livre (par titre et par auteur)")
    print("4 : Trier les livres ( par prix et date de publication )")
    print("5 : Recherche avancée avec filtrage")
    option = input("Entrez votre choix : ")
    return option 

def menu_tri():
    print("Choisissez une manière de trier vos livres : ")
    print("1 : Trier par prix")
    print("2 : Trier par date de publication")
    choix_tri = input("Choisissez une manière (1/2) : ")

def view_books(books_data):
    try : 
        df = pd.read-csv(books_data.csv)
        print("Liste des livres : ")
        for index, row in df.iterrows():
            print(row['B_name'])
    except FileNotFoundError:
        print ("Le fichier csv est introuvable")

def new_book_id(): 
    try : 
        df = pd.read_csv(books_data.csv)
        last_id = df['ID'].max()
        return int(last_id) + 1 
    except FileNotFoundError:
        return 1 

def new_book():
    new_title = input("Saisissez le titre du livre : ")
    new_author = input("Saisissez le nom de l'auteur : ")
    new_price = input(" Saisissez le prix de ce livre : ")
    new_pub_date = input("Saisissez la date de publication de ce livre : ")
    new_id = new_book_id()
    new_row = [new_book_id, new_title, new_author, new_price, new_pub_date]

    book_df = pd.read_csv(columns = ["ID", "B_name", "Author", "B_price", "publication_date"])
    book_df.to_csv('books_data.csv', index = False, mode = 'a', header= not isfile('csv_files'))

    print("Ouvrage ajouté avec succès !")
    book_df = pd.read_csv(columns=["ID", "B_name", "Author", "B_price", "publication_date"])
    book_df.to_csv(books_data.csv, index=False)

def search_book():
    df = pd.read_csv(books_data.csv)
    book_to_search = input("Saisissez le nom du livre que vous cherchez : ")
    author_to_search = input("Saisissez le nom de l'auteur : ")
    if book_to_search in df["B_name"]:
        location = df["B_name"].index(book_to_search)
        return (f"Le livre {book_to_search} se trouve à {location}")
    else : 
        return (f"Le livre {book_to_search} est introuvable")
    if author_to_search in df["Author"]:
        location = df["Author"].index(author_to_search)
        return (f"L'auteur {author_to_search} se trouve à {location}")
    else : return (f"L'auteur {author_to_search} est introuvable")

def tri_prix():
    df = pd.read_csv(books_data.csv)
    df_tri_prix = df.sort_values(by = 'B_price', ascending= False)
    print("Livres rangés par prix")
    print(df_tri_prix)

def tri_date():
    df = pd.read_csv(books_data.csv)
    df_tri_date = df.sort_values(by = 'publication_date', ascending= False )
    print ("Livre rangés par date de publication")
    print(df_tri_date)

