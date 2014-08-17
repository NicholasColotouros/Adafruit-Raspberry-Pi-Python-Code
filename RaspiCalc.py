#!/usr/bin/python

from time import sleep
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate

#Initialization of the plate
lcd = Adafruit_CharLCDPlate.Adafruit_CharLCDPlate()
lcd.begin(16,2)
lcd.clear()
lcd.message("  Introducing\n   RaspiCalc")
sleep(1)
lcd.clear()

#Supported numbers and operations
numbers = "0123456789."
symbols = "+-*/()="

#Global information for easy updating
buttonPressed = False #ensures one press only does one action
showNumbers   = True  #Indicates whether numbers or symbols should be shown
input         = ""    #the currently input expression
cursorLocation= 0



"""
Updates the display based on the global variables.

MenuChanged signals a change from numbers to symbols or vice versa.
"""
def update(menuChanged):
    lcd.clear()
    if showNumers:
        lcd.message(input+"\n"+numbers)
    else:
        lcd.message(input+"\n"+symbols)

    if menuChanged:
        lcd.setCursor(1,0)
    else:
        lcd.setCursor(1, cursorLocation)
