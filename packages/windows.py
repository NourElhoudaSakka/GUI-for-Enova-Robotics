from tkinter import *
from tkinter import ttk

class Window:
    def __init__(self, master):
        self.master = master
        self.master ['bg'] = 'light grey'
        
    def frame1(self, master, bg = 'gray1', bw = 0.2, r = GROOVE, s = TOP):
        self.frame1 = Frame(self.master, background = bg, borderwidth = bw, relief = r)
        return self.frame1

    def frame(self, master, x, y, bg = 'gray1', bw = 0.2, r = GROOVE, s = TOP):
        self.frame = Frame(self.master, background = bg, borderwidth = bw, relief = r)
        self.frame.pack(side = s, padx = x, pady = y)
        return self.frame
        
    def label(self, frame, texte = '', r = 0, c = 0, h = 1, w = 30, fg = 'gray1', bg = 'turquoise4', an = W): 
        self.label = Label(frame, height = h ,width = w, text = texte, foreground = fg, background = bg, anchor = an) 
        self.label.grid(row = r, column = c) 
        return self.label 
        
    def entry(self, frame, r = 0, c = 0, w = 50, bg = 'old lace', j = CENTER, rf = FLAT): 
        self.entry = Entry(frame, width = w, background = bg, justify = j, relief = rf) 
        self.entry.grid(row = r, column = c)
        return self.entry
    
    def button(self, master, cmd, param, x, y, txt = 'Enter'):
        self.button = Button(master, text = txt, command = lambda : cmd(param))
        self.button.pack(padx = x, pady = y)
        return self.button 
        
    def button1(self, master, cmd, param1, param2, x = 2, y = 45, txt = 'Entrer'):
        self.button1 = Button(master, text = txt, command = lambda: cmd (param1, param2))
        self.button1.pack(padx = x, pady = y)
        return self.button1 
        
    def combobox(self, master, val = [], x = 0, y = 0, var = ''):
        self.combobox = ttk.Combobox(self.master, values = val, textvariable = var)
        self.combobox.pack(padx = x, pady = y)
        return self.combobox

    def combobox1(self, master, val = [], x = 0, y = 0, var = ''):
        self.combobox = ttk.Combobox(self.master, values = val, textvariable = var)
        self.combobox.grid(row = x, column = y)
        return self.combobox
	
class PrincipalWindow (Window):
	''' 
	principal window
	inherites from class window 
	'''

	def __init__(self, master):
		Window.__init__(self, master)
		self.master.title('Fenetre principale')

		self.frame1 = PrincipalWindow.frame(self, self.master, 5, 5) 
		self.frame2 = PrincipalWindow.frame(self, self.master, 5, 11) 

		self.label1 = PrincipalWindow.label(self, self.frame1,'Nom du robot', 0, 0)
		self.label2 = PrincipalWindow.label(self, self.frame2,'Version du robot', 1, 0)

		self.entry1 = PrincipalWindow.entry(self, self.frame1, 0, 1)
		self.entry2 = PrincipalWindow.entry(self, self.frame2, 1, 1)
		
		self.frame3 = PrincipalWindow.frame(self, self.master, 5, 20, 'light gray') 
		self.frame4 = PrincipalWindow.frame(self, self.master, 5, 20, 'light gray') 

	def window_button(self, frame, texte, com, txt):
		self.button = Button(self.frame, text = texte, command = lambda : com(txt))
		self.button.pack()
		return self.button
