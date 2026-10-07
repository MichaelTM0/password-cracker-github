from itertools import product
from time import time

letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
special = " !#$%&*/()=?-_"
chars = letters + numbers + special

password = input("Enter your password: ")

# if the password uses a character we aren't testing, it can never be found
missing = [c for c in password if c not in chars]
if missing:
    print(f"This password contains characters not in the test set: {missing}")
    print("It can't be cracked with the current character set.")
else:
    start = time()
    attempts = 0
    found = False

    # try every combination of length 1, then 2, then 3... up to the password's length
    for length in range(1, len(password) + 1):
        for combo in product(chars, repeat=length):
            attempts += 1
            guess = "".join(combo)
            if guess == password:
                found = True
                break
        if found:
            break

    runtime = time() - start

    if found:
        print(f"Password cracked: {password!r}")
    else:
        print("Password not found.")
    print(f"Attempts: {attempts:,}")
    print(f"Runtime: {runtime:.4f} seconds")
