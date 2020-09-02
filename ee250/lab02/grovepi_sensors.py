""" EE 250L Lab 02: GrovePi Sensors

List team members here.

Insert Github repository link here.
"""

"""python3 interpreters in Ubuntu (and other linux distros) will look in a 
default set of directories for modules when a program tries to `import` one. 
Examples of some default directories are (but not limited to):
  /usr/lib/python3.5
  /usr/local/lib/python3.5/dist-packages

The `sys` module, however, is a builtin that is written in and compiled in C for
performance. Because of this, you will not find this in the default directories.
"""
import sys
import time
# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `import grovepi`
sys.path.append('../../Software/Python/')
# This append is to support importing the LCD library.
sys.path.append('../../Software/Python/grove_rgb_lcd')

from grovepi import * 
import grovepi
from grove_rgb_lcd import *

if sys.platform == 'uwp':
    import winrt_smbus as smbus
    bus = smbus.SMBus(1)
else:
    import smbus
    import RPi.GPIO as GPIO
    rev = GPIO.RPI_REVISION
    if rev == 2 or rev == 3:
        bus = smbus.SMBus(1)
    else:
        bus = smbus.SMBus(0)
 
# this device has two I2C addresses
DISPLAY_RGB_ADDR = 0x62
DISPLAY_TEXT_ADDR = 0x3e




"""This if-statement checks if you are running this python file directly. That 
is, if you run `python3 grovepi_sensors.py` in terminal, this if-statement will 
be true"""
if __name__ == '__main__':
	PORT = 4
	potentiometer = 0
	grovepi.pinMode(potentiometer,"INPUT")
	time.sleep(1)
	c = 0
	setText("")
	while True:
		#So we do not poll the sensors too quickly which may introduce noise,
		#sleep for a reasonable time of 200ms between each iteration.
		time.sleep(0.2)
		sensor_value = grovepi.analogRead(potentiometer)%517
		print("sensor value ", sensor_value)
		setRGB(255-c,255,255-c)
		c+=7
		if c == 255:
			c = 0
		read = grovepi.ultrasonicRead(PORT)
		print(read)
		textLn1 = str(sensor_value) + "cm"
		if (read < sensor_value ):
			textLn1 += " OBJ PRES"
		else:
			textLn1+="           "
		textLn2 = "\n" + str(read) + "cm"
		setText_norefresh(textLn1 + textLn2)


