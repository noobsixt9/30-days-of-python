from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
#-----------------------------FIND PASSWORD---------------------------------------#
def find_password():
    website = website_entry.get()
   
    try:
        with open("data.json","r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message=f"No data found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email:{email}\nPassword:{password}")
        else:
            messagebox.showinfo(title="Error", message=f"No data found")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_number = [choice(numbers) for _ in range(randint(2, 4))]
    password_symmbol = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letter + password_number + password_symmbol
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get() 
    new_data = {
        website:
        {
            "email":email,
            "password":password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you have entered all details")
    else:
        try:
            #reading old data
            with open("data.json","r") as file:
                data = json.load(file)

        except FileNotFoundError:
            with open("data.json","w") as file:
                #saving updated data
                json.dump(new_data, file, indent=4)
        else:
            #updating old data 
            data.update(new_data)

            with open("data.json","w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=25, pady=25)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(column=2, row=1)

email_label = Label(text="Email:")
email_label.grid(column=0, row=2)
email_entry = Entry(width=35)
email_entry.insert(0, "randombullshit@go.com")
email_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password", width=15, command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=add)
add_button.grid(column=1, row=4, columnspan=2)

  
window.mainloop()
