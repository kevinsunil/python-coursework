import tkinter

Screen = tkinter.Tk()
Screen.title("Pop up screen")
Screen.minsize(width=200, height=100)
Screen.config(padx=20, pady=20)

label_1 = tkinter.Label(text="Miles")
label_1.grid(column=2, row=0)

entry_1 = tkinter.Entry(width=7)
entry_1.grid(column=1, row=0)

label_2 = tkinter.Label(text="convert to")
label_2.grid(column=0, row=1)

label_3 = tkinter.Label(text="Kilometer")
label_3.grid(column=2, row=1)

label_4 = tkinter.Label(text="0")
label_4.grid(column=1, row=1)


def button_click():
    value = int(entry_1.get())
    value *= 1.609
    label_4["text"] = round(value)


button_1 = tkinter.Button(text="Convert", command=button_click)
button_1.grid(column=1, row=2)

Screen.mainloop()
