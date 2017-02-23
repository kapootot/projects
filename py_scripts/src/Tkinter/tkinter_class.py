from Tkinter import *

class Buttons:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text="Print!", command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="Quit!", command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print("HELLO")


root = Tk()

b = Buttons(root)

root.mainloop()