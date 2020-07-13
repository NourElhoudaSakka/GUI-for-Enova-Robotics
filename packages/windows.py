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

	def entry (self, frame, w, bg, j, rf, r, c): 
		self.entry=Entry(frame, width = w, background = bg, justify = j, relief = rf) 
		self.entry.grid(row = r, column = c)
		return self.entry

def install_window():
	install_root = Tk()
	InstallWindow = Window(install_root)
	install_root.title('Fiche d installation')
	frame1 = Window.frame(InstallWindow, install_root, 'peach puff', 2, GROOVE, TOP, 5, 5)
	frame2 = Window.frame(InstallWindow, install_root, 'peach puff', 2, GROOVE, TOP, 5, 5)
	frame3 = Window.frame(InstallWindow, install_root, 'peach puff', 2, GROOVE, TOP, 5, 5)
	frame4 = Window.frame(InstallWindow, install_root, 'peach puff', 2, GROOVE, TOP, 5, 5)

	ref_doc_label = Window.label(InstallWindow, frame1, 1, 30, 'Reference du document:', 'bisque4', 'peach puff', W, 0, 0)
	creation_date_label = Window.label(InstallWindow, frame1, 1, 30, 'Date de creation:', 'bisque4', 'peach puff', W, 1, 0)
	setby_label = Window.label(InstallWindow, frame1, 1, 30, 'Etablie par:', 'bisque4', 'peach puff', W, 2, 0)
	validatedby_label = Window.label(InstallWindow, frame1, 1, 30, 'Validée par:', 'bisque4', 'peach puff', W, 3, 0)

	ref_doc_entry = Window.entry(InstallWindow, frame1, 50, 'old lace', CENTER, FLAT, 0, 1)
	creation_date_entry = Window.entry(InstallWindow, frame1, 50, 'old lace', CENTER, FLAT, 1, 1)
	setby_entry = Window.entry(InstallWindow, frame1, 50, 'old lace', CENTER, FLAT, 2, 1)
	validatedby_entry = Window.entry(InstallWindow, frame1, 50, 'old lace', CENTER, FLAT, 3, 1)

	robot_name_label = Window.label(InstallWindow, frame2, 1, 30, 'Nom du robot:', 'bisque4', 'peach puff', W, 0, 0)
	s_n_label = Window.label(InstallWindow, frame2, 1, 30, 'S N robot:', 'bisque4', 'peach puff', W, 1, 0)
	pc_name_label = Window.label(InstallWindow, frame2, 1, 30, 'Nom du PC:', 'bisque4', 'peach puff', W, 2, 0)
	image_name_label = Window.label(InstallWindow, frame2, 1, 30, 'Nom de l image:', 'bisque4', 'peach puff', W, 3, 0)
	pc_ref_label = Window.label(InstallWindow, frame2, 1, 30, 'Ref PC:', 'bisque4', 'peach puff', W, 4, 0)

	robot_name_entry = Window.entry(InstallWindow, frame2, 50, 'old lace', CENTER, FLAT, 0, 1)
	s_n_entry = Window.entry(InstallWindow, frame2, 50, 'old lace', CENTER, FLAT, 1, 1)
	pc_name_entry = Window.entry(InstallWindow, frame2, 50, 'old lace', CENTER, FLAT, 2, 1)
	image_name_entry = Window.entry(InstallWindow, frame2, 50, 'old lace', CENTER, FLAT, 3, 1)
	pc_ref_entry = Window.entry(InstallWindow, frame2, 50, 'old lace', CENTER, FLAT, 4, 1)

	mod_indice_label = Window.label(InstallWindow, frame3, 1, 30, 'Indice de modification:', 'bisque4', 'peach puff', W, 0, 0)
	mod_setby_label = Window.label(InstallWindow, frame3, 1, 30, 'Modification établie par:', 'bisque4', 'peach puff', W, 1, 0)
	mod_date_label = Window.label(InstallWindow, frame3, 1, 30, 'Date de modification:', 'bisque4', 'peach puff', W, 2, 0)

	mod_indice_entry = Window.entry(InstallWindow, frame3, 50, 'old lace', CENTER, FLAT, 0, 1)
	mod_setby_entry = Window.entry(InstallWindow, frame3, 50, 'old lace', CENTER, FLAT, 1, 1)
	mod_date_entry = Window.entry(InstallWindow, frame3, 50, 'old lace', CENTER, FLAT, 2, 1)

	disk_size_label = Window.label(InstallWindow, frame4, 1, 30, 'Taille du disque en Go:', 'bisque4', 'peach puff', W, 0, 0)
	doc_date_label = Window.label(InstallWindow, frame4, 1, 30, 'Date du document:', 'bisque4', 'peach puff', W, 1, 0)
	setbyy_label = Window.label(InstallWindow, frame4, 1, 30, 'Installé par:', 'bisque4', 'peach puff', W, 2, 0)
	validated_by_label = Window.label(InstallWindow, frame4, 1, 30, 'Verifié par:', 'bisque4', 'peach puff', W, 3, 0)
	begin_install_label = Window.label(InstallWindow, frame4, 1, 30, 'Debut d installation:', 'bisque4', 'peach puff', W, 4, 0)
	end_install_label = Window.label(InstallWindow, frame4, 1, 30, 'Fin d installation:', 'bisque4', 'peach puff', W, 5, 0)


	disk_size_entry = Window.entry(InstallWindow, frame4, 50, 'old lace', CENTER, FLAT, 0, 1)
	doc_date_entry = Window.entry(InstallWindow, frame4, 50, 'old lace', CENTER, FLAT, 1, 1)
	setbyy_entry = Window.entry(InstallWindow, frame4, 50, 'old lace', CENTER, FLAT, 2, 1)
	validated_by_entry = Window.entry(InstallWindow, frame4, 50, 'old lace', CENTER, FLAT, 3, 1)
	begin_install_entry = Window.entry(InstallWindow, frame4, 50, 'old lace', CENTER, FLAT, 4, 1)
	end_install_entry = Window.entry(InstallWindow, frame4, 50, 'old lace', CENTER, FLAT, 5, 1)

	install_root.mainloop()



def fab_window():
	fab_root = Tk()
	FabWindow = Window(fab_root)
	fab_root.title('Fiche de fabrication')
	frame1 = Window.frame(FabWindow, fab_root, 'peach puff', 2, GROOVE, TOP, 5, 5)
	frame2 = Window.frame(FabWindow, fab_root, 'peach puff', 2, GROOVE, TOP, 5, 5)
	frame3 = Window.frame(FabWindow, fab_root, 'peach puff', 2, GROOVE, TOP, 5, 5)
	frame4 = Window.frame(FabWindow, fab_root, 'peach puff', 2, GROOVE, TOP, 5, 5)

	ref_doc_label = Window.label(FabWindow, frame1, 1, 30, 'Reference du document:', 'bisque4', 'peach puff', W, 0, 0)
	creation_date_label = Window.label(FabWindow, frame1, 1, 30, 'Date de creation:', 'bisque4', 'peach puff', W, 1, 0)
	setby_label = Window.label(FabWindow, frame1, 1, 30, 'Etablie par:', 'bisque4', 'peach puff', W, 2, 0)
	validatedby_label = Window.label(FabWindow, frame1, 1, 30, 'Validée par:', 'bisque4', 'peach puff', W, 3, 0)

	ref_doc_entry = Window.entry(FabWindow, frame1, 50, 'old lace', CENTER, FLAT, 0, 1)
	creation_date_entry = Window.entry(FabWindow, frame1, 50, 'old lace', CENTER, FLAT, 1, 1)
	setby_entry = Window.entry(FabWindow, frame1, 50, 'old lace', CENTER, FLAT, 2, 1)
	validatedby_entry = Window.entry(FabWindow, frame1, 50, 'old lace', CENTER, FLAT, 3, 1)

	sys_name_label = Window.label(FabWindow, frame2, 1, 30, 'Nom du sous systeme:', 'bisque4', 'peach puff', W, 0, 0)
	sys_ref_label = Window.label(FabWindow, frame2, 1, 30, 'Reference du sous systeme:', 'bisque4', 'peach puff', W, 1, 0)
	robot_name_label = Window.label(FabWindow, frame2, 1, 30, 'Nom du robot:', 'bisque4', 'peach puff', W, 2, 0)
	s_n_label = Window.label(FabWindow, frame2, 1, 30, 'S N robot:', 'bisque4', 'peach puff', W, 3, 0)

	sys_name_entry = Window.entry(FabWindow, frame2, 50, 'old lace', CENTER, FLAT, 0, 1)
	sys_ref_entry = Window.entry(FabWindow, frame2, 50, 'old lace', CENTER, FLAT, 1, 1)
	robot_name_entry = Window.entry(FabWindow, frame2, 50, 'old lace', CENTER, FLAT, 2, 1)
	s_n_entry = Window.entry(FabWindow, frame2, 50, 'old lace', CENTER, FLAT, 3, 1)

	mod_indice_label = Window.label(FabWindow, frame3, 1, 30, 'Indice de modification:', 'bisque4', 'peach puff', W, 0, 0)
	mod_setby_label = Window.label(FabWindow, frame3, 1, 30, 'Modification établie par:', 'bisque4', 'peach puff', W, 1, 0)
	mod_date_label = Window.label(FabWindow, frame3, 1, 30, 'Date de modification:', 'bisque4', 'peach puff', W, 2, 0)

	mod_indice_entry = Window.entry(FabWindow, frame3, 50, 'old lace', CENTER, FLAT, 0, 1)
	mod_setby_entry = Window.entry(FabWindow, frame3, 50, 'old lace', CENTER, FLAT, 1, 1)
	mod_date_entry = Window.entry(FabWindow, frame3, 50, 'old lace', CENTER, FLAT, 2, 1)

	doc_date_label = Window.label(FabWindow, frame4, 1, 30, 'Date du document:', 'bisque4', 'peach puff', W, 0, 0)
	made_by_label = Window.label(FabWindow, frame4, 1, 30, 'Fabriqué par:', 'bisque4', 'peach puff', W, 1, 0)
	validated_by_label = Window.label(FabWindow, frame4, 1, 30, 'Verifié par:', 'bisque4', 'peach puff', W, 2, 0)
	begin_fab_label = Window.label(FabWindow, frame4, 1, 30, 'Debut de fabrication:', 'bisque4', 'peach puff', W, 3, 0)
	end_fab_label = Window.label(FabWindow, frame4, 1, 30, 'Fin de fabrication:', 'bisque4', 'peach puff', W, 4, 0)


	doc_date_entry = Window.entry(FabWindow, frame4, 50, 'old lace', CENTER, FLAT, 0, 1)
	setbyy_entry = Window.entry(FabWindow, frame4, 50, 'old lace', CENTER, FLAT, 1, 1)
	validated_by_entry = Window.entry(FabWindow, frame4, 50, 'old lace', CENTER, FLAT, 2, 1)
	begin_install_entry = Window.entry(FabWindow, frame4, 50, 'old lace', CENTER, FLAT, 3, 1)
	end_install_entry = Window.entry(FabWindow, frame4, 50, 'old lace', CENTER, FLAT, 4, 1)

	fab_root.mainloop()



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

		self.config_button = PrincipalWindow.window_button(self, self.config_button_frame, 'Fiches de configuration', self.open, 'instal')
		self.install_button = PrincipalWindow.window_button(self, self.install_button_frame, 'Fiches d installation', self.open, 'instal')
		self.fab_button = PrincipalWindow.window_button(self, self.fab_button_frame, 'Fiches de fabrication', self.open, 'fab')
	
	def window_button(self, frame, texte, com, txt):
		self.button = Button(self.frame, text = texte, command = lambda : com(txt))
		self.button.pack()
		return self.button
 
	def open(self, txt):
		if txt == 'instal':
			install_window()
		elif txt == 'fab':
			fab_window()




