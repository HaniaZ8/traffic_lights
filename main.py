# klasa, żeby włożyć tam okienko to szare/czarne, ona jest zapętlana w nieskończoność, jest odpalane przez guzik
# guzik, żeby zapalać światła, ale po czasie wsn światła są automatyczne, tylko guzik włącza działanie mechanizmu
# klasa z 3 metodami, które zwracają 3 różne informacje, które
# światło się zapala, które nie i to ma się zmieniać w czasie,
# one są w tej pętli pierwszej klasy
# użyj funkcji sleep z pakietu time
# interface graficzny Tkinter

from tkinter import *
import time

box = Tk()
box.geometry("300x400")
canvas = Canvas(width=200, height=300, bg="black")
working = False


def start(can=canvas):
    global working

    if working == False:
        working = True
        while True:
            print('works')
            # e = Functions()
            can.pack(anchor=CENTER, expand=1)

            # THE SLEEP() DOESN'T WORK HERE, also trying get it to work in functions.py
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

    else:
        working = False
        print("doesn't work")
        g_red = can.create_oval(60, 20, 140, 100, outline='#808080', fill='#808080')
        g_yellow = can.create_oval(60, 110, 140, 190, outline='#808080', fill='#808080')
        g_green = can.create_oval(60, 200, 140, 280, outline='#808080', fill='#808080')


class Functions:  # Trying get it to work in functions.py
    can = canvas

    def __init__(self):
        super().__init__()
        self.red_light_on()
        self.yellow_light_on()
        self.green_light_on()
        self.green_light_off()
        self.yellow_light_off()
        self.green_light_off()

    def red_light_on(self):
        for i in range(1):
            time.sleep(0.5)
            Functions.can.create_oval(60, 20, 140, 100, outline="#ff0000", fill="#ff0000")

    def yellow_light_on(self):
        time.sleep(1)
        Functions.can.create_oval(60, 110, 140, 190, outline="#ffff00", fill="#ffff00")

    def green_light_on(self):
        time.sleep(1)
        Functions.can.create_oval(60, 20, 140, 100, outline='#808080', fill='#808080')
        Functions.can.create_oval(60, 110, 140, 190, outline='#808080', fill='#808080')
        Functions.can.create_oval(60, 200, 140, 280, outline="#008000", fill="#008000")

    def green_light_off(self):
        time.sleep(1)
        Functions.can.create_oval(60, 200, 140, 280, outline='#808080', fill='#808080')
        Functions.can.create_oval(60, 110, 140, 190, outline="#ffff00", fill="#ffff00")

    def yellow_light_off(self):
        time.sleep(1)
        Functions.can.create_oval(60, 110, 140, 190, outline='#808080', fill='#808080')


class Example(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()
        button = Button(text="START/STOP", width=20, height=3, command=start)
        button.pack(anchor=N, expand=1)

    def initUI(self):
        self.master.title("Traffic Lights")

        canvas.create_oval(60, 200, 140, 280, outline='#808080', fill='#808080')  # these three circles are grey
        canvas.create_oval(60, 110, 140, 190, outline='#808080', fill='#808080')
        canvas.create_oval(60, 20, 140, 100, outline='#808080', fill='#808080')

        # saved positions of red, yellow and green circle
        # red = canvas.create_oval(60, 20, 140, 100,
        #                         outline="#ff0000", fill="#ff0000")
        # yellow = canvas.create_oval(60, 110, 140, 190,
        #                            outline="#ffff00", fill="#ffff00")
        # green = canvas.create_oval(60, 200, 140, 280,
        #                           outline="#008000", fill="#008000")
        canvas.pack(anchor=CENTER, expand=1)


def main():
    ex = Example()
    box.mainloop()


main()
