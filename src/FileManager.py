import shutil
import os
import glob
from src import ConfigManager as cm
from tkinter.filedialog import askdirectory

# function to search in folder for files ending in set "filetypes" (sub function)
# function to copy files to backup (sub function)

class BackupFromLocation():
    def __init__(self, location):
        self.location = location

    def copyToBackup(self, file):
        os.chdir(self.location)
        for directory in cm.getDestination():
            shutil.copy(file, directory)

    def listAllFiles(self):
        files = []

        os.chdir(self.location)
        for filetype in cm.getFileTypes():
            files += glob.glob("*" + filetype)

        return files

    def backupFromLocation(self):
        for file in self.listAllFiles():
            self.copyToBackup(file)

for location in cm.getLoctations():
    backup = BackupFromLocation(location)
    backup.backupFromLocation()