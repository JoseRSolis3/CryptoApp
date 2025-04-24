import hashlib
import os
from argon2 import PasswordHasher


password = "MySecretPassword"

def super_tron(password):
    ph = PasswordHasher(
        time_cost = 4, #number of iterations
        memory_cost = 65536, # per KB of memory
        parallelism = 3 # number of threads
    )
    hashed = ph.hash(password)

    try:
        ph.verify(hashed, password)
        print("Password Correct!")
    except:
        print("Incorrect Password!")

    return hashed

print(f"Hashed Password: {super_tron(password)}")
