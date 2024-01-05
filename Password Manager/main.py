from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))] + \
                    [choice(numbers) for _ in range(randint(2, 4))] + \
                    [choice(symbols) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, string=password)
    pyperclip.copy(password)
# for char in password_list:
#     password += char
# print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_text = website_entry.get()
    username_text = username_entry.get()
    password_text = password_entry.get()
    new_data = {
        website_text: {
            'email': username_text,
            'password': password_text,
        }
    }

    if len(website_text.strip()) == 0 or len(password_text.strip()) == 0:
        messagebox.showerror(title='Oops', message='Please dont live any fields empty!')
    else:
        try:
            with open('data.json', mode='r') as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open('data.json', mode='w') as data_file:
                # Saving updating data
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open('data.json', mode='w') as data_file:
                # Saving updating data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website_text = website_entry.get()
    try:
        with open('data.json', mode='r') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title='Error', message='No Data File Found')
    else:
        if website_text in data:
            email = data[website_text]['email']
            password = data[website_text]['password']
            messagebox.showinfo(title=website_text, message=f'Email: {email}\nPassword: {password}')
        else:
            messagebox.showinfo(title="Error", message=f'No details for the {website_text} exists')

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
padlock_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=padlock_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text='Website:')
website_label.grid(column=0, row=1)
username_label = Label(text='Email/Username:')
username_label.grid(column=0, row=2)
password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

# Entry
website_entry = Entry(width=19)
website_entry.focus()
website_entry.grid(row=1, column=1)
username_entry = Entry(width=35)
username_entry.insert(END, string='henriqueorei@gmail.com')
username_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=19)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text='Generate Password', highlightthickness=0, width=15, command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text='Add', highlightthickness=0, width=35, command=save)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text='Search', highlightthickness=0, width=15, command=find_password)
search_button.grid(row=1, column=2)

window.mainloop()