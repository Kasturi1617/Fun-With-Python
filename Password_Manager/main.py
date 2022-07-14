import tkinter
import random
from tkinter import messagebox, END
import pyperclip
import json

FONT = ("Courier", 13, "normal")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website_input = website_entry.get()
    email_input = email_entry.get()
    password_input = password_entry.get()

    if len(website_input) == 0 or len(email_input) == 0 or len(password_input) == 0:
        messagebox.showwarning(title="Oops :(", message="Please don't leave mandatory fields empty !")
    else:
        is_ok = messagebox.askokcancel(title=f"{website_input}",
                                       message=f"Entered details are:\n\n Email: {email_input}"
                                               f"\n Password: {password_input}\n Are you sure to save this?")
        new_data = {
            website_input: {
                "email": email_input,
                "password_input": password_input
            }
        }

        if is_ok:
            try:
                with open("data.json", mode="r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json", mode="w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", mode="w") as file:
                    json.dump(data, file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                website_entry.focus()


# ----------------------------SEARCH PASSWORD----------------------------#


def search_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showwarning(title="Error:(", message="Data file empty !")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password_input"]
            messagebox.showinfo(title=f"{website}", message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showwarning(title="Error:(", message=f"No details for {website} exists !")

# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()
window.title("Password Manager")
window.config(height=400, width=500, padx=50, pady=50)

# Logo
canvas = tkinter.Canvas(height=200, width=200)
my_logo = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=my_logo)
canvas.grid(row=0, column=1)

# Website name label
website_label = tkinter.Label(text="Website:", font=FONT)
website_label.grid(row=1, column=0)

# Website input box
website_entry = tkinter.Entry(width=35)
website_entry.grid(row=1, column=1)
website_entry.focus()

# Search button
search_button = tkinter.Button(text="Search", font=FONT,width=15, highlightthickness=0, command=search_password)
search_button.grid(row=1, column=2)

# Email Label
email_label = tkinter.Label(text="Email/Username:", font=FONT)
email_label.grid(row=2, column=0)

# Email input box
email_entry = tkinter.Entry(width=68)
email_entry.grid(row=2, column=1, columnspan=2)
# email_entry.insert(0, "kasturisanyal3@gmail.com")

# Password label
password_label = tkinter.Label(text="Password:", font=FONT)
password_label.grid(row=3, column=0)

# Password input
password_entry = tkinter.Entry(width=35)
password_entry.grid(row=3, column=1)

# Button to generate password
password_button = tkinter.Button(text="Generate Password", font=FONT, command=generate_password, highlightthickness=0)
password_button.grid(row=3, column=2)

# Button to add in file
add_button = tkinter.Button(text="Add", width=42, font=FONT, command=save_password, highlightthickness=0)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()