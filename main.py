from tkinter import *
import math


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 15
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
mark = None


# reset timer
def timer_reset():
    window.after_cancel(timer)
    mark = ""
    canvas.itemconfig(timer_text, text=f"00:00")
    title_label.config(text="Timer")
    global reps
    reps = 0


# countdown
def count_down(count):
    # get mins and seconds
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds == 0:
        seconds = "00"
    elif seconds < 10:
        seconds = f"0{seconds}"


    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")


    if count >= 0:
        global timer
        timer = canvas.after(1000, count_down, count - 1)
    else:
        start_counting()
        global mark
        mark = ""
        for i in range(math.floor(reps/2)):
            mark += "✓"
        check_mark_label.config(text=mark)





# start the count with start button
def start_counting():
    global reps
    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60
    reps += 1


    if reps % 8 == 0:
        count_down(long_break_seconds)
        title_label.config(text="Long Break")
    elif reps % 2 == 0:
        count_down(short_break_seconds)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_seconds)
        title_label.config(text="Work", fg=RED)


# Screen setup
window = Tk()
window.title("Pomodoro Clock")
window.config(bg=YELLOW, padx=100, pady=50)


# Insert photo and text
canvas = Canvas(width=215, height=224, bg=YELLOW, bd=0, highlightthickness=0)
pomodoro_img = PhotoImage(file='tomato.png')
canvas.create_image(105, 112, image=pomodoro_img)
timer_text = canvas.create_text(105, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=2, column=3)


# Labels
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 42, "bold"))
title_label.grid(row=1, column=3)
check_mark_label = Label(fg=GREEN, pady=20, bg=YELLOW, font=(FONT_NAME, 18, "bold"))
check_mark_label.grid(row=3, column=3)


# Buttons
start_button = Button(text="Start", command=start_counting)
start_button.grid(row=3, column=1)
reset_button = Button(text="Reset", command=timer_reset)
reset_button.grid(row=3, column=6)


window.mainloop()