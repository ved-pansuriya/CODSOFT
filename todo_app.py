import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3 as sql

# Global variables
tasks = []

# Add task function
def add_task():
    task_string = task_field.get()
    if len(task_string) == 0:
        messagebox.showinfo("Error", "Field is Empty.")
    else:
        tasks.append(task_string)
        the_cursor.execute('INSERT INTO tasks (title) VALUES (?)', (task_string,))
        the_connection.commit()
        list_update()
        task_field.delete(0, "end")

# Update listbox
def list_update():
    clear_list()
    for task in tasks:
        task_listbox.insert('end', task)

# Delete selected task
def delete_task():
    try:
        selected_task = task_listbox.get(task_listbox.curselection())
        if selected_task in tasks:
            tasks.remove(selected_task)
            the_cursor.execute('DELETE FROM tasks WHERE title = ?', (selected_task,))
            the_connection.commit()
            list_update()
    except:
        messagebox.showinfo("Error", "No Task Selected. Cannot Delete.")

# Delete all tasks
def delete_all_tasks():
    confirm = messagebox.askyesno("Delete All", "Are you sure?")
    if confirm:
        while len(tasks) != 0:
            tasks.pop()
        the_cursor.execute('DELETE FROM tasks')
        the_connection.commit()
        list_update()

# Clear listbox
def clear_list():
    task_listbox.delete(0, 'end')

# Close application
def close():
    print(tasks)
    guiWindow.destroy()

# Retrieve data from database
def retrieve_database():
    while len(tasks) != 0:
        tasks.pop()
    for row in the_cursor.execute('SELECT title FROM tasks'):
        tasks.append(row[0])

# GUI setup
guiWindow = tk.Tk()
guiWindow.title("To-Do List Manager Ved")
guiWindow.geometry("500x450+750+250")
guiWindow.resizable(0, 0)
guiWindow.configure(bg="#010000")  # Light grey background

# Database setup
the_connection = sql.connect('listofTasks.db')
the_cursor = the_connection.cursor()
the_cursor.execute('CREATE TABLE IF NOT EXISTS tasks (title TEXT)')

# Header frame
header_frame = tk.Frame(guiWindow, bg="#3E64FF")
header_frame.pack(fill="both")

header_label = ttk.Label(header_frame, text="To-Do List", font=("Alice", 30, "bold"),
                         background="#3E64FF", foreground="#000000")  # BLACK text
header_label.pack(padx=10, pady=10)

# Functions frame
functions_frame = tk.Frame(guiWindow, bg="#F5F5F5")
functions_frame.pack(side="left", expand=True, fill="both")

task_label = ttk.Label(functions_frame, text="Enter the Task:", font=("Alice", 11, "bold"),
                       background="#F5F5F5", foreground="#000000")  # BLACK
task_label.place(x=30, y=40)

task_field = ttk.Entry(functions_frame, font=("Consolas", 12), width=18)
task_field.place(x=30, y=80)

# Button styling with BLACK text
style = ttk.Style()
style.configure("TButton",
                font=("Segoe UI", 10, "bold"),
                foreground="#000000",  # BLACK
                background="#3E64FF")
style.map("TButton", background=[("active", "#324EDB")])

add_button = ttk.Button(functions_frame, text="Add Task", width=24, command=add_task)
add_button.place(x=30, y=120)

del_button = ttk.Button(functions_frame, text="Delete Task", width=24, command=delete_task)
del_button.place(x=30, y=160)

del_all_button = ttk.Button(functions_frame, text="Delete All Tasks", width=24, command=delete_all_tasks)
del_all_button.place(x=30, y=200)

exit_button = ttk.Button(functions_frame, text="Exit", width=24, command=close)
exit_button.place(x=30, y=240)

# Listbox frame
listbox_frame = tk.Frame(guiWindow, bg="")
listbox_frame.pack(side="right", expand=True, fill="both")

task_listbox = tk.Listbox(listbox_frame, width=26, height=13, selectmode='SINGLE',
                          background="#FFFFFF", foreground="#000000",  # BLACK text
                          selectbackground="#3E64FF", selectforeground="#FFFFFF")
task_listbox.place(x=10, y=20)

# Initial load
retrieve_database()
list_update()

# Start GUI loop
guiWindow.mainloop()

# Close database connection
the_connection.commit()
the_cursor.close()
