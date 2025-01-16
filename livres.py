import csv
import pandas as pd 

books_data = [
    [1, "La vie devant soi", "Romain Gary", "8.50", "1975"],
    [2, "Les misérables", "Victor Hugo","5.80", "1862" ],
    [3, "Le Parfum", "Patrick Suskind", "7.99", "1985"],
    [4, "Le Comte de Monte-Cristo", "Alexandre Dumas", "9.50", "1846"],
    [5, "La métamorphose", "Franz Kafka", "2", "1915"],
    [6, "1984", "Georges Orwell", "6.99", "1949"]
]

df_books = pd.DataFrame(books_data, columns=["ID", "B_name", "Author", "B_price", "publication_date"])
df.to_csv('books_data.csv', index=False ) 

print(df_books)

with open('books_data.csv', 'w', newline='') as file : 
    writer = csv.writer(file)
    field = ["ID", "B_name", "Author", "B_price", "publication_date"]
    writer.writerow(field)
    writer.writerows(books_data)

