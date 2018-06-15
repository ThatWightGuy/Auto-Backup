import tkinter as tk
import os
import ConfigManager as cm
from tkinter.filedialog import askdirectory

# Window Configurations
window = tk.Tk()
window.resizable(width=False, height=False)
window.iconbitmap("images/dunce.ico")
window.title("Auto Backup")
window.geometry("400x370")

# functions/classes
def addBackupLocation():
    location = str(askdirectory())
    cm.setLocations(location)
    os.chdir(cm.SRC_LOCATION)

def addBackupDestination():
    destination = str(askdirectory())
    cm.setDestination(destination)
    os.chdir(cm.SRC_LOCATION)

# TODO: This will need to be a class to allow for destroy function (same will apply for frequency of backup)
def setFileTypes():
    typeWindow = tk.Toplevel(window)
    typeWindow.resizable(width=False, height=False)
    typeWindow.geometry("300x62")
    typeWindow.title("Set File Types")
    typeLabel = tk.Label(typeWindow, text="EX: .jpg,.png,.txt (separate by , without space)")
    typeLabel.pack()
    typeEntry = tk.Entry(typeWindow, width=50, justify=tk.CENTER)
    typeEntry.insert(tk.END, ",".join(cm.getFileTypes()))
    typeEntry.pack()
    typeButton = tk.Button(typeWindow, text="Apply", bd=0)
    typeButton.pack()

# Menu
menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)

filemenu.add_command(label="Add Backup Location...", command=addBackupLocation)
filemenu.add_command(label="Add Backup Destination...", command=addBackupDestination)
filemenu.add_command(label="Set File Types...", command=setFileTypes)
filemenu.add_command(label="Set Frequency Of Backup")
menubar.add_cascade(label="Options", menu=filemenu)

# Log Window
logtext = tk.Text(window, height=20)
logtext.pack()

# Start/Stop Buttons
buttonframe = tk.Frame(window)
buttonframe.pack()
startbutton = tk.Button(buttonframe, text="Start Backup", bd=0, fg="green", activeforeground="green")
startbutton.pack(side=tk.LEFT, padx=2, pady=2)
stopbutton = tk.Button(buttonframe, text="Stop Backup", bd=0, fg="red", activeforeground="red")
stopbutton.pack(side=tk.LEFT, padx=2, pady=2)

window.config(menu=menubar)
window.mainloop()