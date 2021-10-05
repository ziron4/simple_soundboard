from time import sleep
import keyboard
from playsound import playsound
from os import listdir
from os.path import isfile, join

folderPath = "sounds"
lastPlayedSound = ""
filesInFolder = [f for f in listdir(folderPath) if isfile(join(folderPath, f))]

def keyboard_eventhandler(key):
    if key.event_type != "down":
        return
    
    for filename in filesInFolder:
        if filename.startswith(key.name):
            lastPlayedSound = folderPath + "/" + filename
            playsound(lastPlayedSound, True)


keyboard.hook(keyboard_eventhandler)

while True:
    filesInFolder = [f for f in listdir(folderPath) if isfile(join(folderPath, f))]
