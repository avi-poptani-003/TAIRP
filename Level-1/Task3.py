import tkinter as tk
from tkinter import messagebox
import random
import time

class QuizApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Quiz Application")
        self.window.geometry("600x400")
        self.window.configure(bg="#1e1e2f")

        self.question_label = tk.Label(self.window, text="Question will appear here", font=("Arial", 16), bg="#1e1e2f", fg="white", wraplength=500)
        self.question_label.pack(pady=20)

        self.options = []
        for i in range(4):
            btn = tk.Button(self.window, text=f"Option {i+1}", font=("Arial", 14), command=lambda i=i: self.check_answer(i))
            btn.pack(pady=5)
            self.options.append(btn)

        self.score_label = tk.Label(self.window, text="Score: 0", font=("Arial", 14), bg="#1e1e2f", fg="white")
        self.score_label.pack(pady=10)

        self.timer_label = tk.Label(self.window, text="Time left: 10", font=("Arial", 14), bg="#1e1e2f", fg="white")
        self.timer_label.pack(pady=10)

        self.start_button = tk.Button(self.window, text="Start Quiz", font=("Arial", 16), bg="#28a745", fg="white", command=self.start_quiz)
        self.start_button.pack(pady=20)

        self.questions = self.load_questions()
        self.current_question = None
        self.score = 0
        self.time_left = 10
        self.timer_running = False

        self.window.mainloop()

    def load_questions(self):
        return [
            {"question": "What is the capital of France?", "options": ["Berlin", "Madrid", "Paris", "Rome"], "answer": 2},
            {"question": "Who wrote 'Hamlet'?", "options": ["Shakespeare", "Dickens", "Hemingway", "Austen"], "answer": 0},
            {"question": "What is 5 + 7?", "options": ["10", "12", "14", "15"], "answer": 1},
        ]

    def start_quiz(self):
        self.score = 0
        self.score_label.config(text="Score: 0")
        self.time_left = 10
        self.timer_running = True
        random.shuffle(self.questions)
        self.next_question()

    def next_question(self):
        if not self.questions:
            self.end_quiz()
            return

        self.current_question = self.questions.pop(0)
        self.question_label.config(text=self.current_question["question"])
        
        for i, option in enumerate(self.current_question["options"]):
            self.options[i].config(text=option)
        
        self.time_left = 10
        self.update_timer()

    def update_timer(self):
        if self.time_left > 0 and self.timer_running:
            self.timer_label.config(text=f"Time left: {self.time_left}")
            self.time_left -= 1
            self.window.after(1000, self.update_timer)
        elif self.timer_running:
            self.timer_label.config(text="Time's up!")
            self.next_question()

    def check_answer(self, selected_option):
        if self.current_question is None:
            return  
        
        if selected_option == self.current_question["answer"]:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")

        self.next_question()

    def end_quiz(self):
        self.timer_running = False
        messagebox.showinfo("Quiz Finished", f"Your final score is: {self.score}")

if __name__ == "__main__":
    QuizApp()
