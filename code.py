import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(number))

def button_clear():
    entry.delete(0, tk.END)
    history_var.set("")

def button_operation(operator):
    first_number = entry.get()
    global f_num
    global math_operation
    math_operation = operator
    f_num = float(first_number)
    entry.delete(0, tk.END)
    history_var.set(f"{f_num} {operator}")

def button_equal():
    second_number = entry.get()
    entry.delete(0, tk.END)
    history_text = history_var.get()
    
    try:
        if math_operation == "addition":
            result = f_num + float(second_number)
        elif math_operation == "subtraction":
            result = f_num - float(second_number)
        elif math_operation == "multiplication":
            result = f_num * float(second_number)
        elif math_operation == "division":
            result = f_num / float(second_number)
        else:
            raise ValueError("Invalid operation")

        entry.insert(0, result)
        history_var.set(f"{history_text} {second_number} = {result}")

    except Exception as e:
        entry.insert(0, "Error")
        history_var.set("Error")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Entry widget to display the input and results
entry = tk.Entry(root, width=16, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Variable to store and display the history
history_var = tk.StringVar()
history_label = tk.Label(root, textvariable=history_var, anchor="e", padx=10, pady=10)
history_label.grid(row=1, column=0, columnspan=4)

# Define buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

# Add buttons to the grid
row_val = 2
col_val = 0

for button in buttons:
    tk.Button(root, text=button, padx=20, pady=20,
              command=lambda b=button: button_click(b) if b.isdigit() or b in {'C', '=', '+', '-', '*', '/'} else None if b == 'C' else None if b in {'+', '-', '*', '/'} else button_operation(b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Run the application
root.mainloop()
