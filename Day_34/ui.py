from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR: str = "#375362"
FONT: tuple[str, int, str] = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz: QuizBrain = quiz_brain
        self.window: Tk = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.score_label: Label = Label(bg=THEME_COLOR, fg="white", font=FONT, text="Score: 0")
        self.score_label.grid(column=1, row=0)

        self.canvas: Canvas = Canvas(width=300, height=250, bg="white")
        self.question_text: int = self.canvas.create_text(150, 125,
                                                          text="Some Question Text",
                                                          fill=THEME_COLOR,
                                                          font=FONT,
                                                          width=280
                                                          )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_img: PhotoImage = PhotoImage(file="images/true.png")
        self.ture_button: Button = Button(image=true_img, highlightthickness=0,
                                          command=lambda: self.check_answer(True))
        self.ture_button.grid(column=0, row=2)

        false_img: PhotoImage = PhotoImage(file="images/false.png")
        self.false_button: Button = Button(image=false_img, highlightthickness=0,
                                           command=lambda: self.check_answer(False))
        self.false_button.grid(column=1, row=2)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.ture_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_answer(self, answer: bool):
        if self.quiz.check_answer(str(answer)):
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
