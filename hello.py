from cmu_graphics import *

import pyaudio

import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv




def onAppStart(app):
    app.size = 10
    app.stepsPerSecond = 10
    app.x = 4
    app.y = 20

def onMouseMove(app, mouseX, mouseY):
    app.x = mouseX

def onStep(app):
    if app.size >= 60:
        app.size = 10
        
        app.y = 0
    else:
        app.size += 1
        
        app.y += 1

def redrawAll(app):
    drawRect(app.x, app.y, app.size, app.size)

def main():
    runApp()

main()

cmu_graphics.run