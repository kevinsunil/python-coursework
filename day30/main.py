# ---------------------------- MODULES ------------------------------- #
import tkinter
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
known_words = []
word_num = 0
timer = None
data_file = pandas.read_csv("./data/french_words.csv")


# ---------------------------- FRENCH ------------------------------- #
def french_word():
    global word_num
    word_num = random.randint(0, 99)
    word_french = data_file["French"][word_num]
    if word_french in known_words:
        french_word()
    else:
        screen_front.itemconfig(screen, image=front_img)
        screen_front.itemconfig(language_text, text="French")
        screen_front.itemconfig(word_text, text=word_french)
        countdown(5)


# ---------------------------- ENGLISH ------------------------------- #
def english_word():
    global word_num
    word_english = data_file["English"][word_num]
    screen_front.itemconfig(screen, image=back_img)
    screen_front.itemconfig(language_text, text="English")
    screen_front.itemconfig(word_text, text=word_english)


# ---------------------------- KNOWN WORDS ------------------------------- #
def known_word():
    global known_words
    global word_num
    known_words.append(data_file["French"][word_num])
    french_word()
    print(known_words)


# ---------------------------- TIMER MECHANISM ------------------------------- #

def countdown(count_sec):
    global timer
    if count_sec > 0:
        timer = window.after(1000, countdown, count_sec - 1)
    else:
        english_word()


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("French Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

screen_front = tkinter.Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_img = tkinter.PhotoImage(file="./images/card_front.png")
back_img = tkinter.PhotoImage(file="./images/card_back.png")
screen = screen_front.create_image(400, 263, image=front_img)
language_text = screen_front.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
word_text = screen_front.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
screen_front.grid(row=0, column=0, columnspan=2)

correct_img = tkinter.PhotoImage(file="./images/right.png")
button_1 = tkinter.Button(image=correct_img, highlightthickness=0, command=known_word)
button_1.grid(row=1, column=1)
wrong_img = tkinter.PhotoImage(file="./images/wrong.png")
button_2 = tkinter.Button(image=wrong_img, highlightthickness=0, command=french_word)
button_2.grid(row=1, column=0)
french_word()

window.mainloop()
