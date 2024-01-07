import tkinter as tk
from tkinter import messagebox

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.root.geometry("500x500")

        self.score = 0
        self.current_question = 0

        self.questions, self.choices, self.correct_answers = load_quiz_questions()

        self.question_label = tk.Label(root, text="")
        self.question_label.pack(pady=10)

        self.radio_var = tk.StringVar()
        self.radio_var.set(None)

        self.radio_buttons = []
        for i in range(3):
            button = tk.Radiobutton(root, text="", variable=self.radio_var, value=chr(ord('A') + i), command=self.set_user_answer)
            button.pack(anchor=tk.W)
            self.radio_buttons.append(button)

        self.next_button = tk.Button(root, text="Next", command=self.next_question)
        self.next_button.pack(pady=10)

        self.root.bind("<KeyPress-a>", lambda event: self.keyboard_selection("A"))
        self.root.bind("<KeyPress-b>", lambda event: self.keyboard_selection("B"))
        self.root.bind("<KeyPress-c>", lambda event: self.keyboard_selection("C"))

        self.display_next_question()

    def set_user_answer(self):
        user_answer = self.radio_var.get()
        correct_answer = self.correct_answers[self.current_question]

        if user_answer == correct_answer:
            self.score += 1

    def display_next_question(self):
        if self.current_question < len(self.questions):
            self.question_label.config(text=self.questions[self.current_question])

            for i in range(3):
                self.radio_buttons[i].config(text=self.choices[self.current_question][i], value=chr(ord('A') + i))

            self.radio_var.set(None)
        else:
            self.show_final_results()

    def next_question(self):
        self.current_question += 1
        self.display_next_question()

    def show_final_results(self):
        percentage = (self.score / len(self.questions)) * 100
        result_message = f"Your final score is {self.score}/{len(self.questions)} ({percentage:.2f}%)."
        messagebox.showinfo("Quiz Complete", result_message)
        self.root.destroy()

    def keyboard_selection(self, option):
        if self.radio_var.get() == option:
            self.radio_var.set(None)
        else:
            self.radio_var.set(option)
            self.set_user_answer()
            self.next_question()



def load_quiz_questions():
    
    questions = [
        "What is the purpose of the 'volatile' keyword in C++?",
        "In Python, what is the difference between 'deep copy' and 'shallow copy'?",
        "What is a closure in JavaScript?",
        "Which programming language is known for its use in artificial intelligence and machine learning?",
        "In Java, what is the difference between '==', 'equals()', and 'hashCode()' methods when comparing objects?",
        "What does the acronym 'REST' stand for in the context of web services?",
        "In C#, what is the 'async' and 'await' feature used for?",
        "What is the primary use of the 'this' keyword in object-oriented programming?",
        "What is the difference between 'GET' and 'POST' HTTP methods?",
        "Explain the concept of 'polymorphism' in object-oriented programming.",
    ]
    
    choices = [
        ["A. It makes a variable immune to compiler optimizations.", "B. It ensures thread safety.", "C. It prevents memory leaks."],
        ["A. Shallow copy creates a new object, but it does not create copies of nested objects.", "B. Deep copy creates fully independent copies of objects and their nested objects.", "C. Shallow copy creates a duplicate with copies of nested objects."],
        ["A. A function that takes another function as an argument.", "B. A function that is defined inside another function.", "C. A function that returns an object."],
        ["A. Python", "B. Java", "C. R"],
        ["A. '==' compares object references, 'equals()' compares content, and 'hashCode()' generates a hash code for an object.", "B. '==' compares content, 'equals()' compares object references, and 'hashCode()' generates a hash code for an object.", "C. They all perform the same comparison operation."],
        ["A. Representational State Transfer", "B. Remote Execution of Stateful Tasks", "C. Responsive Element Service Technology"],
        ["A. It allows for parallel execution of code without blocking the main thread.", "B. It is used for handling asynchronous operations by providing a way to pause and resume execution.", "C. It is used for declaring a method as a background task."],
        ["A. It refers to the current instance of the class and is used to differentiate between instance variables and method parameters.", "B. It is used to access static members of the class.", "C. It is used to call the superclass constructor."],
        ["A. 'GET' is used for data retrieval, and 'POST' is used for submitting data to be processed to a specified resource.", "B. 'GET' is more secure than 'POST' as it encrypts data.", "C. 'POST' is suitable only for simple data types, while 'GET' is used for complex data."],
        ["A. It allows objects of different types to be treated as objects of a common type.", "B. It refers to the ability of a single function or method to work in different ways based on the input or the object it is acting upon.", "C. It is a technique used in relational databases to link tables together."]
    ]
    
    correct_answers = ["A", "B", "B", "A", "A", "A", "B", "A", "A", "B"]
    
    return questions, choices, correct_answers

# Rest of the code remains unchanged

    

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizGame(root)
    root.mainloop()
