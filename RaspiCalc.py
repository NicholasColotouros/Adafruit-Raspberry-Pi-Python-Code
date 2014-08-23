#!/usr/bin/python

from time import sleep
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate

#Initialization of the plate
lcd = Adafruit_CharLCDPlate.Adafruit_CharLCDPlate()
lcd.begin(16,2)
lcd.clear()
lcd.message("  Introducing\n   RaspiCalc")
sleep(2)
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
def update():
    lcd.clear()
    if showNumbers:
        lcd.message(input+"\n"+numbers)
    else:
        lcd.message(input+"\n"+symbols)

    lcd.setCursor(cursorLocation,1)

"""
Sends an error message to the display then updates the screen
"""
def errorMessage(errMessage):
    lcd.blink()
    lcd.clear()
    lcd.message(errMessage)
    sleep(4)
    update()

# Startup
lcd.blink()
update()


#Polls for input, sleep for 2 seconds after every press to ensure only 1 action per press
while True:
    # Move left
    if lcd.buttonPressed(lcd.LEFT):
        if cursorLocation > 0:
            cursorLocation -= 1
            lcd.setCursor(cursorLocation, 1)

            sleep(delayTime)

        # Move to the end if going left
        else:
            if showNumbers:
                cursorLocation = len(numbers) - 1
            else:
                cursorLocation = len(symbols) - 1

            lcd.setCursor(cursorLocation, 1)

         
    # Move right
    elif lcd.buttonPressed(lcd.RIGHT):
        if showNumbers:
            if cursorLocation + 1 < len(numbers):
                cursorLocation += 1
                lcd.setCursor(cursorLocation, 1)
            else: #else wrap around to the start
                cursorLocation = 0
                lcd.setCursor(cursorLocation, 1)
                
        elif cursorLocation + 1 < len(symbols):
            cursorLocation += 1
            lcd.setCursor(cursorLocation, 1)

        else: #wrap around to the start
            cursorLocation = 0
            lcd.setCursor(cursorLocation, 1)

        sleep(delayTime)

    # Toggle display
    elif lcd.buttonPressed(lcd.UP):
        showNumbers = not showNumbers
        cursorLocation = 0
        update()
        sleep(delayTime)

    # Delete last entry
    elif lcd.buttonPressed(lcd.DOWN):
        input = input[:-1]
        update()
        sleep(delayTime)

    # Select the current entry
    elif lcd.buttonPressed(lcd.SELECT):

        # If = was selected, evaluate
        if not showNumbers and symbols[cursorLocation] == '=':
            try:
                result = eval(input)
                result = str(result)

                # If the result can't fit in the screen, overflow error
                if int(result) >= 10^16:
                    errorMessage("Overflow Error")
                else:
                    input = result
                    update()

            except SyntaxError:
                errorMessage("Invalid Syntax")
                print input

        # Something else was selected
        else:
            if showNumbers:
                input = input + numbers[cursorLocation]
            else:
                input = input + symbols[cursorLocation]
            update()
        sleep(delayTime)    
