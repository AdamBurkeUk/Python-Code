import json
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip  # Module to copy generated password to clipboard
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
# Define character sets for password generation
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Generate random sequences of characters from each set
    password_letters = [choice(letters) for _ in range(randint(8,10))]
    password_symbols = [choice(symbols) for _ in range(randint(2,4))]
    password_numbers = [choice(numbers) for _ in range(randint(2,4))]

# Combine all characters and shuffle to randomize order
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

# Join list into string for the final password
    password = "".join(password_list)

# Insert the password into the password entry field and copy it to clipboard
    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():

# Retrieve entered data from the form
    website = website_entry.get()
    password = password_entry.get()
    email = email_entry.get()

# Structure new data for saving
    new_data = {website: {
        "email": email,
        "password": password,
    }}

# Validate that necessary fields are not empty
    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Error",message="Make sure all fields are filled!")
    else:
        try:
# Try to open the file to read existing data
            with open("data.json", "r") as data_file:
                data = json.load(data_file)  # Load existing data from file
        except FileNotFoundError:
# If file doesn't exist, create a new one and save the new data
            with open("data.json", "w") as data_file:
                json.dump(new_data,data_file,indent=4)
        else:
# Update loaded data with the new entry
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)   # Write updated data back to file
# Clear input fields after saving
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
# Retrieve website name entered by user
    website = website_entry.get()
    try:
# Attempt to read data from file
        with open("data.json","r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
# If file doesn't exist, show error message
        messagebox.showinfo(title="Error",message="No Data File Found.")
    else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website,message=f"Email: {email}\nPassword: {password}")
            else:
# If website is not found, inform the user
                messagebox.showinfo(title="Error",message=f"No Details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

# Canvas setup to display logo
canvas = Canvas(width=200,height=200)
background_image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=background_image)
canvas.grid(row=0,column=1)

#------------------------------Labels---------------------------------------#

website_label = Label(text="Website:")
website_label.grid(row=1,column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2,column=0)

password_label = Label(text="Password:")
password_label.grid(row=3,column=0)

# ---------------------------- Entries ------------------------------- #

website_entry = Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=1)
website_entry.focus()  # Set focus to this entry field

email_entry = Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=1)
email_entry.insert(0,"Adams_email.email")  # Pre-fill with a default email

password_entry = Entry(width=35)
password_entry.grid(row=3,column=1,columnspan=1)

# ---------------------------- Buttons------------------------------- #

generate_button = Button(text="Generate Password",command=password_generator)
generate_button.grid(row=3,column=2)

add_button = Button(text="Add",width=36,command=save_password)
add_button.grid(row=4,column=1,columnspan=2)

search_button = Button(text="Search", width=20 ,command=find_password)
search_button.grid(row=1,column=2)


window.mainloop()