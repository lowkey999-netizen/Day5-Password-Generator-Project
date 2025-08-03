import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\nAnswer:"))
nr_symbols = int(input("How many symbols would you like?\nAnswer:"))
nr_numbers = int(input("How many numbers would you like?\nAnswer:"))

if nr_letters < 0 or nr_symbols < 0 or nr_numbers < 0:
    print("Please enter at least 1 letter and non-negative numbers for the rest.")
    exit()


the_password = ""
for i in range(nr_letters):
    the_password += random.choice(letters)

for i in range(nr_symbols):
    the_password += random.choice(symbols)

for i in range(nr_numbers):
    the_password += random.choice(numbers)

password = list(the_password)
random.shuffle(password)
final = "".join(password)
print(f"\nYour Password is:\n{final}")
