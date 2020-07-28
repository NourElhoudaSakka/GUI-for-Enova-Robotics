from tkinter import *
win = Tk()
import mysql.connector

db = mysql.connector.connect(host = "127.0.0.1", user = "root", password = "EnovaRobotics123", port = 3306, database = "test")

cursor = db.cursor()

x1 = StringVar()
f1 = Frame(win, relief = GROOVE)
f1.pack()
e1 = Entry(f1, textvariable = x1)
e1.pack()
x2 = StringVar()
f2 = Frame(win, relief = GROOVE)
f2.pack()
e2 = Entry(f2, textvariable = x2)
e2.pack()


def c():
    sql = ("INSERT INTO table_de_test VALUES (%s,%s)")
    val = (str(e1.get()), str(e2.get()))
    cursor.execute(sql , val)
    db.commit()

b = Button(win, text = 'click here', command = c)
b.pack()
win.mainloop()