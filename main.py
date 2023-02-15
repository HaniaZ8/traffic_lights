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
box.geometry("300x400")


class Example(Frame):
    lights_working = False

    def __init__(self):
        super().__init__()
        self.initUI()
        button = Button(text="START", width=20, height=3, command=)
        button.pack(anchor=N, expand=1)

    def initUI(self):
        self.master.title("Traffic Lights")

        canvas = Canvas(width=200, height=300, bg="black")

        red = canvas.create_oval(60, 20, 140, 100,
                                 outline="#ff0000", fill="#ff0000")
        yellow = canvas.create_oval(60, 110, 140, 190,
                                    outline="#ffff00", fill="#ffff00")
        green = canvas.create_oval(60, 200, 140, 280,
                                   outline="#008000", fill="#008000")
        canvas.pack(anchor=CENTER, expand=1)

    def start(self):
        canvas.create_oval(60, 200, 140, 280,
                                               outline="#808080", fill="#808080")


def main():
    ex = Example()
    box.mainloop()


main()
