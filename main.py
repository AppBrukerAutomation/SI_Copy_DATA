import os.path
from shutil import copytree, make_archive, copy2
from tkinter import Tk, END, Label, Listbox, Button, messagebox
from tkinter.filedialog import askdirectory, asksaveasfilename, askopenfilename
from datetime import datetime

window = Tk()
window.title('App Autimation - SI BackUp Data - V2')
width_win = 600
height_win = 500
# מיקום במרכז המסך לפי הקורדינטות
x_cor = (window.winfo_screenwidth() / 2) - (width_win / 2)
y_cor = (window.winfo_screenheight() / 2) - (height_win / 2)
window.geometry(f"{width_win}x{height_win}+{int(x_cor)}+{int(y_cor) - 20}")
window.resizable(False, False)

def default_path():
    # לוודא אם התיקיות קיימות
    all_paths = ["D:/Spectra",
             "D:/LTparam",
             "D:/Fabware/MimFiles",
             "D:/Fabware/MimFiles_",
             "D:/Fabware/Configurations",
             "D:/Logs/AllErrors",
             "D:/Logs/MaintenanceScheduler",
             "D:/Logs/Throughput",
             "D:/Logs/Tools"]
    paths = []
    for i in all_paths:
        if os.path.exists(i):
            paths.append(i)
    for i in paths:
        list_folders.insert(END, i)

def add_folder_click():
    folder = askdirectory()
    if folder == "" or folder in list_folders.get(0, END):
        return
    list_folders.insert(END, folder)

def add_file_click():
    file_path = askopenfilename()
    if file_path == "" or file_path in list_folders.get(0, END):
        return
    list_folders.insert(END, file_path)


def remove_click():
    try:
        list_folders.delete(list_folders.get(0, END).index(list_folders.selection_get()))
    except:
        return

def copy_click():
    # להוסיף הודעת הצלחה או שגיאה בסוף הגיבוי
    # להשאיר רק ZIP בסוף
    # try:
    if len(list_folders.get(0, END)) < 1:
        return
    folder_name = asksaveasfilename(title="Select a location and the name of the destination folder", initialfile=f"SI_BackUp_{datetime.today().date()}")
    if folder_name == "":
        return
    os.makedirs(folder_name)
    for i in list_folders.get(0, END):
        if os.path.exists(i):
            try:
                copytree(i, f"{folder_name}/{os.path.basename(i)}")
            except:
                copy2(i, folder_name)
    make_archive(folder_name, 'zip', folder_name)
    messagebox.showinfo("SI BackUp", "The backup was performed successfully")
    exit()
    # except:
    #     messagebox.showerror("Error BackUp!", "An error occurred during the backup operation. Please try again, and if the error recurs - contact the application team.")

title = Label(window, text="Please select the folders you wish to back up", font="ariel 18")
title.place(relx=0.5, rely=0.08, anchor='center')

add_folder = Button(window, text="Add Folder", font="ariel 16", width = 9, command=add_folder_click)
add_folder.place(relx=0.18, rely=0.2, anchor='center')

add_file = Button(window, text="Add File", font="ariel 16", width = 9, command=add_file_click)
add_file.place(relx=0.39, rely=0.2, anchor='center')

remove = Button(window, text="Remove", font="ariel 16", width = 9, command=remove_click)
remove.place(relx=0.61, rely=0.2, anchor='center')

copy_btn = Button(window, text="Save As", font="ariel 16", width = 9, command=copy_click)
copy_btn.place(relx=0.82, rely=0.2, anchor='center')

list_folders = Listbox(window, width=55, height=17, font="ariel 12")
list_folders.place(relx=0.5, rely=0.6, anchor='center')

default_path()

window.mainloop()
# test1