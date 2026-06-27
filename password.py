import random
import string
print("Password Generator")
length=int(input("Enter password length: "))
letters=string.ascii_letters
numbers=string.digits
symbols=string.punctuation
characters=letters+numbers+symbols
password = ""
for i in range(length):
    password+=random.choice(characters)
print("Generated Password:", password)
