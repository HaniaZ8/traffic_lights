import from tkinter *

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.master.title("Colours")
        self.pack(fill=BOTH, expand=1)




def main():
    box = Tk()
    box.geometry("200x300")
    ex = Example()
    heading = Label(text="Traffic Lights", bg="black", fg="gray", height="10", width="40")
    box.mainloop()
    heading.pack()


if __name__ == '__main__':
    main()