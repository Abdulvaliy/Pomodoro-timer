from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.05
SHORT_BREAK_MIN = 0.08
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")  # timer_text = "00:00"
    title_label.config(text="Timer", fg=GREEN)  # title_label "Timer"
    check.config(text="")  # reset check
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # if its the 8th rep:
    if reps == 8:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    # if its the 2nd/4th/6th rep:
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)

    # if its the 1st/3rd/5th/7th rep:
    else:
        count_down(work_sec)
        title_label.config(text="Work ", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = math.floor(count % 60)
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = int(math.floor(reps / 2))
        for _ in range(work_sessions):
            marks += "✔"
        check.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 135, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
title_label.grid(row=0, column=1)

start_button = Button(text="start", command=start_timer, font=("Arial", 12, "bold"), bg="white", highlightthickness=0,
                      padx=7, pady=5)
start_button.grid(row=2, column=0)

reset_button = Button(text="reset", command=reset_timer, font=("Arial", 12, "bold"), bg="white", highlightthickness=0,
                      padx=7, pady=5)
reset_button.grid(row=2, column=2)

check = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25))
check.grid(row=3, column=1)

window.mainloop()
