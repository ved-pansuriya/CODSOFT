import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.configure(bg="black")

# Entry widget for displaying input/output
entry = tk.Entry(root, font=("Arial", 24), bd=10, relief=tk.FLAT, 
                 justify='right', bg="#1f2b37", fg="white")
entry.grid(row=0, column=0, columnspan=4, sticky="nsew", ipady=20)

# Button click handler
def button_click(symbol):
    if symbol == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif symbol == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, symbol)

# Button layout
buttons = [
    ["C", "(", ")", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "⌫", "="]
]

# Button colors
colors = {
    "C": "#ea4533",
    "=": "#30da4a",
    "+": "#e67e22",
    "-": "#e67e22",
    "*": "#e67e22",
    "/": "#e67e22",
    "⌫": "#3498db"
}

# Create buttons
for i, row in enumerate(buttons):
    for j, btn_text in enumerate(row):
        color = colors.get(btn_text, "#3498db")
        button = tk.Button(root, text=btn_text, font=("Arial", 18), bg=color, fg="white", bd=0,
                           command=lambda symbol=btn_text: button_click(symbol))
        button.grid(row=i+1, column=j, sticky="nsew", padx=1, pady=1)

# Add backspace functionality
def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

# Overwrite ⌫ button to use backspace
root.grid_slaves(row=5, column=2)[0].configure(command=backspace)

# Make grid cells expand
for i in range(6):
    root.rowconfigure(i, weight=1)
for j in range(4):
    root.columnconfigure(j, weight=1)

root.mainloop()
