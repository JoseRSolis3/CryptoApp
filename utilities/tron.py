import hashlib
import os

password = "my_secret_password"

salt = os.urandom(16)

password_salt = password.encode() + salt

hashed_password = hashlib.sha256(password_salt).hexdigest()

print(f"Salt: {salt}")
print(f"Hashed Password: {hashed_password}")
