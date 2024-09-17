import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK: str = "#e2979c"
RED: str = "#e7305b"
GREEN: str = "#9bdeac"
YELLOW: str = "#f7f5dd"
FONT_NAME: str = "Courier"
CHECK_MARK: str = "✔"
WORK_MIN: int = 25
SHORT_BREAK_MIN: int = 5
LONG_BREAK_MIN: int = 20
reps = 0
timer = ""


def reset_timer() -> None:
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    checkmark_label.config(text="")
    global reps
    reps = 0


def start_timer() -> None:
    global reps
    reps += 1
    work_sec: int = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)


def count_down(count: int) -> None:
    count_min: int = math.floor(count / 60)
    count_sec: int = count % 60
    if count_sec < 10:
        count_sec: str = f"0{count_sec}"
    if count_min < 10:
        count_min: str = f"0{count_min}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps / 2)):
            mark += CHECK_MARK
        checkmark_label.config(text=mark)



window: tkinter.Tk = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas: tkinter.Canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img: tkinter.PhotoImage = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))

timer_label: tkinter.Label = tkinter.Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50, "bold"), bg=YELLOW)
checkmark_label: tkinter.Label = tkinter.Label(fg=GREEN, font=(FONT_NAME, 16, "normal"), bg=YELLOW)
start_button: tkinter.Button = tkinter.Button(text="Start", command=start_timer)
reset_button: tkinter.Button = tkinter.Button(text="Reset", command=reset_timer)

timer_label.grid(column=1, row=0)
canvas.grid(column=1, row=1)
start_button.grid(column=0, row=2)
checkmark_label.grid(column=1, row=3)
reset_button.grid(column=2, row=2)

window.mainloop()
