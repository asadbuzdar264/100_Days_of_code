# Password Generator Project
# Easy Version
import random  # Importing random module to generate random characters
# List of possible letters (both lowercase and uppercase)
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
    'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
    'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
# List of possible numbers
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# List of possible symbols
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# Welcome message for the user
print("Welcome to the PyPassword Generator!")
# Asking the user how many letters, numbers, and symbols they want
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
# Selecting random letters, numbers, and symbols based on user input
letter_choice = random.choices(letters, k=nr_letters)
number_choice = random.choices(numbers, k=nr_numbers)
symbol_choice = random.choices(symbols, k=nr_symbols)
# Combining all chosen characters into a single list
data = letter_choice + number_choice + symbol_choice
# Creating the final password by joining the list into a string
init = ""
for item in data:
    init += item
# Displaying the generated password
print(init)

# Asadaf Writes
