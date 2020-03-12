"""
controls.py

functions to control physical hardware of 
the moth trap via raspberry pi GPIO

see README.md

pin assignments
---------------
Pin  7 - GPIO4  - Servo PWM
Pin 12 - GPIO18 - Moth LED Control
Pin 15 - GPIO22 - Fan Control
Pin 16 - GPIO23 - Flash LED Control
Pin  ? - GPIO?  - hatch closed limit switch
"""

import RPi.GPIO as GPIO
import time

#GPIO pin assignments (GPIO in BCM mode)
LEDPIN = 18
FANPIN = 22
SERVOPIN = 4
#TODO CLOSEDPIN = 

OPEN_HATCH_TIME = 3 #time to run servo to fully open hatch
RELEASE_TIME	= 4 #time to hold hatch open with fan running


def trap_init():
    #TODO set gpio mode, and configure inputs/outputs
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SERVOPIN,GPIO.OUT)

def trap_release():
    #light off, open hatch, run fan for x seconds, 
    #fan off, close hatch, light on
    light_on(False)
    open_hatch(OPEN_HATCH_TIME)
    fan_on(True)
    time.sleep(4)
    fan_on(False)
    close_hatch()
    light_on(True)



def open_hatch(open_time):    	
    #run the servo to open the hatch for <time> seconds
    p = GPIO.PWM(SERVOPIN, 50) 	# setup for PWM with 50Hz
    p.start(5)
    time.sleep(open_time)
    p.ChangeDutyCycle(7.05)  	#TODO find servo centre pwm 5 should be left, 7.5 centre, 10 right , possibly up to 12.5
    time.sleep(1)
    p.stop


#def close_hatch():
#    TODO run the servo to close the hatch, servo runs until the limit switch is hit 


def light_on(switch_on):  #control the main moth attracting LEDs, True for on, False for off
    GPIO.output(LEDPIN, GPIO.HIGH) if switch_on else GPIO.output(LEDPIN, GPIO.LOW)

def fan_on(switch_on): #control the 12V fan, True to start the fan, False to stop
    GPIO.output(FANPIN, GPIO.HIGH) if switch_on else GPIO.output(FANPIN, GPIO.LOW)


trap_init()
open_hatch(5)
GPIO.cleanup()
