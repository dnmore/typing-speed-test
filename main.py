from tkinter import *
from tkinter import messagebox

FONT = "Georgia"
LIGHT_PINK = "#FFE6FF"
PURPLE = "#E371E9"

words = ["dark", "every", "few", "water", "person", "hard", "him", "kind", "show", "green", "gave", "strong", "learn",
         "complete", "game", "question", "wonder"]

user_typed_words = []

# --------------- Display word ------#

position = 0


def display_word():
    global position
    if position < len(words):
        words_box.config(text=words[position])
        position += 1
    else:
        position = 0
    get_user_entry()


# -------------- Get user entry ------------------ #

def get_user_entry():
    typed_word = user_input.get()
    user_typed_words.append(typed_word)
    user_input.delete(0, END)


# ------- Calculate WPM: Characters Typed in One Minute / 5 ---- #
# ----Source: https://www.typing.com/blog/what-is-words-per-minute/ ---#

def calculate_wpm():
    global user_typed_words
    char_list = ''.join(user_typed_words)
    total_chars_typed = len(char_list)
    wpm = total_chars_typed / 5
    return wpm


# -------------- Countdown mechanism ---------------#

def count_down(count):
    timer_label.config(text=f"Time: {count}s")
    if count > 0:
        window.after(1000, count_down, count - 1)
    if count == 0:
        messagebox.showinfo(title="Well Done!", message=f"Thanks for taking the test! Your WPM is {calculate_wpm()}")


# -------------- Start the timer ------ #

def start_timer():
    count_down(60)


# --------------- UI set up -----------------#


window = Tk()
window.title("Typing Speed")
window.config(pady=100, padx=100, bg=LIGHT_PINK)

title_label = Label(text="Test your typing speed", bg=LIGHT_PINK, font=(FONT, 25))
title_label.grid(column=1, row=0, columnspan=2)

start_button = Button(text="Start timer", bg=PURPLE, font=(FONT, 12), padx=10, border="0", cursor='hand2',
                      highlightthickness=0,
                      command=start_timer)
start_button.grid(column=1, row=1)

timer_label = Label(text="Time: 60s", bg=LIGHT_PINK, font=(FONT, 12))
timer_label.grid(column=2, row=1, pady=20, padx=10)

words_label = Label(text="Type the word below:", bg=LIGHT_PINK, font=(FONT, 16))
words_label.grid(column=1, row=2, columnspan=2, pady=10, padx=10)

words_box = Label(text="----", bg=LIGHT_PINK, font=(FONT, 16, "bold"))
words_box.grid(column=1, row=3, columnspan=2, pady=10, padx=10)

user_input = Entry(font=(FONT, 16))
user_input.grid(column=1, row=4, pady=40, padx=10)

next_button = Button(text="Next", bg=PURPLE, font=(FONT, 12), padx=10, border="0", cursor='hand2', highlightthickness=0,
                     command=display_word)
next_button.grid(column=2, row=4)

display_word()
window.mainloop()
