from tkinter import *
from tkinter import messagebox
import random
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
    password_input.delete(0, END)
    password_input.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    data = f"{website_input.get()} | {email_input.get()} | {password_input.get()}\n"
    if len(website_input.get()) <= 0 or len(password_input.get()) <= 0:
        messagebox.showinfo(message="Missing Fields, Please input all the details")
    else:
        is_ok = messagebox.askokcancel(title=website_input.get(), message=f"These are the details entered: Website input : {website_input.get()}\n Email input: {email_input.get()}\n Password input:{password_input.get()}\n ")

        if is_ok:
            my_file= open("passwords.txt", "a")
            my_file.write(data)
            my_file.close()
            website_input.delete(0, END)
            password_input.delete(0, END)

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
generate_password = Button(text="Generate Password", command=password)
generate_password.grid(column=2, row=3)

add_password = Button(text="Add", width=35, command=save)
add_password.grid(column=1, columnspan=2, row=4)

#Text inputs
website_input = Entry(width=35)
website_input.grid(column=1, columnspan=2, row=1)
website_input.focus()

email_input = Entry(width=35)
email_input.grid(column=1, columnspan=2, row=2)
email_input.insert(0,"maybemar.hernandez@gmail.com")

password_input = Entry(width=21)
password_input.grid(column=1, row=3)

my_window.mainloop()