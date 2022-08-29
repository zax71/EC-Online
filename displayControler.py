from machine import Pin
import time

display0 = Pin(0, Pin.OUT)
display1 = Pin(1, Pin.OUT)
display2 = Pin(2, Pin.OUT)
display3 = Pin(3, Pin.OUT)
display4 = Pin(4, Pin.OUT)
display5 = Pin(5, Pin.OUT)
display6 = Pin(6, Pin.OUT)
display7 = Pin(7, Pin.OUT)
display8 = Pin(8, Pin.OUT)
display9 = Pin(9, Pin.OUT)

def displaySetHigh(num):
    if num == 0:
        display0.high()
    elif num == 1:
        display1.high()
    elif num == 2:
        display2.high()
    elif num == 3:
        display3.high()
    elif num == 4:
        display4.high()
    elif num == 5:
        display5.high()
    elif num == 6:
        display6.high()
    elif num == 7:
        display7.high()
    elif num == 8:
        display8.high()
    elif num == 9:
        display9.high()

def displaySetLow(num):
    if num == 0:
        display0.low()
    elif num == 1:
        display1.low()
    elif num == 2:
        display2.low()
    elif num == 3:
        display3.low()
    elif num == 4:
        display4.low()
    elif num == 5:
        display5.low()
    elif num == 6:
        display6.low()
    elif num == 7:
        display7.low()
    elif num == 8:
        display8.low()
    elif num == 9:
        display9.low()
    

def clearScreen():
    display0.low()
    display1.low()
    display2.low()
    display3.low()
    display4.low()
    display5.low()
    display6.low()
    display7.low()
    display8.low()
    display9.low()
def displayNum(number):

    clearScreen()
    
    for i in range(0, number):
        print(f"displaying {i}")
        displaySetHigh(i)
