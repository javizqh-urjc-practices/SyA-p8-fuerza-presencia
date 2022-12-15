#!/usr/bin/python
import RPi.GPIO as GPIO
import signal
import sys
from time import sleep

ledPin = 3
ledTTL = 30
lightTTL = 0

fuerzaPin = 7

presenciaPin = 8
presenciaTTL = 30 # in seconds
detectTTL = 0

def callbackSalir(senial, cuadro):
    '''Clear the GPIO pin and exits the program'''
    GPIO.cleanup()
    sys.exit(0)
    
def callbackFuerza(canal):
    # Start the timer
    global detectTTL, presenciaTTL
    detectTTL = presenciaTTL

def callbackPresencia(canal):
    global detectTTL,presenciaTTL, ledTTL, lightTTL
    # Start the timer
    if (detectTTL == 0): return
    lightTTL = ledTTL
    detectTTL = presenciaTTL # Reset detect timer
    GPIO.output(ledPin, GPIO.HIGH) # Turn on light

def main():
    global detectTTL, lightTTL
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(fuerzaPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.setup(presenciaPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.setup(ledPin, GPIO.OUT)

    GPIO.add_event_detect(fuerzaPin, GPIO.RISING,callback=callbackFuerza, bouncetime=5)
    GPIO.add_event_detect(presenciaPin, GPIO.RISING,callback=callbackPresencia, bouncetime=5)

    signal.signal(signal.SIGINT, callbackSalir)

    while True:
        if (detectTTL > 0): detectTTL -= 1
        if (lightTTL > 0): lightTTL -= 1
        if (lightTTL == 0):  GPIO.output(ledPin, GPIO.LOW) # Turn off light
        # Uncomment for debugging
        # print(f'detectTTL = {detectTTL} seconds')
        # print(f'lightTTL = {lightTTL} seconds')
        sleep(1)

    signal.pause()
                  
main()