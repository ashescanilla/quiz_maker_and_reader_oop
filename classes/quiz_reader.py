import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import sys

class QuizReader:
    def __init__(self):
        self.quiz_window = None
        self.timer_reference = None
        self.remaining_time_seconds = 15
        self.score_counter = 0
        self.current_question_text = ""
        self.current_choices_list = []
        self.correct_answer_choice_letter = ""
        self.answer_buttons = []
        self.list_of_quiz_questions = []

    def load_questions_from_file(self, file_path):
        questions = []
        question_text = None
        choices_list = []
        correct_choice_letter = None
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    line = line.strip()
                    if line.startswith("QUESTION:"):
                        if question_text:
                            questions.append((question_text, choices_list, correct_choice_letter))
                        question_text = line.replace("QUESTION: ", "")
                        choices_list = []
                        correct_choice_letter = None
                    elif line.startswith("ANSWER:"):
                        correct_choice_letter = line.replace("ANSWER: ", "").strip()
                    elif line.startswith(("A.", "B.", "C.", "D.")):
                        choices_list.append(line[3:].strip())
                if question_text:
                    questions.append((question_text, choices_list, correct_choice_letter))
        except FileNotFoundError:
            messagebox.showerror("File Not Found", f"The file '{file_path}' could not be found.")
            sys.exit(1)

        if not questions:
            messagebox.showerror("Empty File", "The quiz file is empty or has formatting errors.")
            sys.exit(1)

        return questions

    def load_new_question(self):
        if self.timer_reference:
            self.quiz_window.after_cancel(self.timer_reference)

        self.current_question_text, self.current_choices_list, self.correct_answer_choice_letter = random.choice(self.list_of_quiz_questions)
        self.question_label.config(text=self.current_question_text)

        for i, btn in enumerate(self.answer_buttons):
            letter = chr(65 + i)
            btn.config(
                text=f"{letter}. {self.current_choices_list[i]}",
                state="normal",
                command=lambda ltr=letter: self.check_answer(ltr)
            )

        self.feedback_label.config(text="")
        self.remaining_time_seconds = 15
        self.timer_label.config(text=f"Time remaining: {self.remaining_time_seconds} seconds")
        self.start_timer()

    def check_answer(self, selected_letter):
        if selected_letter == self.correct_answer_choice_letter:
            self.feedback_label.config(text="✅ Correct!", fg="blue", font=("Arial", 16, "bold"))
            self.score_counter += 1
            self.score_label.config(text=f"Score: {self.score_counter}")
        else:
            index = ord(self.correct_answer_choice_letter) - 65
            correct_text = self.current_choices_list[index]
            self.feedback_label.config(
                text=f"❌ Incorrect. The correct answer is: {self.correct_answer_choice_letter}. {correct_text}",
                fg="red", font=("Arial", 16, "bold")
            )
        for btn in self.answer_buttons:
            btn.config(state="disabled")

        if self.timer_reference:
            self.quiz_window.after_cancel(self.timer_reference)

        self.quiz_window.after(2000, self.load_new_question)

    def start_timer(self):
        if self.remaining_time_seconds > 0:
            self.remaining_time_seconds -= 1
            self.timer_label.config(text=f"Time remaining: {self.remaining_time_seconds} seconds")
            self.timer_reference = self.quiz_window.after(1000, self.start_timer)
        else:
            self.feedback_label.config(text="❌ Time's up! Moving to the next question...", fg="red", font=("Arial", 16, "bold"))
            for btn in self.answer_buttons:
                btn.config(state="disabled")
            self.quiz_window.after(2000, self.load_new_question)

    def launch_quiz(self):
        def on_close():
            if messagebox.askyesno("Exit Quiz", f"You scored {self.score_counter} points.\nDo you want to try again?"):
                self.quiz_window.destroy()
                self.show_start_screen()
            else:
                self.quiz_window.destroy()

        self.quiz_window = tk.Tk()
        self.quiz_window.title("Multiple Choice Quiz")
        self.quiz_window.geometry("700x600")
        self.quiz_window.configure(bg="#ffffff")
        self.quiz_window.protocol("WM_DELETE_WINDOW", on_close)

        self.list_of_quiz_questions = self.load_questions_from_file("quiz_data.txt")

        top_frame = tk.Frame(self.quiz_window, bg="#ffffff")
        top_frame.pack(fill="x", pady=(10, 0))

        self.timer_label = tk.Label(top_frame, text="Time remaining: 15 seconds", font=("Arial", 14), bg="#ffffff")
        self.timer_label.pack(side="left", padx=20)

        self.score_label = tk.Label(top_frame, text="Score: 0", font=("Arial", 14), bg="#ffffff")
        self.score_label.pack(side="right", padx=20)

        self.question_label = tk.Label(self.quiz_window, text="", wraplength=650, font=("Arial", 20, "bold"),
                                       justify="center", bg="#ffffff", padx=20, pady=20)
        self.question_label.pack(pady=30)

        self.answer_buttons = []
        for _ in range(4):
            btn = tk.Button(self.quiz_window, font=("Arial", 14), width=40, relief="raised",
                            bg="#4CAF50", fg="white", activebackground="#45a049", activeforeground="white",
                            padx=20, pady=10)
            btn.pack(pady=5)
            self.answer_buttons.append(btn)

        self.feedback_label = tk.Label(self.quiz_window, text="", font=("Arial", 16), bg="#ffffff")
        self.feedback_label.pack(pady=10)

        next_btn = tk.Button(self.quiz_window, text="Next Question", font=("Arial", 12),
                             bg="#008CBA", fg="white", activebackground="#006F8E", width=20, height=2,
                             command=self.load_new_question)
        next_btn.pack(pady=20)

        def exit_quiz():
            if messagebox.askyesno("Quiz Finished", f"You scored {self.score_counter} points.\nDo you want to try again?"):
                self.quiz_window.destroy()
                self.show_start_screen()
            else:
                self.quiz_window.destroy()

        exit_btn = tk.Button(self.quiz_window, text="Exit", font=("Arial", 12),
                             bg="#f44336", fg="white", activebackground="#c62828", width=20, height=2,
                             command=exit_quiz)
        exit_btn.pack(pady=(0, 20))

        self.remaining_time_seconds = 15
        self.timer_reference = None
        self.score_counter = 0

        self.load_new_question()
        self.quiz_window.mainloop()

    def show_start_screen(self):
        start_window = tk.Tk()
        start_window.title("Start Quiz")
        start_window.geometry("700x600")
        start_window.resizable(False, False)

        script_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(script_dir)
        image_path = os.path.join(project_root, "quiz_background.jpg")

        try:
            bg_image = Image.open(image_path)
            bg_image = bg_image.resize((700, 600), Image.Resampling.LANCZOS)
            background = ImageTk.PhotoImage(bg_image)
            bg_label = tk.Label(start_window, image=background)
            bg_label.image = background
            bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        except FileNotFoundError:
            messagebox.showwarning("Image Missing", f"Background image not found at:\n{image_path}\nUsing plain background.")
            start_window.configure(bg="#f0f0f0")

        def start_quiz():
            start_window.destroy()
            self.launch_quiz()

        start_btn = tk.Button(
            start_window, text="Start Quiz", font=("Arial", 16),
            bg="#008CBA", fg="white", activebackground="#005F8E",
            width=20, height=2, command=start_quiz
        )
        start_btn.place(relx=0.5, rely=0.85, anchor="center")
        start_window.mainloop()