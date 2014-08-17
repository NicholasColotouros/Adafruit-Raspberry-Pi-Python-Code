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
showNumbers   = True  # Indicates whether numbers or symbols should be shown
input         = ""    # The currently input expression
cursorLocation= 0     
delayTime = 1         # The time it takes to look for another button press


"""
Updates the display based on the global variables.

MenuChanged signals a change from numbers to symbols or vice versa.
"""
def update(menuChanged):
    lcd.clear()
    if showNumbers:
        lcd.message(input+"\n"+numbers)
    else:
        lcd.message(input+"\n"+symbols)

    if menuChanged:
        lcd.setCursor(0,1)
    else:
        lcd.setCursor(cursorLocation,1)


# Startup
lcd.blink()
update(False)


#Polls for input, sleep for 2 seconds after every press to ensure only 1 action per press
while True:
    # Move left
    if lcd.buttonPressed(lcd.LEFT):
        if cursorLocation > 0:
            cursorLocation = cursorLocation - 1
            lcd.setCursor(cursorLocation, 1)
        sleep(delayTime)
         
    # Move right
    elif lcd.buttonPressed(lcd.RIGHT):
        if showNumbers:
            if cursorLocation + 1 < len(numbers):
                cursorLocation += 1
                lcd.setCursor(cursorLocation, 1)

        elif cursorLocation + 1 < len(symbols):
            cursorLocation += 1
            lcd.setCursor(cursorLocation, 1)
        sleep(delayTime)

    # Toggle display
    elif lcd.buttonPressed(lcd.UP):
        showNumbers = not showNumbers
        update(True)
