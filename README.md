RaspiCalc
=========
This is a raspberry pi calculator designed to work with the Adafruit 2 line LCD display with keypad which can be found [here](http://www.adafruit.com/products/1110). Will work with both the positive, negative and multi-colour displays. 

This is a fork of the Adafruit-Raspberry-Pi-Python-Code repository. Included are all of the original files needed to setup the plate. If you haven't done any setup for the LCD plate on your raspberry pi, please see the [tutorial](https://learn.adafruit.com/adafruit-16x2-character-lcd-plus-keypad-for-raspberry-pi).

The top line of the display shows the equation currently being entered or the result of the requested evaluation. The bottom line serves as a menu to select digits or operations (+, -, *, etc).

To run, simply call sudo python RaspiCalc.py

Controls
--------

* The left and right buttons navigate the menu
  * Trying to move beyond the ends of a selection menu will wrap around to the other side
* The up button toggles between digits and operations
* The down button serves as a delete button, which will remove the last selected item
* The select button selects the currently highlighted item
