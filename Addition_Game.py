import tkinter as tk
import random

# Create main window
root = tk.Tk()
root.title("Addition Game")

# Variables
num1 = 0
num2 = 0
answer_var = tk.StringVar()
result_var = tk.StringVar()
question_var = tk.StringVar()

# Functions
def generate_question(digits):
    global num1, num2
    lower = 10**(digits-1)
    upper = (10**digits) - 1
    num1 = random.randint(lower, upper)
    num2 = random.randint(lower, upper)
    question_var.set(f"{num1} + {num2} =")

def check_answer():
    try:
        user_answer = int(answer_var.get())
        if user_answer == num1 + num2:
            result_var.set("✓")
        else:
            result_var.set("✗")
    except ValueError:
        result_var.set("Enter a number")

# GUI Layout
# Question label
tk.Label(root, textvariable=question_var, font=('Arial', 20)).grid(row=0, column=0, columnspan=3, pady=10)

# Answer entry
tk.Entry(root, textvariable=answer_var, font=('Arial', 16)).grid(row=1, column=0, columnspan=2, pady=10)

# Check button
tk.Button(root, text="Check", command=check_answer).grid(row=1, column=2, padx=5)

# Result label
tk.Label(root, textvariable=result_var, font=('Arial', 24)).grid(row=2, column=1, pady=10)

# Digit buttons
tk.Button(root, text="1 digit", width=10, command=lambda: generate_question(1)).grid(row=3, column=0, pady=10)
tk.Button(root, text="2 digit", width=10, command=lambda: generate_question(2)).grid(row=3, column=1, pady=10)
tk.Button(root, text="3 digit", width=10, command=lambda: generate_question(3)).grid(row=3, column=2, pady=10)

# Start GUI
root.mainloop()