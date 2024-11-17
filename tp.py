from cmu_graphics import *

import pyaudio

import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import wavio as wv

duration = 5  # Duration of recording in seconds
samplerate = 44100  # Sampling rate in Hz
app.stepsPerSecond = 1


sd.default.device = (0, None)



def onAppStart(app):
    app.size = 210
    app.color = "cyan"
    app.recording = False
    #app.stepsPerSecond = 10
    app.x = app.width/2-app.size/2
    app.y = app.height/2-app.size/2
    app.audio = None

def onMousePress(app, mouseX, mouseY):
    if app.x <= mouseX <= app.x + app.size and app.y <= mouseY <= app.x + app.size:
        app.recording = True
        # if app.recording == False:
        #     app.color = "red"
        #     app.recording = True  
        # else: 
        #     app.color = "cyan"
        #     app.recording = False
    else:
        sd.play(app.audio, samplerate=samplerate)
        
    

        

# def onMouseMove(app, mouseX, mouseY):
#     app.x = mouseX - app.size/2

def onStep(app):
    if app.recording:
        app.color = "red"
        app.audio = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=1, dtype='float32')
        sd.wait()  # Wait for recording to finish
        app.recording = False
        app.color = "cyan"
        


def redrawAll(app):
    drawLabel("Press Blue Button to Record 5 second Clip", app.width/2, 20, align= "center")
    drawLabel("(Pressing outside button will replay)", app.width/2, 40, align= "center")
    drawRect(app.x, app.y, app.size, app.size, fill = app.color)

def main():
    runApp()

main()

cmu_graphics.run