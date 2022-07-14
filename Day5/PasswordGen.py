import pyfiglet
from printy import printy
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F'>
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

ascii_banner = pyfiglet.figlet_format("PASS-GEN.PY")
printy(ascii_banner,'n')
n_letter = int(input("How many letters do you want in your password? "))
n_number = int(input("How many numbers do you want in your password? "))
n_symbol = int(input("How many symbols do you want in your password? "))

password_list = []
for i in range(1, n_letter + 1):
        password_list += random.choices(letters)
for i in range(1, n_number + 1):
        password_list += random.choices(numbers)
for i in range(1, n_symbol+1):
        password_list += random.choices(symbols)
#print(password_list)
random.shuffle(password_list)
#print(passsword_list)
password = ""
for i in password_list:
        password += i
printy(f"\nYour final password is {password}",'n')
