from tkinter import *
from gpiozero import LED
import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

LED = LED(17)

screen = Tk()
screen.title("Morse Coder")  

def blinkMorsecode(Input):

    for letter in Input:
        if (letter == 'a'):
            dot()
            dash()

        elif (letter == 'b'):
            dash()
            dot()
            dot()
            dot()

        elif (letter == 'c'):
            dash()
            dot()
            dash()
            dot()

        elif (letter == 'd'):
            dash()
            dot()
            dot()

        elif (letter == 'e'):
            dot()

        elif (letter == 'f'):
            dot()
            dot()
            dash()
            dot()

        elif (letter == 'g'):
            dash()
            dash()
            dot()

        elif (letter == 'h'):
            dot()
            dot()
            dot()
            dot()

        elif (letter == 'i'):
            dot()
            dot()

        elif (letter == 'j'):
            dot()
            dash()
            dash()
            dash()

        elif (letter == 'k'):
            dash()
            dot()
            dash()

        elif (letter == 'l'):
            dot()
            dash()
            dot()
            dot()

        elif (letter == 'm'):
            dash()
            dash()

        elif (letter == 'n'):
            dash()
            dot()

        elif (letter == 'o'):
            dash()
            dash()
            dash()

        elif (letter == 'p'):
            dot()
            dash()
            dash()
            dot()

        elif (letter == 'q'):
            dash()
            dash()
            dot()
            dash()

        elif (letter == 'r'):
            dot()
            dash()
            dot()

        elif (letter == 's'):
            dot()
            dot()
            dot()

        elif (letter == 't'):
            dash()

        elif (letter == 'u'):
            dot()
            dot()
            dash()

        elif (letter == 'v'):
            dot()
            dot()
            dot()
            dash()

        elif (letter == 'w'):
            dot()
            dash()
            dash()

        elif (letter == 'x'):
            dash()
            dot()
            dot()
            dash()

        elif (letter == 'y'):
            dash()
            dot()
            dash()
            dash()

        elif (letter == 'z'):
            dash()
            dash()
            dot()
            dot()
            
def dot():
    LED.on()
    time.sleep(0.3)
    LED.off()
    time.sleep(0.5)    

def dash():
    LED.on()
    time.sleep(0.9)
    LED.off()
    time.sleep(0.5)    

def enter():
    input = text_box.get("1.0", "end-1c")
    blinkMorsecode(input)
    
text_box = Text(screen, height=2, width=24, bg="yellow")
text_box.grid(row=1, column=1, padx=16, pady=12)

enter = Button(screen, text="Enter", command=enter, bg='light blue', height=2, width=12)
enter.grid(row=2, column=1, padx=12, pady=6)

screen.mainloop()
