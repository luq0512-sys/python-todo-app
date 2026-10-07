import tkinter as tk

window = tk.Tk()
window.title("To-Do-List")
window.geometry("400x500")

task_list = tk.Listbox(
    window,
    width=40,
    height=15,
    font=("Arial", 12)
)

task_list.pack(pady=20)

task_entry = tk.Entry(
    window,
    width=30,
    font=("Arial", 12)
)

task_entry.pack(pady=10)

def add_task():

    task = task_entry.get()

    if task !="":
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)

add_button = tk.Button(
    window,
    text="Add Task",
    width=15,
    command=add_task
)

add_button.pack(pady=10)

def delete_task():
    selected = task_list.curselection()

    if selected:
        task_list.delete(selected[0])

delete_button = tk.Button(
    window,
    text="Delete Task",
    width=15,
    command=delete_task
)

delete_button.pack(pady=10)


window.mainloop()