from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    pyperclip.copy(password)
    password_input.delete(0, END)
    password_input.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) <= 0 or len(password) <= 0:
        messagebox.showinfo(message="Missing Fields, Please input all the details")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: Website input : "
                                                              f"{website}\n Email input: {email}\n Password input:{password}\n ")

        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    #load the data into a variable
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    #saving updated data
                    json.dump(data, data_file, indent=4)
                    #cleaning the text inputs
            finally:
                website_input.delete(0, END)
                password_input.delete(0, END)

#----------------------------- SEARCH PASSWORD -------------------------#
def search():
    website_info = website_input.get()
    try:
        with open("data.json", "r") as data_file:
            data= json.load(data_file)
            website_data = data[website_info]
            email = website_data["email"]
            password = website_data["password"]
    except FileNotFoundError:
        messagebox.showinfo(message="File Not Found")
    except KeyError:
        messagebox.showinfo(message="This website doesn't exist")
    else:
        messagebox.showinfo(message=f"The email is {email}\n The password is: {password}")

# ---------------------------- UI SETUP ------------------------------- #
my_window = Tk()
my_window.configure(padx=20, pady=20)
my_window.title("Password Generator")

#create canvas
canvas = Canvas(width=200, height=200)
my_img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=my_img)
canvas.grid(column=1, row=0)

#create labels
my_website = Label(text="Website")
my_website.grid(column=0, row=1)

my_email = Label(text="Email/Username")
my_email.grid(column=0, row=2)

my_password = Label(text="Password")
my_password.grid(column=0, row=3)

#Buttons
generate_password = Button(text="Generate Password", width=20, command=password)
generate_password.grid(column=2, row=3)

add_password = Button(text="Add", width=35, command=save)
add_password.grid(column=1, columnspan=2, row=4)

search_button = Button(text="Search", width=20, command=search)
search_button.grid(column=2, row=1)

#Text inputs
website_input = Entry(width=35)
website_input.grid(column=1, row=1)
website_input.focus()

email_input = Entry(width=35)
email_input.grid(column=1, row=2)
email_input.insert(0,"maybemar.hernandez@gmail.com")

password_input = Entry(width=35)
password_input.grid(column=1, row=3)

my_window.mainloop()