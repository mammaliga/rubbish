from tkinter import *
from math import floor

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checks = []
my_timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    window.after_cancel(my_timer)
    title_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(text_canvas, text="00:00")
    check_label.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ---------------------------- #


def start_time():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps == 8:
        countdown(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 1:
        countdown(work_sec)
        title_label.config(text="Work", fg=GREEN)
    else:
        countdown(short_break_sec)
        title_label.config(text="Break", fg=RED)

# ---------------------------- COUNTDOWN MECHANISM ------------------------ #


def countdown(count):
    count_min = floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    canvas.itemconfig(text_canvas, text=f"{count_min}:{count_sec}")
    if count > 0:
        global my_timer
        my_timer = window.after(1000, countdown, count - 1)
    else:
        start_time()
        if reps % 2 == 0:
            checks.append("✔")
            check_label.config(text=checks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(
    text="Timer",
    bg=YELLOW,
    fg=GREEN,
    font=(
        FONT_NAME,
        36))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
text_canvas = canvas.create_text(
    103,
    130,
    text="00:00",
    fill="white",
    font=(
        FONT_NAME,
        28,
         "bold"))
canvas.grid(column=1, row=1)


start_btn = Button(
    text="Start",
    padx=0,
    pady=0,
    bg="white",
    command=start_time)
start_btn.grid(column=0, row=2)
reset_btn = Button(
    text="Reset",
    padx=0,
    pady=0,
    bg="white",
    command=reset_timer)
reset_btn.grid(column=2, row=2)

check_label = Label(
    bg=YELLOW,
    fg=GREEN)
check_label.grid(column=1, row=3)


window.mainloop()
