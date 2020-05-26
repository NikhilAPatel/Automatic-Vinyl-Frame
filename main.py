#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import re
import time
import queue as q
import vlc

MUSIC_PATH = "/home/pi/Desktop/Music/"

reader = SimpleMFRC522()

currentCommand = ""
play = True
queue = q.MusicQueue()
p = vlc.MediaPlayer("")


while True:
    try:
        
        newCommand = re.sub("[^a-z0-9]+","",reader.read()[1],flags = re.IGNORECASE)

        if(newCommand=="PAUSE"):
                play= not play
                if(play):
                    try:
                        p.set_pause(False)
                    except:
                        print("Player Has Not Yet Been Created")
                    time.sleep(1)
                if(not play):
                    try:
                        p.set_pause(True)
                    except:
                        print("Player Has Not Yet Been Created")
                    time.sleep(1)
    
        elif(currentCommand != newCommand):
            p.stop()
            currentCommand=newCommand
            queue.clearQueue()
            
            try:
                queue.generateAlbumQueue(MUSIC_PATH + currentCommand)
            except StopIteration:
                print("Invalid Path")
            try:
                p= vlc.MediaPlayer("file://"+queue.getNextSong())
                p.play()
            except:
                print("Something went wrong!")
                
    finally:
        GPIO.cleanup()
