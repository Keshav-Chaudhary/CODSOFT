import tkinter as tk

def on_click(button_text):
    current_text = entry_var.get()
    if button_text == "=":
        try:
            result = eval(current_text)
            entry_var.set(result)
        except Exception as e:
            entry_var.set("Error")
    elif button_text == "C":
        entry_var.set("")
    elif button_text == "<-":
        entry_var.set(current_text[:-1])
    else:
        entry_var.set(current_text + button_text)

def on_key_press(event):
    key = event.char
    if key.isdigit() or key in "+-*/":
        on_click(key)
    elif key == "\r":  # Enter key
        on_click("=")
    elif key == "\x08":  # Backspace key
        on_click("<-")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Entry widget to display the input and results
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, justify="right", font=('Arial', 18))
entry.grid(row=0, column=0, columnspan=4)

# Define the calculator buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+',
    '<-'
]

# Add buttons to the grid
row_val = 1
col_val = 0
for button in buttons:
    tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 16),
              command=lambda b=button: on_click(b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Bind key presses to the on_key_press function
root.bind("<Key>", on_key_press)

# Run the Tkinter event loop
root.mainloop()
