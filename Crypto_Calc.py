import requests
import hashlib

import json
from pathlib import Path

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# REGISTER USER

def register_user(username, password):
    path = Path("users.json")

    if not path.exists():
        with open(path, "w") as f:
            json.dump({"users": {}}, f, indent=4)

    with open(path, "r") as f:
        data = json.load(f)

    if username in data["users"]:
        print("User already exists!")
    
    data["users"][username] ={
        "password": hash_password(password),
        "strategies": [],
        "goals": []
    }

    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    
    print("User registered successfully.")
    return True

#USER LOG IN

def login_user(username, password):
    with open("users.json", "r") as f:
        data = json.load(f)
    
    user = data["users"].get(username)

    if not user:
        print("User does not exist.")
        print("Would you like to register? (y/n)\n")
        while True:
            choice = input()
            if choice == "y":
                register_user(username, password)
            elif choice == "n":
                break
            else:
                print("Please respond with y or n.")
    
    if user["password"] == hash_password(password):
        print("Login successful!")
        return True
    else:
        print("Incorrect password.")
        return False
    
def main_menu():
    while True:
        action = input("\n----------\nMain Menu\n\n1.register\n2.login\n3.quit\n----------\n").lower()
        
        if action == "1":
            u = input("Username: ")
            p = input("Password: ")
            register_user(u, p)

        elif action == "2":
            u = input("Username: ")
            p = input("Password: ")
            if login_user(u, p):
                print(f"Welcome back, {u}!")
                break

        elif action == "3":
            print("End of Line")
            break

        else:
            print("Invalid option.")


main_menu()

def get_crypto_price(crypto="bitcoin", currency="usd"):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies={currency}"
    response = requests.get(url)
    data = response.json()

    if crypto not in data:
        return "Error: crypto not in data"

    price = data[crypto][currency]
    formatted_price = "{:.20f}".format(price).rstrip('0').rstrip('.')

    return formatted_price

