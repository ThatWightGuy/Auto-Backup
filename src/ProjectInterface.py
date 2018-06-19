import tkinter as tk
import os
import time
import ConfigManager as cm
import FileManager as fm
from tkinter.filedialog import askdirectory

runBackup = False

# Window Configurations
window = tk.Tk()
window.resizable(width=False, height=False)
window.iconbitmap("images/dunce.ico")
window.title("Auto Backup")
window.geometry("415x370")

# functions/classes
def writeToLog(message):
    logtext.config(state="normal")
    logtext.insert(tk.INSERT, message + "\n")
    logtext.see(tk.END)
    logtext.config(state="disabled")

def addBackupLocation():
    location = str(askdirectory())

    writeToLog("New Location Added:")
    writeToLog(location + "\n")

    cm.setLocations(location)
    os.chdir(cm.SRC_LOCATION)

def addBackupDestination():
    destination = str(askdirectory())

    writeToLog("New Destination Added:")
    writeToLog(destination + "\n")

    cm.setDestination(destination)
    os.chdir(cm.SRC_LOCATION)

class fileTypes():
    def __init__(self):
        self.typeWindow = tk.Toplevel(window)
        self.typeWindow.resizable(width=False, height=False)
        self.typeWindow.geometry("300x62")
        self.typeWindow.title("Set File Types")
        self.typeLabel = tk.Label(self.typeWindow, text="EX: .jpg,.png,.txt (separate by , without space)")
        self.typeLabel.pack()
        self.typeEntry = tk.Entry(self.typeWindow, width=50, justify=tk.CENTER)
        self.typeEntry.insert(tk.END, ",".join(cm.getFileTypes()))
        self.typeEntry.pack()
        self.typeButton = tk.Button(self.typeWindow, text="Apply", bd=0, command=self.destroy)
        self.typeButton.pack()

    def destroy(self):
        writeToLog("File Types to be Backed Up:")
        writeToLog(', '.join(self.typeEntry.get().split(',')) + "\n")

        cm.setFileTypes(self.typeEntry.get())

        os.chdir(cm.SRC_LOCATION)
        self.typeWindow.destroy()

def setFileTypes():
    fileTypes()

class interval():
    def __init__(self):
        self.intervalWindow = tk.Toplevel(window)
        self.intervalWindow.resizable(width=False, height=False)
        self.intervalWindow.geometry("300x62")
        self.intervalWindow.title("Set Frequency Of Backup")
        self.intervalLabel = tk.Label(self.intervalWindow, text="Insert Interval (in minutes, no decimals)")
        self.intervalLabel.pack()
        self.intervalEntry = tk.Entry(self.intervalWindow, width=50, justify=tk.CENTER)
        self.intervalEntry.insert(tk.END, int(cm.getTimeInterval()/60))
        self.intervalEntry.pack()
        self.intervalButton = tk.Button(self.intervalWindow, text="Apply", bd=0, command=self.destroy)
        self.intervalButton.pack()

    def destroy(self):
        writeToLog("New Interval: " + self.intervalEntry.get() + " minute(s)\n")

        cm.setTimeInterval(self.intervalEntry.get())

        os.chdir(cm.SRC_LOCATION)
        self.intervalWindow.destroy()

def setInterval():
    interval()

class EditLocation:
    def __init__(self):
        self.locationWindow = tk.Toplevel(window)
        self.locationWindow.resizable(width=False, height=False)
        self.locationWindow.geometry("300x62")
        self.locationWindow.title("Edit Backup Locations")
        self.locationLabel = tk.Label(self.locationWindow, text="Manually Add/Delete Backup Locations")
        self.locationLabel.pack()
        self.locationEntry = tk.Entry(self.locationWindow, width=50, justify=tk.CENTER)
        self.locationEntry.insert(tk.END, ','.join(cm.getLoctations()))
        self.locationEntry.pack()
        self.locationButton = tk.Button(self.locationWindow, text="Apply", bd=0, command=self.destroy)
        self.locationButton.pack()

    def destroy(self):
        writeToLog("Locations Set:")

        if self.locationEntry.get() != '':
            writeToLog(', '.join(self.locationEntry.get().split(',')) + '\n')
        else:
            writeToLog("None\n")

        cm.editLocaions(self.locationEntry.get().split(','))

        os.chdir(cm.SRC_LOCATION)
        self.locationWindow.destroy()

def locationEdit():
    EditLocation()

class EditDestination:
    def __init__(self):
        self.destinationWindow = tk.Toplevel(window)
        self.destinationWindow.resizable(width=False, height=False)
        self.destinationWindow.geometry("300x62")
        self.destinationWindow.title("Edit Backup Destinations")
        self.destinationLabel = tk.Label(self.destinationWindow, text="Manually Add/Delete Backup Destinations")
        self.destinationLabel.pack()
        self.destinationEntry = tk.Entry(self.destinationWindow, width=50, justify=tk.CENTER)
        self.destinationEntry.insert(tk.END, ','.join(cm.getDestination()))
        self.destinationEntry.pack()
        self.destinationButton = tk.Button(self.destinationWindow, text="Apply", bd=0, command=self.destroy)
        self.destinationButton.pack()

    def destroy(self):
        writeToLog("Locations Set:")

        if self.destinationEntry.get() != '':
            writeToLog(', '.join(self.destinationEntry.get().split(',')) + '\n')
        else:
            writeToLog("None\n")

        cm.editDestinations(self.destinationEntry.get().split(','))

        os.chdir(cm.SRC_LOCATION)
        self.destinationWindow.destroy()

def destinationEdit():
    EditDestination()

def saveLog():
    logtext.config(state="normal")
    os.chdir(cm.CONFIG_LOCATION + "/logs")

    with open('log-' + str(int(time.time())) + ".txt", 'w') as log:
        log.write(logtext.get('1.0',tk.END))

    os.chdir(cm.SRC_LOCATION)
    logtext.config(state="disabled")

def clearLog():
    logtext.config(state="normal")
    logtext.delete('1.0', tk.END)
    logtext.config(state="disabled")

def run():
    writeToLog("Starting Backup...")
    totalFiles = 0

    for location in cm.getLoctations():
        backup = fm.BackupFromLocation(location)
        backup.backupFromLocation()
        writeToLog("Backing up " + str(backup.getNumFiles()) + " files from: " + location)
        totalFiles += backup.getNumFiles()

    writeToLog(str(totalFiles) + " Files Located In: \n" + '\n'.join(cm.getDestination()))
    writeToLog("Backup Finished")

def runPerSetInterval():
    if runBackup:
        run()
        writeToLog("---- Last back up at: " + time.ctime(time.time()) + " ----\n")
        window.after(1000*cm.getTimeInterval(), runPerSetInterval)

def startBackup():
    menubar.entryconfig("Options", state="disabled")
    menubar.entryconfig("Log", state="disabled")
    global runBackup
    runBackup = True
    startbutton.config(state="disabled")
    stopbutton.config(state="normal")
    runPerSetInterval()

def quitBackup():
    menubar.entryconfig("Options", state="normal")
    menubar.entryconfig("Log", state="normal")
    global runBackup
    runBackup = False
    startbutton.config(state="normal")
    stopbutton.config(state="disabled")
    writeToLog("Stopped. Please Wait for Running Processes (if any)\n")


# Log Window
logtext = tk.Text(window, height=20, bg="black", fg="green")
logtext.config(state="disabled")
logtext.pack()

# Menu
menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
logmenu = tk.Menu(menubar,  tearoff=0)

# File Menu
filemenu.add_command(label="Add Backup Location...", command=addBackupLocation)
filemenu.add_command(label="Add Backup Destination...", command=addBackupDestination)
filemenu.add_command(label="Set File Types...", command=setFileTypes)
filemenu.add_command(label="Set Frequency Of Backup...", command=setInterval)
filemenu.add_separator()
filemenu.add_command(label="Edit Backup Locations...", command=locationEdit)
filemenu.add_command(label="Edit Backup Destinations...", command=destinationEdit)
menubar.add_cascade(label="Options", menu=filemenu)

# Log Menu
logmenu.add_command(label="Save Log", command=saveLog)
logmenu.add_command(label="Clear Log", command=clearLog)
menubar.add_cascade(label="Log", menu=logmenu)

# Start/Stop Buttons
buttonframe = tk.Frame(window)
buttonframe.pack()
startbutton = tk.Button(buttonframe, text="Start Backup", bd=0, fg="green", activeforeground="green", command=startBackup)
startbutton.pack(side=tk.LEFT, padx=2, pady=2)
stopbutton = tk.Button(buttonframe, text="Stop Backup", bd=0, fg="red", activeforeground="red", command=quitBackup)
stopbutton.config(state="disabled")
stopbutton.pack(side=tk.LEFT, padx=2, pady=2)

window.config(menu=menubar)
window.mainloop()