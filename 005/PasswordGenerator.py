print("---PASSWORD GENERATOR---")

import random as rand

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

indices = []
for index in range(0, nr_letters + nr_numbers + nr_symbols):
    indices.append(index)

password = []

for letter in range(0, nr_letters):
    selectedIndex = rand.choice(indices)
    password.insert(selectedIndex + 1, rand.choice(letters))
    indices.remove(selectedIndex)

for symbol in range(0, nr_symbols):
    selectedIndex = rand.choice(indices)
    password.insert(selectedIndex + 1, rand.choice(symbols))
    indices.remove(selectedIndex)

for number in range(0, nr_numbers):
    selectedIndex = rand.choice(indices)
    password.insert(selectedIndex + 1, rand.choice(numbers))
    indices.remove(selectedIndex)

strPassword = ""
for letter in password:
    strPassword += letter
print(f"Here is your password: {strPassword}")
