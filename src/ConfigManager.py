# Parses and manages the config.ini file. Not to be confused with ConfigMenu (to be implemented later)
import os
import configparser

SRC_LOCATION = os.getcwd()
CONFIG_LOCATION = os.path.join(os.getcwd(), os.pardir)

config = configparser.ConfigParser()

os.chdir(CONFIG_LOCATION)
config.read("config.ini")

def writeToConfig():
    os.chdir(CONFIG_LOCATION)
    with open("config.ini", 'w') as configfile:
        config.write(configfile)

def getDestination():
    return list(config["Directories"]["destination"].split(','))

def getLoctations():
    return list(config["Directories"]["locations"].split(','))

def getFileTypes():
    return list(config["FileTypes"]["filetypes"].split(','))

def getLastRunTime():
    return int(config["Execution"]["lastruntime"])

def setDestination(destination):
    config["Directories"]["destination"] = ",".join(destination)
    writeToConfig()

def setLocations(locations):
    config["Directories"]["destination"] = ",".join(locations)
    writeToConfig()

def setFileTypes(filetypes):
    config["FileTypes"]["filetypes"] = ",".join(filetypes)
    writeToConfig()