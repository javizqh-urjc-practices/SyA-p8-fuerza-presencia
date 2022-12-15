#!/usr/bin/python
import RPi.GPIO as GPIO
import signal
import sys

ledPin = 3
ledPinState = True

presenciaPin = 7

def callbackSalir(senial, cuadro):
    '''Clear the GPIO pin and exits the program'''
    GPIO.cleanup()
    sys.exit(0)
    
def callbackPresencia(canal):
    '''Turns the led on or off according to the last state'''
    global ledPinState
    if(ledPinState):
        ledPinState = False
        GPIO.output(ledPin, GPIO.HIGH)
    else:
        ledPinState = True
        GPIO.output(ledPin, GPIO.LOW)
        
def main():
    
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(presenciaPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.add_event_detect(presenciaPin, GPIO.BOTH,callback=callbackPresencia, bouncetime=5)
    signal.signal(signal.SIGINT, callbackSalir)
    signal.pause()
          
main()
