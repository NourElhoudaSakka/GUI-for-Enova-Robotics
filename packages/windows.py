from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image


class Window:
    def __init__(self, master):
        self.master = master
        self.configure_gui()
    
    
    def configure_gui(self):
        self.master ['bg'] = 'grey94'
        self.logo(self.master)
        self.master.geometry('830x470')
        
        
    def label(self, frame, texte = '', x = 0, y = 0): 
        self.label = Label(frame, height = 1 ,width = 25, text = texte, foreground = 'gray16', background = 'medium sea green', anchor = NW, font= ('Arial', 12)) 
        self.label.place(x = x, y = y) 
        return self.label
        
    
    def entry(self, master, x = 0, y = 0): 
        self.entry = Entry(master, borderwidth = 2, width = 40, background = 'grey84', justify = CENTER, font= ('Arial', 12), relief = FLAT) 
        self.entry.place(x = x, y = y)
        return self.entry
        
        
    def button(self, master, cmd, x = 0, y = 0, txt = 'Entrer'):
        button = Button(master, text = txt, font = ('Arial', 10), foreground = 'sea green', background = 'grey86')
        def commande():
            cmd()
            button['state'] = DISABLED
        button['command'] = commande
        button.place(x = x, y = y)
    
    
    def button_with_param(self, master, cmd, param, x = 0, y = 0, txt = 'Entrer', fg = 'gray16'):
        button = Button(master, text = txt, font = ('Arial', 10), foreground = fg, background = 'grey86')
        def commande():
            cmd(param)
            button['state'] = DISABLED
        button['command'] = commande
        button.place(x = x, y = y)

    def info_button(self, master, x, y, txt):
        self.photo = Image.open(r'C:\Users\Asus\Documents\GitHub\Enova-Application\packages\info.png')
        self.photo = self.photo.resize((20,20), Image.ANTIALIAS)
        self.photoi = ImageTk.PhotoImage(self.photo)
        def commande():
            window = Toplevel()
            window.title(' ')
            Label(window, text = txt, justify = LEFT).pack()
            button['state'] = DISABLED
        button = Button(master, image = self.photoi, command = commande)
        button.place(x = x, y = y)

    def combobox(self, master, val = [], x = 0, y = 0, var = ''):
        self.combobox = ttk.Combobox(self.master, values = val, textvariable = var, font= ('Arial', 10))
        self.combobox.place(x = x, y = y)
        return self.combobox
    
    
    def logo(self, master):
        self.img = Image.open(r"C:\Users\Asus\Documents\GitHub\Enova-Application\packages\enova.png")
        self.img = self.img.resize((200,50), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(self.img)
        self.imagelabel = Label(self.master, image = self.photoimg)
        self.imagelabel.place(x = 10, y = 10)