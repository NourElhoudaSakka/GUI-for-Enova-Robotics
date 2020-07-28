from tkinter import *
win = Tk()
x = StringVar()
f = Frame(win, relief = GROOVE)
f.pack()
e = Entry(f, textvariable = x)
e.pack()
def c():
    print( str(x.get()))
b = Button(win, text = 'click here', command = c)
b.pack()
win.mainloop()