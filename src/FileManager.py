import shutil
import os

from src import ConfigManager as cm

file = open("config.json", "w")

print(cm.getDestination())
cm.setDestination(["butt plugs", "anal beads", 'dildos'])
print(cm.getDestination())

os.chdir(cm.SRC_LOCATION)

print(os.getcwd())

shutil.copy("test.txt", os.getcwd() + "\\test")