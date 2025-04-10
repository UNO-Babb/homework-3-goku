import tkinter as tk
from tkinter import messagebox
import turtle
import os

# trivia
questions = [
    {
        "question": "What is Goku's Saiyan birth name?",
        "options": ["Gohan", "Vegeta", "Kakarot", "Raditz"],
        "answer": "Kakarot"
    },
    {
        "question": "What transformation lets Goku fight Jiren on par?",
        "options": ["Super Saiyan Blue", "Ultra Instinct", "Super Saiyan God", "Kaio-ken x10"],
        "answer": "Ultra Instinct"
    },
    {
        "question": "Who was Goku's first teacher in martial arts?",
        "options": ["Master Roshi", "King Kai", "Grandpa Gohan", "Whis"],
        "answer": "Grandpa Gohan"
    }
]

current_question = 0
screen = None
goku = None
root = None
question_label = None
buttons = []

def check_answer(selected):
    global current_question
    if selected == questions[current_question]["answer"]:
        messagebox.showinfo("Correct!", "You got it right!")
        current_question += 1
        goku.forward(150)

        if current_question < len(questions):
            load_question()
        else:
            messagebox.showinfo("Victory!", "You finished the trivia!")
            root.destroy()
            screen.bye()
    else:
        messagebox.showerror("Wrong!", "That’s not the right answer.")

def load_question():
    question_label.config(text=questions[current_question]["question"])
    for i, option in enumerate(questions[current_question]["options"]):
        buttons[i].config(text=option, command=lambda opt=option: check_answer(opt))

def setup_turtle():
    global screen, goku
    screen = turtle.Screen()
    screen.title("Goku Progress Tracker")
    screen.setup(width=600, height=200)
    screen.bgcolor("black")

    gif_path = "GOKU.gif"
    if os.path.exists(gif_path):
        screen.register_shape(gif_path)
        shape = gif_path
    else:
        print("Goku GIF not found, using default turtle.")
        shape = "turtle"

    goku = turtle.Turtle()
    goku.penup()
    goku.shape(shape)
    goku.goto(-250, -50)
    goku.speed(1)

def setup_gui():
    global root, question_label, buttons
    root = tk.Tk()
    root.title("Goku Trivia Game")
    root.geometry("450x300")

    question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=400)
    question_label.pack(pady=20)

    for _ in range(4):
        btn = tk.Button(root, text="", width=40, font=("Arial", 12))
        btn.pack(pady=5)
        buttons.append(btn)

def main():
    setup_turtle()
    setup_gui()
    load_question()
    root.mainloop()

if __name__ == "__main__":
    main()
