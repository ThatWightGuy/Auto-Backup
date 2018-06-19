# Parses and manages the config.ini file.
import os
import configparser

SRC_LOCATION = os.getcwd()
CONFIG_LOCATION = os.path.join(os.getcwd(), os.pardir)

config = configparser.ConfigParser()

os.chdir(CONFIG_LOCATION)
config.read("config.ini")
os.chdir(SRC_LOCATION)

def writeToConfig():
    os.chdir(CONFIG_LOCATION)
    with open("config.ini", 'w') as configfile:
        config.write(configfile)
    os.chdir(SRC_LOCATION)

def getDestination():
    os.chdir(CONFIG_LOCATION)
    destinations = list()

    if config["Directories"]["destinations"] != '':
        destinations = config["Directories"]["destinations"].split(',')

    return destinations

def getLoctations():
    os.chdir(CONFIG_LOCATION)
    locations = list()

    if config["Directories"]["locations"] != '':
        locations = config["Directories"]["locations"].split(',')

    return locations

def getFileTypes():
    os.chdir(CONFIG_LOCATION)
    fileTypes = list()

    if config["FileTypes"]["filetypes"] != '':
        fileTypes = config["FileTypes"]["filetypes"].split(',')

    return fileTypes

def getTimeInterval():
    return 60*int(config["Execution"]["runtimeinterval"])

def setDestination(destination):
    curDestinations = getDestination()
    curDestinations.append(destination)
    config["Directories"]["destinations"] = ",".join(curDestinations)

    writeToConfig()

def setLocations(location):
    curLocations = getLoctations()
    curLocations.append(location)
    config["Directories"]["locations"] = ",".join(curLocations)

    writeToConfig()

def editDestinations(destinations):
    if destinations != "":
        config["Directories"]["destinations"] = ",".join(destinations)
    else:
        config["Directories"]["destinations"] = destinations
    writeToConfig()

def editLocaions(locations):
    if locations != "":
        config["Directories"]["locations"] = ",".join(locations)
    else:
        config["Directories"]["locations"] = locations

    writeToConfig()

def setFileTypes(filetypes):
    config["FileTypes"]["filetypes"] = filetypes
    writeToConfig()

def setTimeInterval(interval):
    config["Execution"]["runtimeinterval"] = str(interval)
    writeToConfig()