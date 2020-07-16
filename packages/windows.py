from tkinter import *
'''
import mysql.connector

robot_db = mysql.connector.connect(host="localhost", user="yourusername", password="yourpassword")

cursor = robot_db.cursor()

cursor.execute("CREATE TABLE fiche_config (S/N Robot VARCHAR(50), Nom du module VARCHAR(50), Reference interne du module VARCHAR(50), Adresse IP : Port(par defaut) VARCHAR(50), Mot de passe (par defaut) VARCHAR(50), Adresee IP: Port (modifiée) VARCHAR(50), Mot de passe (modifié) VARCHAR(50), Nom du fichier de configuration VARCHAR(50), Configuré par VARCHAR(50), Debut de configuration DATE, Fin de configuration DATE)")
cursor.execute("CREATE TABLE fiche_install (S/N Robot VARCHAR(50), Nom du PC VARCHAR(50), Nom de l'image VARCHAR(50), Reference PC  VARCHAR(50), Taille du disque en Go VARCHAR(50), Date du document VARCHAR(50), Installé par VARCHAR(50), Vérifié par VARCHAR(50), Debut d'installation DATE, Fin d'installation DATE)")
cursor.execute("CREATE TABLE fiche_fab (Nom du sous système VARCHAR(50), Reference du sous système VARCHAR(50), S/N Robot VARCHAR(50), Date du document VARCHAR(50), Fabriqué par VARCHAR(50), Vérifié par VARCHAR(50), Debut de fabrication DATE, Fin de fabrication DATE)")
'''
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

	def entry(self, frame, w, bg, j, rf, r, c, var = StringVar): 
		self.entry=Entry(frame, width = w, background = bg, justify = j, relief = rf, textvariable = var) 
		self.entry.grid(row = r, column = c)
		return self.entry

	def listbox(self, master, mode, r, c):
		self.listbox = Listbox(self.master, selectmode = mode)
		self.listbox.grid(row = r, column = c)
		return self.listbox


def config_window():
	#s_n, name, ref, ip_d, password_d, ip_m, password_m, fiche_name, configured, begin, end = StringVar()
	config_root = Tk()
	ConfigWindow = Window(config_root)
	config_root.title('Fiche de configuration')
	
	list = Window.listbox(ConfigWindow, config_root, BROWSE, 0, 0)

	for item in ["2 x 180 vue panoramique", "Caméra optique", "Caméra thermique", "Module 4G", "Lidar 3D", "WiFi", "Microphone", "Haut-parleur", "GPS", "Régulateur de température", "IP 54 housing", "ATV Tires"]:
		list.insert(END, item)

	choice_label = Window.label(ConfigWindow, config_root, 1, 30, list.curselection(), 'gray1', 'turquoise4', W, 5, 0)

	frame1 = Window.frame(ConfigWindow, config_root, 'peach puff', 2, GROOVE, BOTTOM, 0, 0)
	frame2 = Window.frame(ConfigWindow, config_root, 'peach puff', 2, GROOVE, BOTTOM, 0, 0)

	s_n_label = Window.label(ConfigWindow, frame1, 1, 30, 'S N robot:', 'bisque4', 'peach puff', W, 6, 0)
	module_name_label = Window.label(ConfigWindow, frame1, 1, 30, 'Nom du module:', 'bisque4', 'peach puff', W, 7, 0)
	module_ref_label = Window.label(ConfigWindow, frame1, 1, 30, 'Reference interne module:', 'bisque4', 'peach puff', W, 8, 0)
	ip_adress_label = Window.label(ConfigWindow, frame1, 1, 30, 'Adresse IP : Port (par defaut):', 'bisque4', 'peach puff', W, 9, 0)
	password_label = Window.label(ConfigWindow, frame1, 1, 30, 'Mot de passe (par defaut):', 'bisque4', 'peach puff', W, 10, 0)

	s_n_entry = Window.entry(ConfigWindow, frame1, 50, 'old lace', CENTER, FLAT, 6, 1, s_n)
	module_name_entry = Window.entry(ConfigWindow, frame1, 50, 'old lace', CENTER, FLAT, 7, 1, name)
	module_ref_entry = Window.entry(ConfigWindow, frame1, 50, 'old lace', CENTER, FLAT, 8, 1, ref)
	ip_adress_entry = Window.entry(ConfigWindow, frame1, 50, 'old lace', CENTER, FLAT, 9, 1, ip_d)
	password_entry = Window.entry(ConfigWindow, frame1, 50, 'old lace', CENTER, FLAT, 10, 1, password_d)


	ip_adress_mod_label = Window.label(ConfigWindow, frame2, 1, 30, 'Adresse IP: Port (modifiée):', 'bisque4', 'peach puff', W, 0, 0)
	password_mod_label = Window.label(ConfigWindow, frame2, 1, 30, 'Mot de passe (modifiée):', 'bisque4', 'peach puff', W, 1, 0)
	name_label = Window.label(ConfigWindow, frame2, 1, 30, 'Nom du fichier de configuration:', 'bisque4', 'peach puff', W, 2, 0)
	configurated_by_label = Window.label(ConfigWindow, frame2, 1, 30, 'Configuré par:', 'bisque4', 'peach puff', W, 3, 0)
	begin_config_label = Window.label(ConfigWindow, frame2, 1, 30, 'Debut de configuration:', 'bisque4', 'peach puff', W, 4, 0)
	end_config_label = Window.label(ConfigWindow, frame2, 1, 30, 'Fin de configuration:', 'bisque4', 'peach puff', W, 5, 0)
	

	ip_adress_mod_entry = Window.entry(ConfigWindow, frame2, 50, 'old lace', CENTER, FLAT, 0, 1, ip_m)
	password_mod_entry = Window.entry(ConfigWindow, frame2, 50, 'old lace', CENTER, FLAT, 1, 1, password_m)
	name_entry = Window.entry(ConfigWindow, frame2, 50, 'old lace', CENTER, FLAT, 2, 1, fiche_name)
	configurated_by_entry = Window.entry(ConfigWindow, frame2, 50, 'old lace', CENTER, FLAT, 3, 1, configured)
	begin_config_entry = Window.entry(ConfigWindow, frame2, 50, 'old lace', CENTER, FLAT, 4, 1, begin)
	end_config_entry = Window.entry(ConfigWindow, frame2, 50, 'old lace', CENTER, FLAT, 5, 1, end)
	

	config_root.mainloop()



def install_window():
	install_root = Tk()
	InstallWindow = Window(install_root)
	install_root.title('Fiche d installation')
	frame1 = Window.frame(InstallWindow, install_root, 'peach puff', 2, GROOVE, TOP, 5, 5)
	frame2 = Window.frame(InstallWindow, install_root, 'peach puff', 2, GROOVE, TOP, 5, 5)

	
	s_n_label = Window.label(InstallWindow, frame1, 1, 30, 'S N robot:', 'bisque4', 'peach puff', W, 0, 0)
	pc_name_label = Window.label(InstallWindow, frame1, 1, 30, 'Nom du PC:', 'bisque4', 'peach puff', W, 1, 0)
	image_name_label = Window.label(InstallWindow, frame1, 1, 30, 'Nom de l image:', 'bisque4', 'peach puff', W, 2, 0)
	pc_ref_label = Window.label(InstallWindow, frame1, 1, 30, 'Ref PC:', 'bisque4', 'peach puff', W, 3, 0)

	s_n_entry = Window.entry(InstallWindow, frame1, 50, 'old lace', CENTER, FLAT, 0, 1)
	pc_name_entry = Window.entry(InstallWindow, frame1, 50, 'old lace', CENTER, FLAT, 1, 1)
	image_name_entry = Window.entry(InstallWindow, frame1, 50, 'old lace', CENTER, FLAT, 2, 1)
	pc_ref_entry = Window.entry(InstallWindow, frame1, 50, 'old lace', CENTER, FLAT, 3, 1)


	disk_size_label = Window.label(InstallWindow, frame2, 1, 30, 'Taille du disque en Go:', 'bisque4', 'peach puff', W, 0, 0)
	doc_date_label = Window.label(InstallWindow, frame2, 1, 30, 'Date du document:', 'bisque4', 'peach puff', W, 1, 0)
	setbyy_label = Window.label(InstallWindow, frame2, 1, 30, 'Installé par:', 'bisque4', 'peach puff', W, 2, 0)
	validated_by_label = Window.label(InstallWindow, frame2, 1, 30, 'Verifié par:', 'bisque4', 'peach puff', W, 3, 0)
	begin_install_label = Window.label(InstallWindow, frame2, 1, 30, 'Debut d installation:', 'bisque4', 'peach puff', W, 4, 0)
	end_install_label = Window.label(InstallWindow, frame2, 1, 30, 'Fin d installation:', 'bisque4', 'peach puff', W, 5, 0)


	disk_size_entry = Window.entry(InstallWindow, frame2, 50, 'old lace', CENTER, FLAT, 0, 1)
	doc_date_entry = Window.entry(InstallWindow, frame2, 50, 'old lace', CENTER, FLAT, 1, 1)
	setbyy_entry = Window.entry(InstallWindow, frame2, 50, 'old lace', CENTER, FLAT, 2, 1)
	validated_by_entry = Window.entry(InstallWindow, frame2, 50, 'old lace', CENTER, FLAT, 3, 1)
	begin_install_entry = Window.entry(InstallWindow, frame2, 50, 'old lace', CENTER, FLAT, 4, 1)
	end_install_entry = Window.entry(InstallWindow, frame2, 50, 'old lace', CENTER, FLAT, 5, 1)

	install_root.mainloop()



def fab_window():
	fab_root = Tk()
	FabWindow = Window(fab_root)
	fab_root.title('Fiche de fabrication')
	frame1 = Window.frame(FabWindow, fab_root, 'peach puff', 2, GROOVE, TOP, 5, 5)
	frame2 = Window.frame(FabWindow, fab_root, 'peach puff', 2, GROOVE, TOP, 5, 5)

	sys_name_label = Window.label(FabWindow, frame1, 1, 30, 'Nom du sous systeme:', 'bisque4', 'peach puff', W, 0, 0)
	sys_ref_label = Window.label(FabWindow, frame1, 1, 30, 'Reference du sous systeme:', 'bisque4', 'peach puff', W, 1, 0)
	s_n_label = Window.label(FabWindow, frame1, 1, 30, 'S N robot:', 'bisque4', 'peach puff', W, 2, 0)

	sys_name_entry = Window.entry(FabWindow, frame1, 50, 'old lace', CENTER, FLAT, 0, 1)
	sys_ref_entry = Window.entry(FabWindow, frame1, 50, 'old lace', CENTER, FLAT, 1, 1)
	s_n_entry = Window.entry(FabWindow, frame1, 50, 'old lace', CENTER, FLAT, 2, 1)


	doc_date_label = Window.label(FabWindow, frame2, 1, 30, 'Date du document:', 'bisque4', 'peach puff', W, 0, 0)
	made_by_label = Window.label(FabWindow, frame2, 1, 30, 'Fabriqué par:', 'bisque4', 'peach puff', W, 1, 0)
	validated_by_label = Window.label(FabWindow, frame2, 1, 30, 'Verifié par:', 'bisque4', 'peach puff', W, 2, 0)
	begin_fab_label = Window.label(FabWindow, frame2, 1, 30, 'Debut de fabrication:', 'bisque4', 'peach puff', W, 3, 0)
	end_fab_label = Window.label(FabWindow, frame2, 1, 30, 'Fin de fabrication:', 'bisque4', 'peach puff', W, 4, 0)


	doc_date_entry = Window.entry(FabWindow, frame2, 50, 'old lace', CENTER, FLAT, 0, 1)
	setbyy_entry = Window.entry(FabWindow, frame2, 50, 'old lace', CENTER, FLAT, 1, 1)
	validated_by_entry = Window.entry(FabWindow, frame2, 50, 'old lace', CENTER, FLAT, 2, 1)
	begin_fab_entry = Window.entry(FabWindow, frame2, 50, 'old lace', CENTER, FLAT, 3, 1)
	end_fab_entry = Window.entry(FabWindow, frame2, 50, 'old lace', CENTER, FLAT, 4, 1)

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

		self.label1 = PrincipalWindow.label(self, self.frame1, 1, 30, 'Nom du robot', 'gray1', 'turquoise4', W, 0, 0)
		self.label2 = PrincipalWindow.label(self, self.frame2, 1, 30, 'Version du robot', 'gray1', 'turquoise4', W, 1, 0)

		var1 = StringVar()
		var2 = StringVar()

		self.entry1 = PrincipalWindow.entry(self, self.frame1, 50, 'old lace', CENTER, FLAT, 0, 1, var1)
		print(self.entry1.get())
		self.entry2 = PrincipalWindow.entry(self, self.frame2, 50, 'old lace', CENTER, FLAT, 1, 1, var2)

		#self.save_button = PrincipalWindow.window_button(self, self, 'Enregistrer', self.save_or_show, 'input')
		#self.show_button = PrincipalWindow.window_button(self, self, 'Récupérer', self.save_or_show, 'output')

		self.config_button_frame = PrincipalWindow.frame(self, self.master, 'peach puff', 2, GROOVE, TOP, 10, 11)
		self.install_button_frame = PrincipalWindow.frame(self, self.master, 'peach puff', 2, GROOVE, TOP, 30, 11)
		self.fab_button_frame = PrincipalWindow.frame(self, self.master, 'peach puff', 2, GROOVE, TOP, 20, 11)

		self.config_button = PrincipalWindow.window_button(self, self.config_button_frame, 'Fiches de configuration', self.open, 'config')
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
		elif txt == 'config':
			config_window()

'''
	def save_or_show(self,txt):
		if txt == 'input':
			self.config_button_frame = PrincipalWindow.frame(self, self.master, 'peach puff', 2, GROOVE, TOP, 10, 11)
			self.install_button_frame = PrincipalWindow.frame(self, self.master, 'peach puff', 2, GROOVE, TOP, 30, 11)
			self.fab_button_frame = PrincipalWindow.frame(self, self.master, 'peach puff', 2, GROOVE, TOP, 20, 11)
			
			self.config_button = PrincipalWindow.window_button(self, self.config_button_frame, 'Fiches de configuration', self.open_and_save, 'config')
			self.install_button = PrincipalWindow.window_button(self, self.install_button_frame, 'Fiches d installation', self.open_and_save, 'instal')
			self.fab_button = PrincipalWindow.window_button(self, self.fab_button_frame, 'Fiches de fabrication', self.open_and_save, 'fab')

			def open_and_save(self, txt):
				if txt == 'instal':
					install_window()
					install_sql = "INSERT INTO fiche_install VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
					install_val = (s_n_entry.get(), pc_name_entry.get(), image_name_entry.get(), pc_ref_entry.get(), disk_size_entry.get(), doc_date_entry.get(), setbyy_entry.get(), validated_by_entry.get(), begin_install_entry.get(), end_install_entry.get() )
					mycursor.execute(install_sql, install_val)
				elif txt == 'fab':
					fab_window()
					fab_sql = "INSERT INTO fiche_fab VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
					fab_val = (sys_name_entry.get(), sys_ref_entry.get(), s_n_entry.get(), doc_date_entry.get(), setbyy_entry.get(), validated_by_entry.get(), begin_fab_entry.get(), end_fab_entry.get())
					mycursor.execute(fab_sql, fab_val)
				elif txt == 'config':
					config_window()
					config_sql = "INSERT INTO fiche_config VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
					config_val = (s_n_entry.get(), module_name_entry.get(), module_ref_entry.get(), ip_adress_entry.get(), password_entry.get(), ip_adress_mod_entry.get(), password_mod_entry .get(), name_entry.get(), configurated_by_entry.get(), begin_config_entry.get(), end_config_entry.get())
					mycursor.execute(config_sql, config_val)
				robot_db.commit()

		elif txt == 'ouput':
			self.config_button_frame = PrincipalWindow.frame(self, self.master, 'peach puff', 2, GROOVE, TOP, 10, 11)
			self.install_button_frame = PrincipalWindow.frame(self, self.master, 'peach puff', 2, GROOVE, TOP, 30, 11)
			self.fab_button_frame = PrincipalWindow.frame(self, self.master, 'peach puff', 2, GROOVE, TOP, 20, 11)
			
			self.config_button = PrincipalWindow.window_button(self, self.config_button_frame, 'Fiches de configuration', self.show, 'config')
			self.install_button = PrincipalWindow.window_button(self, self.install_button_frame, 'Fiches d installation', self.show, 'instal')
			self.fab_button = PrincipalWindow.window_button(self, self.fab_button_frame, 'Fiches de fabrication', self.show, 'fab')

			def show(self, txt):
				if txt == 'instal':
					mycursor.execute("SELECT * FROM install_sql")
				elif txt == 'config':
					mycursor.execute("SELECT * FROM config_sql")
				elif txt == 'fab':
					mycursor.execute("SELECT * FROM fab_sql")
 '''

	
