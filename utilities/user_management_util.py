import sqlite3

class SQL_users:
    def __init__(self, db_name='users.db'):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        self.create_users_table()

    def create_users_table(self):
        create_table_query = """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                email TEXT NOT NULL,
                password TEXT NOT NULL,
                title TEXT NOT NULL
            );
        """
        self.cur.execute(create_table_query)
        self.conn.commit()
    
    def creating_user(self, username, email, password, title):
        adding_user = """
            INSERT INTO users(
                username,
                email,
                password,
                title
            )
            VALUES (
                ?,
                ?,
                ?,
                ?
            );
        """
        self.cur.execute(adding_user, (username, email, password, title)) # Add usename, email, password, title all in one row
        self.conn.commit()

    def delete_user(self, username, email, password, title):
        # Delete the user row where the email entered equals to "user_email"
        remove_user = """
            DELETE FROM users WHERE email = ?
        """
        self.cur.execute(remove_user, (email,))
        self.conn.commit()

    def password_update(self, email, new_password):
        # in users change the password where the email entered is equal to "user_email"
        updating_password = """
            UPDATE users 
            SET password = ?
            WHERE email = ?
        """
        self.cur.execute(updating_password, (new_password, email,)) 
        self.conn.commit()

    def email_update(self, email, new_email):
        updating_email = """
            UPDATE users
            SET email = ?
            WHERE email = ?
        """
        self.cur.execute(updating_email, (new_email, email))
        self.conn.commit()
    
    def title_update(self, title, new_title):
        updating_title = """
            UPDATE users
            SET title = ?
            WHERE title = ?
        """
        self.cur.execute(updating_title, (new_title, title))
        self.conn.commit()

    def select_all_users(self):
        # Select all data from users
        all_users = """
            SELECT * FROM users;
        """
        self.cur.execute(all_users)
        return self.cur.fetchall()
    
    def select_by_title(self, title):
        all_devs = """
            SELECT * FROM users WHERE title = ?;
        """
        self.cur.execute(all_devs, (title,))
        return self.cur.fetchall()
    
    def validate_password(self, email, password):
        fetch_password_on_file = """
            SELECT password
            FROM users
            WHERE email = ?
        """
        self.cur.execute(fetch_password_on_file, (email,))
        password_on_file = self.cur.fetchone()

        actual_password = password_on_file[0]
        if password != actual_password:
            print("wrong password!")

    def validate_username_taken(self, username, email, password, title):
        validating_existance = """
            SELECT username
            FROM users
            WHERE username = ?
        """
        self.cur.execute(validating_existance, (username,))
        username_on_file = self.cur.fetchone()

        if username_on_file:
            print("user exists!")
        else:
            self.creating_user(username, email, password, title)

    def total_users(self):
        count_users = """
            SELECT COUNT(*) FROM users
        """
        self.cur.execute(count_users)
        total = self.cur.fetchone()[0]
        return total

    def close(self):
        self.conn.close() 

db = SQL_users()

db.validate_username_taken('Jose', 'jrs31997@outlook.com', 'password123', 'dev')

db.close()