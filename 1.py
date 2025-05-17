import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task!")

def delete_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
    except:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def mark_completed():
    try:
        index = listbox.curselection()[0]
        task = listbox.get(index)
        listbox.delete(index)
        listbox.insert(tk.END, f"✔️ {task}")
    except:
        messagebox.showwarning("Selection Error", "Please select a task to mark complete.")

root = tk.Tk()
root.title("To-Do List")

# Entry widget for new task input
entry = tk.Entry(root, width=30, font=('Arial', 14))
entry.pack(pady=10)

# Add Task button
add_btn = tk.Button(root, text="Add Task", width=20, command=add_task)
add_btn.pack(pady=5)

# Listbox for tasks
listbox = tk.Listbox(root, width=40, height=10, font=('Arial', 12))
listbox.pack(pady=10)

# Buttons for mark complete and delete
complete_btn = tk.Button(root, text="Mark as Completed", width=20, command=mark_completed)
complete_btn.pack(pady=5)

delete_btn = tk.Button(root, text="Delete Task", width=20, command=delete_task)
delete_btn.pack(pady=5)

root.mainloop()
