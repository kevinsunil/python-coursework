import tkinter

# equivalent to screen from turtle module
window = tkinter.Tk()

# to change title
window.title("Test Program")

# minimum size of the application window
window.minsize(width=500, height=300)

# creating a label
label_1 = tkinter.Label(text="Test Label", font=("Arial", 22, "bold"))
# placing the label on the screen
# label_1.pack(side="left", expand=True)
# label_1.pack()
label_1.grid(column=1, row=0)
# changng the value of optional arguments
label_1["text"] = "New Test"
label_1.config(font=("Arial", 18))

# creating an input line/entry
entry = tkinter.Entry()
entry.grid(column=1, row=1)


# button function
def button_click():
    label_1.config(text=entry.get())


# creating a button
button = tkinter.Button(text="Click here", command=button_click)
button.place(x=210, y=70)

# to keep the screen stay open and wait for user instruction  and always at the end of the program
window.mainloop()
