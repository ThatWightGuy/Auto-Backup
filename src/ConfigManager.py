# Parses and manages the config.ini file. Not to be confused with ConfigMenu (to be implemented later)
import os
import configparser

SRC_LOCATION = os.getcwd()
CONFIG_LOCATION = os.path.join(os.getcwd(), os.pardir)

config = configparser.ConfigParser()

os.chdir(CONFIG_LOCATION)
config.read("config.ini")

def getDestination():
    return list(config["Directories"]["destination"].split(','))

def getLoctations():
    return list(config["Directories"]["locations"].split(','))

def getFileTypes():
    return list(config["FileTypes"]["filetypes"].split(','))

def setDestination(destination):
    config["Directories"]["destination"] = ",".join(destination)

    os.chdir(CONFIG_LOCATION)
    with open("config.ini", 'w') as configfile:
        config.write(configfile)

def setLocations(locations):
    config["Directories"]["destination"] = ",".join(locations)

    os.chdir(CONFIG_LOCATION)
    with open("config.ini", 'w') as configfile:
        config.write(configfile)

def setFileTypes(filetypes):
    config["FileTypes"]["filetypes"] = ",".join(filetypes)

    os.chdir(CONFIG_LOCATION)
    with open("config.ini", 'w') as configfile:
        config.write(configfile)