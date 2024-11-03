import tkinter as tk
from tkinter import messagebox

def button_click(number):
    """Handles button click to display numbers and operators."""
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def clear_entry():
    """Clears the calculator display."""
    entry.delete(0, tk.END)
    result_label.config(text="")  # Clear previous result

def backspace():
    """Deletes the last character from the display."""
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current[:-1])

def evaluate_expression():
    """Evaluates the mathematical expression entered."""
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))  # Keep the result in display
        result_label.config(text=f"{expression} = {result}")  # Show last calculation
    except Exception as e:
        messagebox.showerror("Error", "Invalid Expression")

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.configure(bg="black")

# Entry widget to display input and result
entry = tk.Entry(root, width=40, borderwidth=5, font=("Arial", 24), bg="black", fg="white", insertbackground="white")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=5)

# Label to show the last calculation in lighter color
result_label = tk.Label(root, text="", font=("Arial", 14), bg="black", fg="gray")
result_label.grid(row=1, column=0, columnspan=4)

# Define buttons and their positions
button_list = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
    ('0', 5, 0), ('.', 5, 1), ('+', 5, 2), ('=', 5, 3),
    ('Clear', 6, 0), ('←', 6, 1), ('Exit', 6, 2, 3)
]

# Create buttons dynamically
for item in button_list:
    text = item[0]
    row = item[1]
    col = item[2]
    colspan = item[3] if len(item) > 3 else 1

    if text == '=':
        btn = tk.Button(root, text=text, padx=30, pady=20, font=("Arial", 14),
                        command=evaluate_expression, bg="#333", fg="white")
    elif text == 'Clear':
        btn = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 14),
                        command=clear_entry, bg="#333", fg="white")
    elif text == '←':
        btn = tk.Button(root, text=text, padx=25, pady=20, font=("Arial", 14),
                        command=backspace, bg="#333", fg="white")
    elif text == 'Exit':
        btn = tk.Button(root, text=text, padx=25, pady=20, font=("Arial", 14),
                        command=root.quit, bg="#333", fg="white")
    else:
        btn = tk.Button(root, text=text, padx=30, pady=20, font=("Arial", 14),
                        command=lambda t=text: button_click(t), bg="#333", fg="white")
    
    btn.grid(row=row, column=col, columnspan=colspan, sticky="nsew")

# Configure grid layout to adjust buttons evenly
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(2, 7):
    root.grid_rowconfigure(i, weight=1)

# Run the GUI event loop
root.mainloop()
