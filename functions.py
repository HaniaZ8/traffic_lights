from tkinter import *
import time

canvas = Canvas(width=200, height=300, bg="black")
can = canvas
# Function that's supposed to make the lights work aka trying to get the sleep() to work properly. Currently,
# it sums up every second from all the time sleep()s and instead of executing one after another it waits for like 10
# seconds and "does" everything at once (in the result we do not see anything new, in the GUI the button is just
# "clicked" for like 10 secs)

# THE SLEEP() DOESN'T WORK HERE HEEEEEEEEEEEELP
red = can.create_oval(60, 20, 140, 100, outline="#ff0000", fill="#ff0000")
time.sleep(1)
yellow = can.create_oval(60, 110, 140, 190, outline="#ffff00", fill="#ffff00")
time.sleep(1)
time.sleep(2)
g_red = can.create_oval(60, 20, 140, 100, outline='#808080', fill='#808080')
g_yellow = can.create_oval(60, 110, 140, 190, outline='#808080', fill='#808080')
green = can.create_oval(60, 200, 140, 280, outline="#008000", fill="#008000")
time.sleep(5)
g_green = can.create_oval(60, 200, 140, 280, outline='#808080', fill='#808080')
yellow = can.create_oval(60, 110, 140, 190, outline="#ffff00", fill="#ffff00")
time.sleep(2)
g_yellow = can.create_oval(60, 110, 140, 190, outline='#808080', fill='#808080')


class Fun:  # trying while loop from test.py
    can = canvas
    a = True
    b = True
    c = True
    d = True
    e = True

    def __init__(self):
        super().__init__()
        self.red_light_on()
        self.yellow_light_on()
        self.green_light_on()
        self.green_light_off()
        self.yellow_light_off()
        self.green_light_off()

    def red_light_on(self):
        while Fun.a:
            time.sleep(2)
            Fun.can.create_oval(60, 20, 140, 100, outline="#ff0000", fill="#ff0000")
            Fun.a = False

    def yellow_light_on(self):
        while Fun.b:
            time.sleep(2)
            Fun.can.create_oval(60, 110, 140, 190, outline="#ffff00", fill="#ffff00")
            Fun.b = False

    def green_light_on(self):
        while Fun.c:
            time.sleep(2)
            Fun.can.create_oval(60, 20, 140, 100, outline='#808080', fill='#808080')
            Fun.can.create_oval(60, 110, 140, 190, outline='#808080', fill='#808080')
            Fun.can.create_oval(60, 200, 140, 280, outline="#008000", fill="#008000")
            Fun.c = False

    def green_light_off(self):
        while Fun.d:
            time.sleep(2)
            Fun.can.create_oval(60, 200, 140, 280, outline='#808080', fill='#808080')
            Fun.can.create_oval(60, 110, 140, 190, outline="#ffff00", fill="#ffff00")
            Fun.d = False

    def yellow_light_off(self):
        while Fun.e:
            time.sleep(2)
            Fun.can.create_oval(60, 110, 140, 190, outline='#808080', fill='#808080')
            Fun.e = False
