# klasa, żeby włożyć tam okienko to szare/czarne, ona jest zapętlana w nieskończoność, jest odpalane przez guzik
# guzik, żeby zapalać światła, ale po czasie wsn światła są automatyczne, tylko guzik włącza działanie mechanizmu
# klasa z 3 metodami, które zwracają 3 różne informacje, które
# światło się zapala, które nie i to ma się zmieniać w czasie,
# one są w tej pętli pierwszej klasy
# użyj funkcji sleep z pakietu time
# interface graficzny Tkinter

from tkinter import *

# box = Tk()
# box.geometry("200x300")
# box.title("Traffic lights")
# heading = Label(text="Traffic Lights", bg="black", fg="white", height="200", width="300")
# oval = canvas.create_oval(30, 10, 30, 80, outline="#7f7d78", fill="#7f7d78")
# heading.pack()

box = Tk()
box.geometry("200x300")


class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.master.title("Colours")
        self.pack(expand=1)

        canvas = Canvas(self, width=200, height=300, bg="black")

        red = canvas.create_rectangle(50, 15, 150, 65,
                             outline="#ff0000", fill="#ff0000")
        yellow = canvas.create_rectangle(50, 75, 150, 125,
                                outline="#ffff00", fill="#ffff00")
        green = canvas.create_rectangle(50, 135, 150, 185,
                                outline="#008000", fill="#008000")
        canvas.pack(expand=1)


ex = Example()
heading = Label(text="Traffic Lights", bg="black", fg="white", height="10", width="40")
box.mainloop()
