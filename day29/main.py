# ---------------------------- MODULES ------------------------------- #
import tkinter
from tkinter import messagebox
import random
import pyperclip

FONT_NAME = "Courier"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    nr_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    nr_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    nr_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password = nr_letters + nr_numbers + nr_symbols
    random.shuffle(password)
    password_generated = "".join(password)
    Input_3.insert(0, password_generated)
    pyperclip.copy(password_generated)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = Input_1.get()
    email = Input_2.get()
    password = Input_3.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Reminder", message="Do not leave any fields empty")
    else:
        check_confirm = messagebox.askokcancel(title=website,
                                               message=f"The details entered are: \nEmail: {email} \nPassword:{password} "
                                                       f"\nProceed to save?")

        if check_confirm:
            with open("password_details.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")
                Input_1.delete(0, tkinter.END)
                Input_3.delete(0, tkinter.END)

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Generator")
# window.minsize(width=300, height=300)
window.config(padx=50, pady=50)

screen = tkinter.Canvas(width=200, height=200, highlightthickness=0)
logo_img = tkinter.PhotoImage(file="logo.png")
screen.create_image(100, 100, image=logo_img)
screen.grid(column=1, row=0)
label_1 = tkinter.Label(text="Website:")
label_1.grid(column=0, row=1)
label_2 = tkinter.Label(text="Email/Username:")
label_2.grid(column=0, row=2)
label_3 = tkinter.Label(text="Password:")
label_3.grid(column=0, row=3)

Input_1 = tkinter.Entry(width=35)
Input_1.grid(column=1, columnspan=2, row=1, sticky="EW")
Input_1.focus()
Input_2 = tkinter.Entry(width=35)
Input_2.grid(column=1, row=2, columnspan=2, sticky="EW")
Input_2.insert(0, "kevinsunil.2001@gmail.com")
Input_3 = tkinter.Entry(width=21)
Input_3.grid(column=1, row=3, sticky="EW")

button_1 = tkinter.Button(text="Generate Password", highlightthickness=0, command=password_gen)
button_1.grid(column=2, row=3, sticky="EW")
button_2 = tkinter.Button(text="Add", width=36, command=save, highlightthickness=0)
button_2.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
