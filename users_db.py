import pandas as pd
import hashlib
import csv 
import os

user_data = [
    [1, "Clara", "Pepit3h", "MDPsecr3t"],
    [2, "Paul", "FauxRapp3ur", "0uietN0n"],
    [3, "Sandra", "v0dka", "N0M0n3y"],
    [4, "Chef", "Jefe", "Allez"]
]

df = pd.DataFrame(user_data, columns = ["ID", "first_name", "username", "password"])

print(df)

with open('users.csv', 'w', newline='') as file :
    writer= csv.writer(file)
    field =  ["ID", "first_name", "username", "password"]
    writer.writerow(field)
    writer.writerows(user_data)


def hash_passwords() :
    df = pd.read_csv('users.csv')
    def generate_salt(length=16) : 
        return os.urandom(length).hex()
    def hash_value(password) : 
        salt = generate_salt()
        salted_password = salt + password
        hashed_password = hashlib.sha256(salted_password.encode()).hexdigest()
        return hashed_password, salt
    df[['password','salt']] = df['password'].apply(lambda x: pd.Series(hash_value(x)))
    df.to_csv('users_hashed_salted.csv',index=False)
    return df

hashed_df = hash_passwords()
print(hashed_df)