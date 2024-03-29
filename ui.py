from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window =  Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)  

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.text = self.canvas.create_text(150, 125, text="some question text fr", fill=THEME_COLOR, font=("Arial", 20, "italic"), width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        r_img = PhotoImage(file="images\\true.png")
        w_img = PhotoImage(file="images\\false.png")

        self.r_button = Button(image=r_img, command=self.check_right_button)
        self.r_button.grid(row=2, column=0)

        self.w_button = Button(image=w_img, command=self.check_wrong_button)
        self.w_button.grid(row=2, column=1,)

        self.get_next_question() 

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text)
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.text, text="You've reached the end of the quiz")
            self.r_button.config(state="disabled")
            self.w_button.config(state="disabled")

    def check_right_button(self) -> str:
        self.give_feedback(self.quiz.check_answer("True"))
    
    def check_wrong_button(self) -> str:
        self.give_feedback(self.quiz.check_answer("False"))
    
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else: 
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
       