import sqlite3
import os
from api.crypto_data import get_crypto_price

class user_crypto:
    def __init__(self, db_name, username):
        base_folder = "users"

        #user folder lives within the base folder
        user_folder = os.path.join(base_folder, username)   
        db_name = f"{username}_crypto_portfolio.db"
        db_path = os.path.join(user_folder, db_name)

        # If the base folder doesnt exist then create it
        if not os.path.exists(base_folder):
            os.mkdir(base_folder)

        # if the user folder doesnt exist then create it 
        if not os.path.exists(user_folder):
            os.mkdir(user_folder)         

        self.conn = sqlite3.connect(db_path)
        self.cur = self.conn.cursor()
        self.create_user_crypto_table()

    def create_user_crypto_table(self):
        create_crypto_table = """
        CREATE TABLE IF NOT EXISTS user_crypto(
            id INTEGER PRIMARY KEY,
            crypto TEXT NOT NULL,
            current_price REAL NOT NULL,
            current_shares REAL NOT NULL,
            share_value REAL NOT NULL
        );
        """
        self.cur.execute(create_crypto_table)
        self.conn.commit()

    def update_crypto_price(crypto, current_price):
        get_crypto_price(crypto)

    def close(self):
        self.conn.close()