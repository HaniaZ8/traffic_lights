from tkinter import *
import time

"""
So far everything is working fine, I figured out how to put everything in one class (Example) and the changing 
lights mechanism is working (finally). Although I still have to make it work in a loop, make the button unclick and try
to make the mechanism break when user hits STOP
"""


class Example(Frame):

    def __init__(self, parent):  # Here we have determined box for lights mechanism, the button, and variable end
        # (maybe useful for breaking the loop in the future)
        super().__init__()
        self.box = parent
        self.box.geometry("300x400")
        self.frame = Frame(parent)
        self.frame.pack()
        self.canvas = Canvas(width=200, height=300, bg="black")
        self.initUI()
        self.button = Button(text="START", width=20, height=3, command=self.start)
        self.button.pack(anchor=N, expand=1)
        self.can = self.canvas
        self.end = False

    def initUI(self):  # Here everything is the same as it was
        self.master.title("Traffic Lights")

        self.canvas.create_oval(60, 200, 140, 280, outline='#808080', fill='#808080')  # these three circles are grey
        self.canvas.create_oval(60, 110, 140, 190, outline='#808080', fill='#808080')
        self.canvas.create_oval(60, 20, 140, 100, outline='#808080', fill='#808080')

        self.canvas.pack(anchor=CENTER, expand=1)

    def start(self):  # this one initiates the start of lights mechanism (yet to figure out how to make it a loop,
        # and break it)
        self.can.pack(anchor=CENTER, expand=1)
        if self.button['text'] == 'START':
            print("works")
            self.button.config(text="STOP")
            # the whole circles changing colours here
            self.end = True
            self.working()
        else:  # The primary state of the box (grey circles)
            print("doesn't work")
            g_red = self.can.create_oval(60, 20, 140, 100, outline='#808080', fill='#808080')
            g_yellow = self.can.create_oval(60, 110, 140, 190, outline='#808080', fill='#808080')
            g_green = self.can.create_oval(60, 200, 140, 280, outline='#808080', fill='#808080')
            self.button.config(text="START")
            pass

    # Here we start defining every function needed to continue changing of the lights
    def red_light_on(self):
        red = self.can.create_oval(60, 20, 140, 100, outline="#ff0000", fill="#ff0000")
        self.box.after(1000, self.yellow_light_on)

    def yellow_light_on(self):
        yellow = self.can.create_oval(60, 110, 140, 190, outline="#ffff00", fill="#ffff00")
        self.box.after(1000, self.green_light_on)

    def green_light_on(self):

        g_red = self.can.create_oval(60, 20, 140, 100, outline='#808080', fill='#808080')
        g_yellow = self.can.create_oval(60, 110, 140, 190, outline='#808080', fill='#808080')
        green = self.can.create_oval(60, 200, 140, 280, outline="#008000", fill="#008000")
        self.box.after(1000, self.green_light_off)

    def green_light_off(self):
        g_green = self.can.create_oval(60, 200, 140, 280, outline='#808080', fill='#808080')
        yellow = self.can.create_oval(60, 110, 140, 190, outline="#ffff00", fill="#ffff00")
        self.box.after(1000, self.yellow_light_off)

    def yellow_light_off(self):
        g_yellow = self.can.create_oval(60, 110, 140, 190, outline='#808080', fill='#808080')
        self.end = True

    def working(self):  # attempts to loop the mechanism, or eventually to break it
        while True:
            if self.end:
                self.red_light_on()
                self.end = False
            else:
                break


def main():
    box = Tk()
    ex = Example(box)
    box.mainloop()


main()
