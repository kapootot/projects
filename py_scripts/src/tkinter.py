from Tkinter import *

root = Tk()

# def printName():
#     print "Name"

# topFrame = Frame(root)
# topFrame.pack()
# bottomFrame = Frame(root)
# bottomFrame.pack(side=BOTTOM)
#
# button1 = Button(topFrame, text="Button 1", fg="red", bg="blue")
# button2 = Button(topFrame, text="Button 2", fg="blue")
# button3 = Button(topFrame, text="Button 3", fg="green")
# button4 = Button(bottomFrame, text="Button 4", fg="purple")
#
# button1.pack(side=LEFT)
# button2.pack(side=LEFT)
# button3.pack(side=LEFT)
# button4.pack(side=BOTTOM)

# one = Label(root, text="One", bg="red", fg="white")
# one.pack()
#
# two = Label(root, text="Two", bg="green", fg="black")
# two.pack(fill=X)
#
# three = Label(root, text="Three", bg="blue", fg="white")
# three.pack(side=LEFT, fill=Y)

# label_1 = Label(root, text="Name")
# label_2 = Label(root, text="Password")
# button1 = Button(root, text="Button 1", fg="red", bg="blue")
# # button1.pack(side=LEFT)
#
# entry_1 = Entry(root)
# entry_2 = Entry(root)
#
# label_1.grid(row=0, sticky=E)
# label_2.grid(row=1, sticky=E)
#
# entry_1.grid(row=0, column=1)
# entry_2.grid(row=1, column=1)
#
# c = Checkbutton(root, text="Keep me signed in")
# c.grid(columnspan=2)
#
# btn = Button(root, text="Print Name", command=printName)
# btn.grid(columnspan=2)


# Binding

# Technique I:

# def printName():
#     print "Name"
# btn = Button(root, text="Print Name", command=printName)
# btn.grid(columnspan=2)

# Technique II:

# def printNameII(event):
#     print "Name"
#
# btn2 = Button(root, text="Print my name again!")
# btn2.bind("<Button-1>", printNameII)
# btn2.grid(columnspan=2)

# def leftClick(event):
#     print("Left")
#
# def middleClick(event):
#     print("Middle")
#
# def rightClick(event):
#     print("Right")
#
# frame = Frame(root, width=300, height=250)
# frame.bind("<Button-1>", leftClick)
# frame.bind("<Button-2>", middleClick)
# frame.bind("<Button-3>", rightClick)
# frame.pack()

root.mainloop()