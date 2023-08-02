import tkinter as tk
from tkinter import messagebox
from tkinter import*

win = tk.Tk()
win.title("To-Do App")
win.geometry("500x600")
win.resizable(False, False)
win.config(bg="#f2f2f2")

f1_font = ("Arial", 30, "bold")
f2_font = ("Arial", 16, "bold")
f3_font = ("Arial", 12)

#iconphoto

img=PhotoImage(file="todolist.png")
win.iconphoto(False,img)

# List to store tasks
tasks_list = []

def add_task():
    task_text = e1.get().strip()
    if task_text:
        tasks_list.append(task_text)
        update_tasks_list()
        e1.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        index_to_delete = selected_task_index[0]
        del tasks_list[index_to_delete]
        update_tasks_list()

def update_tasks_list():
    tasks_listbox.delete(0, tk.END)
    for task in tasks_list:
        tasks_listbox.insert(tk.END, task)

# Label
Label(win, text="To-Do List", font=f1_font, fg="#333", bg="#f2f2f2").pack(pady=20)

# Entry
e1 = Entry(win, font=f3_font, fg="#333", bg="#fff", borderwidth=0)
e1.pack(pady=10, padx=20, ipady=8, ipadx=10, fill=tk.X)

# Frame
f1_frame = Frame(win, height=300, width=450, bg="#f2f2f2", highlightthickness=1, highlightbackground="#ccc")
f1_frame.pack(pady=20)

# Listbox to display tasks
tasks_listbox = Listbox(f1_frame, font=f3_font, bg="#f2f2f2", selectbackground="#f2f2f2", selectforeground="#333", borderwidth=0, highlightthickness=0)
tasks_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Scrollbar
scrollbar = Scrollbar(f1_frame, command=tasks_listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
tasks_listbox.config(yscrollcommand=scrollbar.set)

# Button
b1 = Button(win, text="ADD TASK", font=f2_font, bg="#4CAF50", fg="#fff", relief=tk.FLAT, activebackground="#45a049", command=add_task)
b1.pack(pady=10)

b2 = Button(win, text="DELETE TASK", font=f2_font, bg="#f44336", fg="#fff", relief=tk.FLAT, activebackground="#d32f2f", command=delete_task)
b2.pack(pady=10)

win.mainloop()
