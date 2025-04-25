import sqlite3
import os
from crypto_data import get_crypto_price

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

    def create_user_data(self, crypto, current_shares):
        
        current_price = f"${get_crypto_price(crypto)}"
        share_value = current_price * current_shares

        creating_user_port = """
            INSERT INTO user_crypto(
                crypto,
                current_price,
                current_shares,
                share_value
            )
            VALUES(
                ?,
                ?,
                ?,
                ?
            )
        """
        self.cur.execute(creating_user_port, (crypto, current_price, current_shares, share_value))
        self.conn.commit()

    def update_crypto_price(self, crypto):
        #gets crypto name from button.
        current_price = get_crypto_price(crypto)

        updating_price = """
            UPDATE user_crypto
            SET current_price = ?
            WHERE crypto = ?
        """
        self.cur.execute(updating_price, (current_price, crypto))
        self.conn.commit()

    def update_shares(self, new_shares, crypto):
        formatted, price = get_crypto_price(crypto)
        new_share_value = f"${round(new_shares * price, 2)}"
        current_price = f"${formatted}"

        updating_shares = """
            UPDATE user_crypto
            SET current_shares = ?, share_value = ?, current_price = ?
            WHERE crypto = ?
        """
        self.cur.execute(updating_shares, (new_shares, new_share_value, current_price, crypto))
        self.conn.commit()

    def close(self):
        self.conn.close()

username = 'jose'
db = user_crypto(db_name = f"{username}_crypto_portfolio.db", username = "jose")
#db.create_user_crypto_table()
#db.create_user_data("pepe", 5000)
db.update_shares(new_shares=30000000, crypto="pepe")
db.close()