# EXTRA CREDIT IMPLEMENTATIONS
#   - ADD A TASK DESCRIPTION FOR THE TASK
#   - ADD EDITING FEATURE THAT CAN EDIT EXISTING TASKS
#   - CREATED A DISPLAY OF HOW THE FULL TASK NAME WOULD DISPLAY BEFORE ADDING THE TASK (UPDATES ON  ANY CHANGE)



import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
text = ""
task = ""
def update_label(event = None):
    global task
    text = entry.get()  # Get the current text in the Entry
    selected_date = cal.get_date()  # Get the selected date from the Calendar
    selected_option = combobox.get()  # Get the current selection from the Combo Box
    description_text = description.get()
    task = text + " - Priority: " + selected_option + " - Due Date: " + selected_date + " - Description: " + description_text
    label.config(text=task)  # Update the Label with the current text

def on_calendar_change(event):
    update_label()

def on_combo_box_change(event):
    update_label()

def on_add_task(event = None):
    global task
    text = entry.get()  # Get the current text in the Entry
    if text.replace(" ", "") == "":
        return
    if task == "":
        return
    active_list_box.insert(tk.END, task)
    entry.delete(0, tk.END)
    description.delete(0, tk.END)
    task = ""
    label.config(text=task)  # Update the Label with the current text
    description_label.config(text=task)
    selected_option.set("High")



def on_complete_task(event = None):
    selected_indicies = active_list_box.curselection()
    if selected_indicies:
        index = selected_indicies[0]
        selected_task = active_list_box.get(index)
        complete_list_box.insert(tk.END, selected_task)
        active_list_box.delete(index)
    else:
        return

def on_remove_task(event = None):
    selected_indicies = complete_list_box.curselection()
    if selected_indicies:
        index = selected_indicies[0]
        complete_list_box.delete(index)
    else:
        return

def on_edit_task(event = None):
    global task
    global cal
    global options
    cal.selection_clear()
    window.update()
    selected_indicies = active_list_box.curselection()
    if selected_indicies:
        index = selected_indicies[0]
        selected_task = active_list_box.get(index)
        task_name = selected_task.split(" - Priority: ")[0]  # Extract task name
        priority_info = selected_task.split(" - Priority: ")[1]  # Extract priority and date information
        description_name = selected_task.split(" - Description: ")[1]  # Split by the description part

        print(selected_task)
        priority = priority_info.split(" - Due Date: ")[0]  # Extract priority
        due_date = priority_info.split(" - Due Date: ")[1]  # Extract due date
        cal.selection_set(due_date)
        selected_option.set(priority)

        entry.insert(0, task_name)
        label.config(text=selected_task)  # Update the Label with the current text
        description.insert(0, description_name)
        active_list_box.delete(index)

window = tk.Tk()
window.title("To-Do List App")


########################################################################################################################################################################
options = ["High", "Medium", "Low"]
selected_option = tk.StringVar(window)
selected_option.set(options[0]) 
combobox = ttk.Combobox(window, textvariable=selected_option, values=options, state='readonly', width=30)
combobox.pack(pady=40)
combobox.bind("<<ComboboxSelected>>", on_combo_box_change)  # Bind event when combo box selection changes

########################################################################################################################################################################
cal = Calendar(window)
cal.pack(pady=10)
cal.bind("<<CalendarSelected>>", on_calendar_change)  # Bind event when calendar date changes


add_task_frame = tk.Frame(window)
label = tk.Label(add_task_frame, text="To-Do Item")
label.pack(side=tk.LEFT, padx=5) 
########################################################################################################################################################################
task_name_frame = tk.Frame(window)

entry = tk.Entry(add_task_frame, width=30)
entry.bind("<KeyRelease>", update_label)  
entry.pack(side=tk.LEFT)  

description_label = tk.Label(add_task_frame, text="Description")
description_label.pack(side=tk.LEFT, padx=5) 
description = tk.Entry(add_task_frame, width=30)
description.bind("<KeyRelease>", update_label)
description.pack(side=tk.LEFT)

full_task_name_label = tk.Label(task_name_frame, text="Task: ")
full_task_name_label.pack(side=tk.LEFT)

label = tk.Label(task_name_frame, text="")
label.pack(pady=10)

add_task_button = tk.Button(add_task_frame, text="Add Task")
add_task_button.pack()
add_task_frame.pack(pady=10)
add_task_button.bind("<Button-1>", on_add_task)
task_name_frame.pack()
########################################################################################################################################################################

active_list_box = tk.Listbox(window, selectmode=tk.SINGLE, width=150, height=20)
mark_complete_button = tk.Button( text="Mark Complete", pady=10)
mark_complete_button.bind("<Button-1>", on_complete_task)
edit_task_button = tk.Button( text="Edit Task", pady=10)
edit_task_button.bind("<Button-1>", on_edit_task)
complete_list_box = tk.Listbox(window, selectmode=tk.SINGLE, width=150, height=10)
remove_complete_button = tk.Button(text="Remove Completed", pady=10)
remove_complete_button.bind("<Button-1>", on_remove_task)

active_list_box.pack()
mark_complete_button.pack()
edit_task_button.pack()
complete_list_box.pack()
remove_complete_button.pack()

########################################################################################################################################################################
window.mainloop()