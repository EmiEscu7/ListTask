import tkinter as tk
import task

window = tk.Tk()
window.geometry("500x500")
task_manager = task.TaskManager()


def create_new_task():

    
    def save_info(name, description, date, time, priority):
        n_task = task.Task(name, description, date, time, priority)
        task_manager.addTask(n_task)
        new_wn.destroy()


    new_wn = tk.Tk()
    new_wn.geometry("350x350")
    new_wn.title("New Task")
    new_wn.resizable(False, False)
    title = tk.Label(new_wn, text="Create New Task")
    title.config(font=("Courier", 20))
    title.grid(row=0, column=0, columnspan=2)
    #enter name task
    label_name = tk.Label(new_wn, text="Task Name")
    label_name.grid(row=2, column=0)
    entry_name = tk.Entry(new_wn)
    entry_name.grid(row=2, column=1)
    #enter description task
    label_description = tk.Label(new_wn, text="Description")
    label_description.grid(row=4, column=0)
    entry_description = tk.Entry(new_wn)
    entry_description.grid(row=4, column=1)
    #enter date task
    label_date = tk.Label(new_wn, text="Date")
    label_date.grid(row=6, column=0)
    entry_date = tk.Entry(new_wn)
    entry_date.grid(row=6, column=1)
    #enter time task
    label_time = tk.Label(new_wn, text="Time")
    label_time.grid(row=8, column=0)
    entry_time = tk.Entry(new_wn)
    entry_time.grid(row=8, column=1)
    #enter priority task
    label_priority = tk.Label(new_wn, text="Priority")
    label_priority.grid(row=10, column=0)
    #VER COMO HACER PA PONER CIRUCLITOS CON OPCIONES
    #button to save info
    button_save = tk.Button(new_wn, text="Save", command=lambda: save_info(entry_name.get(), entry_description.get(), entry_date.get(), entry_time.get(), 1))
    button_save.grid(row=12, column=0)

def list_tasks():
    i = 2
    for task in task_manager.getTasks():
        task = tk.Label(window, text=task.getName() + " " + task.getDescription() + " " + task.getDate() + " " + task.getTime() + " " + str(task.getPriority()))
        task.config(font=("Courier", 10))
        task.grid(row=i, column=4)
        i += 1

new_task = tk.Button(window, text="+ New Task", width=10, height=10, command=lambda: create_new_task())
new_task.grid(row=2, column=1)
refresh_task = tk.Button(window, text="Refresh", width=10, height=10, command=lambda: list_tasks())
refresh_task.grid(row=3, column=1)


window.mainloop()