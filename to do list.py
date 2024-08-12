
import tkinter as tk
from tkinter import simpledialog, messagebox

tasks = []

def add_task():
    task = simpledialog.askstring("Add Task", "Enter the task:")
    if task:
        tasks.append(task)
        update_task_list()

def edit_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_index = selected_task_index[0]
        new_task = simpledialog.askstring("Edit Task", "Edit the task:", initialvalue=tasks[task_index])
        if new_task:
            tasks[task_index] = new_task
            update_task_list()
    else:
        messagebox.showwarning("Edit Task", "Please select a task to edit.")

def delete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_index = selected_task_index[0]
        del tasks[task_index]
        update_task_list()
    else:
        messagebox.showwarning("Delete Task", "Please select a task to delete.")

def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

# Set up the main window
root = tk.Tk()
root.title("To-Do List")

# Set up the task list box
task_listbox = tk.Listbox(root, height=10, width=50)
task_listbox.pack(pady=20)

# Set up buttons
add_button = tk.Button(root, text="Add Task", width=15, command=add_task)
add_button.pack(side=tk.LEFT, padx=10)

edit_button = tk.Button(root, text="Edit Task", width=15, command=edit_task)
edit_button.pack(side=tk.LEFT, padx=10)

delete_button = tk.Button(root, text="Delete Task", width=15, command=delete_task)
delete_button.pack(side=tk.LEFT, padx=10)

# Run the application
root.mainloop()

