from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
data_dict = {}

try:
    data = pandas.read_csv('words_to_learn.csv')
except FileNotFoundError:
    data = pandas.read_csv('data/french_words.csv')
    data_dict = data.to_dict(orient='records')
else:
    data_dict = data.to_dict(orient='records')
finally:
    current_card = {}


def on_know_button_click():
    update_wordlist()
    next_card()


def update_wordlist():
    try:
        data_dict.remove(current_card)
    except ValueError:
        canvas.itemconfig(canvas_img, image=card_front_img)
        canvas.itemconfig(language_text, text='Nice', fill='black')
        canvas.itemconfig(word_text, text='Finished', fill='black')
    else:
        new_words = pandas.DataFrame(data_dict)
        new_words.to_csv('data/words_to_learn.csv', index=False)


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)

    current_card = random.choice(data_dict)
    canvas.itemconfig(canvas_img, image=card_front_img)
    canvas.itemconfig(language_text, text='French', fill='black')
    canvas.itemconfig(word_text, text=current_card['French'], fill='black')
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(canvas_img, image=card_back_img)
    canvas.itemconfig(language_text, text='English', fill='white')
    canvas.itemconfig(word_text, text=current_card['English'], fill='white')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file='images/card_front.png')
card_back_img = PhotoImage(file='images/card_back.png')
canvas_img = canvas.create_image(400, 268, image=card_front_img)
canvas.grid(column=0, columnspan=2, row=0)
language_text = canvas.create_text(400, 150, text='Title', fill='black', font=('Ariel', 40, 'italic'))
word_text = canvas.create_text(400, 263, text='word', fill='black', font=('Ariel', 60, 'bold'))

# Buttons
right_img = PhotoImage(file='images/right.png')
known_button = Button(image=right_img, highlightthickness=0, command=on_know_button_click)
known_button.grid(column=1, row=1)

wrong_img = PhotoImage(file='images/wrong.png')
unkown_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
unkown_button.grid(column=0, row=1)

next_card()

window.mainloop()
