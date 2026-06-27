"""PASSWORD GENERATOR PROGRAM"""
import random
import string
print("Password Generator")
length=int(input("Enter password length: "))
LETTERS=string.ascii_letters
NUMBERS=string.digits
SYMBOLS=string.punctuation
CHARACTERS=LETTERS+NUMBERS+SYMBOLS
password = ""
for i in range(length):
    password+=random.choice(CHARACTERS)
print("Generated Password:", password)
