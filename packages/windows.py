from tkinter import *

class Window:
	'''
	parent class
	'''
	def __init__(self, master):
		self.master = master
		self.frame = Frame(self.master)
		self.master ['bg'] = 'light grey'


	def frame(self, master, bg, bw, r, s, x, y):
		self.frame = Frame(self.master, background = bg, borderwidth = bw, relief = r)
		self.frame.pack(side = s, padx = x, pady = y)
		return self.frame


	def label(self, frame, h, w, texte, fg, bg, an, r, c): 
		''' 
		fontion des Labels 
		@param window_frame : windows for tkinter 
		@type  
		@param h : height 
		@type int 
		@return  
		@type Label 
		'''  
		self.label = Label(frame, height = h ,width = w, text = texte, foreground = fg, background = bg, anchor = an) 
		self.label.grid(row = r, column = c) 
		return self.label 

	def entry (self, frame, w, bg, j, rf, r, c ): 
		self.entry=Entry (frame, width = w, background = bg, justify = j, relief = rf) 
		self.entry.grid ( row = r, column = c )
		return self.entry


class PrincipalWindow (Window):
	''' 
	principal window
	inherites from class window
	'''
	def __init__(self, master):
		Window.__init__(self, master)
		self.master.title('Fenetre principale')

		self.frame1 = PrincipalWindow.frame(self, self.master, 'peach puff', 2, GROOVE, TOP, 5, 5) 
		self.frame2 = PrincipalWindow.frame(self, self.master, 'peach puff', 2, GROOVE, TOP, 5, 11) 
		self.frame3 = PrincipalWindow.frame(self, self.master, 'peach puff', 2, GROOVE, TOP, 5, 11) 
		self.frame4 = PrincipalWindow.frame(self, self.master, 'peach puff', 2, GROOVE, TOP, 5, 11) 

		self.label1 = PrincipalWindow.label(self, self.frame1, 1, 30, 'Nom du robot', 'bisque4', 'peach puff', W, 0, 0)
		self.label2 = PrincipalWindow.label(self, self.frame2, 1, 30, 'Version du robot', 'bisque4', 'peach puff', W, 1, 0)
		self.label3 = PrincipalWindow.label(self, self.frame3, 1, 30, 'Nom du PC', 'bisque4', 'peach puff', W, 2, 0)
		self.label4 = PrincipalWindow.label(self, self.frame4, 1, 30, 'Ref du PC', 'bisque4', 'peach puff', W, 3, 0)

		self.entry1 = PrincipalWindow.entry(self, self.frame1, 50, 'old lace', CENTER, FLAT, 0, 1)
		self.entry2 = PrincipalWindow.entry(self, self.frame2, 50, 'old lace', CENTER, FLAT, 1, 1)
		self.entry3 = PrincipalWindow.entry(self, self.frame3, 50, 'old lace', CENTER, FLAT, 2, 1)
		self.entry4 = PrincipalWindow.entry(self, self.frame4, 50, 'old lace', CENTER, FLAT, 3, 1)
		
		self.config_button_frame = PrincipalWindow.frame(self, self.master, 'peach puff', 2, GROOVE, TOP, 10, 11)
		self.install_button_frame = PrincipalWindow.frame(self, self.master, 'peach puff', 2, GROOVE, TOP, 30, 11)
		self.fab_button_frame = PrincipalWindow.frame(self, self.master, 'peach puff', 2, GROOVE, TOP, 20, 11)

		self.config_button = PrincipalWindow.window_button(self, self.config_button_frame, 'Fichiers configuration', self.open, ConfigWindow)
		self.install_button = PrincipalWindow.window_button(self, self.install_button_frame, 'Fichiers installation', self.open, InstallWindow)
		self.fab_button = PrincipalWindow.window_button(self, self.fab_button_frame, 'Fichiers sous systemes', self.open, FabWindow)
	
	def window_button(self, frame, texte, com, window):
		self.button = Button(self.frame, text = texte, command = lambda : com(window))
		self.button.pack()
		return self.button
 
	def open(self, win):
		self.win = Tk()
		self.win.mainloop()

		
class ConfigWindow(Window):
	pass

class InstallWindow(Window):
	pass

class FabWindow(Window):
	pass


