import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("600x400")
root.title("To Do List")

def add_command():
    task = ent.get().strip()
    if not task:
        messagebox.showwarning("Input Error", "You have not put any values.")
        return
    lbox.insert(tk.END, task)
    ent.delete(0, tk.END)

def mark_command():
    try:
        pos = lbox.curselection()[0]
        text = lbox.get(pos)
        lbox.delete(pos)
        lbox.insert(tk.END, f"{text} \u2713")
    except IndexError:
        messagebox.showwarning("Selection Error", "Nothing to mark. Select an item first.")

def del_command():
    try:
        pos = lbox.curselection()[0]
        lbox.delete(pos)
    except IndexError:
        messagebox.showwarning("Deletion Error", "Nothing to delete. Select an item first.")

lb1 = tk.Label(root, text="Enter task :", font=('calibri', 16))
lb1.place(x=15, y=20)

ent = tk.Entry(root, width=50)
ent.place(x=120, y=20)

lbox = tk.Listbox(root, width=50, height=10)
lbox.place(x=120, y=70)

btn1 = tk.Button(root, text="ADD", font=('calibri', 15), width=12, command=add_command)
btn1.place(x=50, y=250)

btn2 = tk.Button(root, text="MARK", font=('calibri', 15), width=12, command=mark_command)
btn2.place(x=230, y=250)

btn3 = tk.Button(root, text="REMOVE", font=('calibri', 15), width=12, command=del_command)
btn3.place(x=400, y=250)

root.mainloop()
