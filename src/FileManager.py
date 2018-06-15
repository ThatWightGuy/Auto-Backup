import shutil
import os
import glob
import ConfigManager as cm
import time


# function to search in folder for files ending in set "filetypes" (sub function)
# function to copy files to backup (sub function)

class BackupFromLocation():
    def __init__(self, location):
        self.location = location

    def copyToBackup(self, file):
        print("copyToBackup")
        for directory in cm.getDestination():
            os.chdir(self.location)
            shutil.copy(file, directory)

    def listAllFiles(self):
        print("listAllFiles")
        files = []
        print(self.location)
        print(cm.getFileTypes())
        for filetype in cm.getFileTypes():
            print(os.getcwd())
            os.chdir(self.location)
            files += glob.glob("*" + filetype)
        print(files)

        return files

    def backupFromLocation(self):
        print("backupFromLocation")
        for file in self.listAllFiles():
            self.copyToBackup(file)

def runPerSetInterval():
    while True:
        for location in cm.getLoctations():
            backup = BackupFromLocation(location)
            backup.backupFromLocation()
        print("files backed up")
        time.sleep(cm.getTimeInterval())