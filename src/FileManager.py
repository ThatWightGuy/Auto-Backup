import shutil
import os
import glob
import ConfigManager as cm

class BackupFromLocation():
    def __init__(self, location):
        self.location = location
        self.numFiles = 0

    def getNumFiles(self):
        return self.numFiles

    def copyToBackup(self, file):
        for directory in cm.getDestination():
            os.chdir(self.location)
            shutil.copy(file, directory)

    def listAllFiles(self):
        files = []

        for filetype in cm.getFileTypes():
            os.chdir(self.location)
            files += glob.glob("*" + filetype)

        self.numFiles = len(files)

        return files

    def backupFromLocation(self):
        for file in self.listAllFiles():
            self.copyToBackup(file)

