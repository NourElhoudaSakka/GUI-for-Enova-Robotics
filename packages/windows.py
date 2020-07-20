from tkinter import *
from tkinter import ttk

import mysql.connector

robot_db = mysql.connector.connect(host = "127.0.0.1", user = "root", password = "EnovaRobotics123", port = 3306, database = "fiches_robot_bd")

cursor = robot_db.cursor()

#cursor.execute("CREATE TABLE fiche_config (SN_Robot VARCHAR(50), Nom_du_module VARCHAR(50), Reference_interne_du_module VARCHAR(50), Adresse_IP_Port_par_defaut VARCHAR(50), Mot_de_passe_par_defaut VARCHAR(50), Adresee_IP_Port_modifiée VARCHAR(50), Mot_de_passe_modifié VARCHAR(50), Nom_du_fichier_de_configuration VARCHAR(50), Configuré_par VARCHAR(50), Debut_de_configuration VARCHAR(50), Fin_de_configuration VARCHAR(50))")
#cursor.execute("CREATE TABLE fiche_install (SN_Robot VARCHAR(50), Nom_du_PC VARCHAR(50), Nom_de_limage VARCHAR(50), Reference_PC  VARCHAR(50), Taille_du_disque_en_Go VARCHAR(50), Date_du_document VARCHAR(50), Installé_par VARCHAR(50), Vérifié_par VARCHAR(50), Debut_dinstallation VARCHAR(50), Fin_d_installation VARCHAR(50))")
#cursor.execute("CREATE TABLE fiche_fab (Nom_du_sous_système VARCHAR(50), Reference_du_sous_système VARCHAR(50), SN_Robot VARCHAR(50), Date_du_document VARCHAR(50), Fabriqué_par VARCHAR(50), Vérifié_par VARCHAR(50), Debut_de_fabrication VARCHAR(50), Fin_de_fabrication VARCHAR(50))")


class Window:
	'''
	parent class
	'''
	def __init__(self, master):
		self.master = master
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

	def combobox(self, master, val, x, y):
		self.combobox = ttk.Combobox(self.master, values = val)
		self.combobox.pack(padx = x, pady = y)
		return self.combobox


def config_window():
	s_n = StringVar()
	name = StringVar()
	ref = StringVar()
	ip_d = StringVar()
	password_d = StringVar()
	ip_m = StringVar()
	password_m = StringVar()
	fiche_name = StringVar()
	configured = StringVar()
	begin = StringVar()
	end = StringVar()
	
	config_root = Tk()
	ConfigWindow = Window(config_root)
	config_root.title('Fiche de configuration')
	
	values = ["2 x 180 vue panoramique", "Caméra optique", "Caméra thermique", "Module 4G", "Lidar 3D", "WiFi", "Microphone", "Haut-parleur", "GPS", "Régulateur de température", "IP 54 housing", "ATV Tires"]
	combo = Window.combobox(ConfigWindow, config_root, values, 2, 5)
	
	choice_frame = Window.frame(ConfigWindow, config_root, 'gray1', 0.2, GROOVE, TOP, 2, 10)
	choice_label = Window.label(ConfigWindow, choice_frame, 1, 30, str(combo.get()), 'gray1', 'turquoise4', W, 5, 0)

	frame1 = Window.frame(ConfigWindow, config_root, 'gray1', 0.2, GROOVE, TOP, 2, 15)
	frame2 = Window.frame(ConfigWindow, config_root, 'gray1', 0.2, GROOVE, TOP, 2, 30)

	s_n_label = Window.label(ConfigWindow, frame1, 1, 30, 'S N robot:', 'gray1', 'turquoise4', W, 0, 0)
	module_name_label = Window.label(ConfigWindow, frame1, 1, 30, 'Nom du module:', 'gray1', 'turquoise4', W, 1, 0)
	module_ref_label = Window.label(ConfigWindow, frame1, 1, 30, 'Reference interne module:', 'gray1', 'turquoise4', W, 2, 0)
	ip_adress_label = Window.label(ConfigWindow, frame1, 1, 30, 'Adresse IP : Port (par defaut):', 'gray1', 'turquoise4', W, 3, 0)
	password_label = Window.label(ConfigWindow, frame1, 1, 30, 'Mot de passe (par defaut):', 'gray1', 'turquoise4', W, 4, 0)

	s_n_entry = Window.entry(ConfigWindow, frame1, 50, 'old lace', CENTER, FLAT, 0, 1, s_n)
	module_name_entry = Window.entry(ConfigWindow, frame1, 50, 'old lace', CENTER, FLAT, 1, 1, name)
	module_ref_entry = Window.entry(ConfigWindow, frame1, 50, 'old lace', CENTER, FLAT, 2, 1, ref)
	ip_adress_entry = Window.entry(ConfigWindow, frame1, 50, 'old lace', CENTER, FLAT, 3, 1, ip_d)
	password_entry = Window.entry(ConfigWindow, frame1, 50, 'old lace', CENTER, FLAT, 4, 1, password_d)


	ip_adress_mod_label = Window.label(ConfigWindow, frame2, 1, 30, 'Adresse IP: Port (modifiée):', 'gray1', 'turquoise4', W, 0, 0)
	password_mod_label = Window.label(ConfigWindow, frame2, 1, 30, 'Mot de passe (modifiée):', 'gray1', 'turquoise4', W, 1, 0)
	name_label = Window.label(ConfigWindow, frame2, 1, 30, 'Nom du fichier de configuration:', 'gray1', 'turquoise4', W, 2, 0)
	configurated_by_label = Window.label(ConfigWindow, frame2, 1, 30, 'Configuré par:', 'gray1', 'turquoise4', W, 3, 0)
	begin_config_label = Window.label(ConfigWindow, frame2, 1, 30, 'Debut de configuration:', 'gray1', 'turquoise4', W, 4, 0)
	end_config_label = Window.label(ConfigWindow, frame2, 1, 30, 'Fin de configuration:', 'gray1', 'turquoise4', W, 5, 0)
	

	ip_adress_mod_entry = Window.entry(ConfigWindow, frame2, 50, 'old lace', CENTER, FLAT, 0, 1, ip_m)
	password_mod_entry = Window.entry(ConfigWindow, frame2, 50, 'old lace', CENTER, FLAT, 1, 1, password_m)
	name_entry = Window.entry(ConfigWindow, frame2, 50, 'old lace', CENTER, FLAT, 2, 1, fiche_name)
	configurated_by_entry = Window.entry(ConfigWindow, frame2, 50, 'old lace', CENTER, FLAT, 3, 1, configured)
	begin_config_entry = Window.entry(ConfigWindow, frame2, 50, 'old lace', CENTER, FLAT, 4, 1, begin)
	end_config_entry = Window.entry(ConfigWindow, frame2, 50, 'old lace', CENTER, FLAT, 5, 1, end)
	
	config_sql = 'INSERT INTO fiche_config VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
	config_val = (str(s_n.get()), str(name.get()), str(ref.get()), str(ip_d.get()), str(password_d.get()), str(ip_m.get()), str(password_m.get()), str(fiche_name.get()), str(configured.get()), str(begin.get()), str(end.get()))
	cursor.execute(config_sql, config_val)
	robot_db.commit()
	

	config_root.mainloop()



def install_window():
	s_n = StringVar()
	name = StringVar()
	image_name = StringVar()
	pc_ref = StringVar()
	disk_size = StringVar()
	doc_date = StringVar()
	setby = StringVar()
	validatedby = StringVar()
	begin = StringVar()
	end = StringVar()
	
	install_root = Tk()
	InstallWindow = Window(install_root)
	install_root.title('Fiche d installation')
	frame1 = Window.frame(InstallWindow, install_root, 'gray1', 0.2, GROOVE, TOP, 5, 5)
	frame2 = Window.frame(InstallWindow, install_root, 'gray1', 0.2, GROOVE, TOP, 5, 5)

	
	s_n_label = Window.label(InstallWindow, frame1, 1, 30, 'S N robot:', 'gray1', 'turquoise4', W, 0, 0)
	pc_name_label = Window.label(InstallWindow, frame1, 1, 30, 'Nom du PC:', 'gray1', 'turquoise4', W, 1, 0)
	image_name_label = Window.label(InstallWindow, frame1, 1, 30, 'Nom de l image:', 'gray1', 'turquoise4', W, 2, 0)
	pc_ref_label = Window.label(InstallWindow, frame1, 1, 30, 'Ref PC:', 'gray1', 'turquoise4', W, 3, 0)

	s_n_entry = Window.entry(InstallWindow, frame1, 50, 'old lace', CENTER, FLAT, 0, 1, s_n)
	pc_name_entry = Window.entry(InstallWindow, frame1, 50, 'old lace', CENTER, FLAT, 1, 1, name)
	image_name_entry = Window.entry(InstallWindow, frame1, 50, 'old lace', CENTER, FLAT, 2, 1, image_name)
	pc_ref_entry = Window.entry(InstallWindow, frame1, 50, 'old lace', CENTER, FLAT, 3, 1, pc_ref)


	disk_size_label = Window.label(InstallWindow, frame2, 1, 30, 'Taille du disque en Go:', 'gray1', 'turquoise4', W, 0, 0)
	doc_date_label = Window.label(InstallWindow, frame2, 1, 30, 'Date du document:', 'gray1', 'turquoise4', W, 1, 0)
	setbyy_label = Window.label(InstallWindow, frame2, 1, 30, 'Installé par:', 'gray1', 'turquoise4', W, 2, 0)
	validated_by_label = Window.label(InstallWindow, frame2, 1, 30, 'Verifié par:', 'gray1', 'turquoise4', W, 3, 0)
	begin_install_label = Window.label(InstallWindow, frame2, 1, 30, 'Debut d installation:', 'gray1', 'turquoise4', W, 4, 0)
	end_install_label = Window.label(InstallWindow, frame2, 1, 30, 'Fin d installation:', 'gray1', 'turquoise4', W, 5, 0)


	disk_size_entry = Window.entry(InstallWindow, frame2, 50, 'old lace', CENTER, FLAT, 0, 1, disk_size)
	doc_date_entry = Window.entry(InstallWindow, frame2, 50, 'old lace', CENTER, FLAT, 1, 1, doc_date)
	setbyy_entry = Window.entry(InstallWindow, frame2, 50, 'old lace', CENTER, FLAT, 2, 1, setby)
	validated_by_entry = Window.entry(InstallWindow, frame2, 50, 'old lace', CENTER, FLAT, 3, 1, validatedby)
	begin_install_entry = Window.entry(InstallWindow, frame2, 50, 'old lace', CENTER, FLAT, 4, 1, begin)
	end_install_entry = Window.entry(InstallWindow, frame2, 50, 'old lace', CENTER, FLAT, 5, 1, end)
	
	install_sql = 'INSERT INTO fiche_install VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
	install_val = (str(s_n.get()), str(name.get()), str(image_name.get()), str(pc_ref.get()), str(disk_size.get()), str(doc_date.get()), str(setby.get()), str(validatedby.get()), str(begin.get()), str(end.get()) )
	cursor.execute(install_sql, install_val)
	robot_db.commit()

	install_root.mainloop()



def fab_window():

	name = StringVar()
	ref = StringVar()
	s_n = StringVar()
	doc_date = StringVar()
	setby = StringVar()
	validatedby = StringVar()
	begin = StringVar()
	end = StringVar()

	fab_root = Tk()
	FabWindow = Window(fab_root)
	fab_root.title('Fiche de fabrication')
	frame1 = Window.frame(FabWindow, fab_root, 'gray1', 0.2, GROOVE, TOP, 5, 5)
	frame2 = Window.frame(FabWindow, fab_root, 'gray1', 0.2, GROOVE, TOP, 5, 5)

	sys_name_label = Window.label(FabWindow, frame1, 1, 30, 'Nom du sous systeme:', 'gray1', 'turquoise4', W, 0, 0)
	sys_ref_label = Window.label(FabWindow, frame1, 1, 30, 'Reference du sous systeme:', 'gray1', 'turquoise4', W, 1, 0)
	s_n_label = Window.label(FabWindow, frame1, 1, 30, 'S N robot:', 'gray1', 'turquoise4', W, 2, 0)

	sys_name_entry = Window.entry(FabWindow, frame1, 50, 'old lace', CENTER, FLAT, 0, 1)
	sys_ref_entry = Window.entry(FabWindow, frame1, 50, 'old lace', CENTER, FLAT, 1, 1)
	s_n_entry = Window.entry(FabWindow, frame1, 50, 'old lace', CENTER, FLAT, 2, 1)


	doc_date_label = Window.label(FabWindow, frame2, 1, 30, 'Date du document:', 'gray1', 'turquoise4', W, 0, 0)
	made_by_label = Window.label(FabWindow, frame2, 1, 30, 'Fabriqué par:', 'gray1', 'turquoise4', W, 1, 0)
	validated_by_label = Window.label(FabWindow, frame2, 1, 30, 'Verifié par:', 'gray1', 'turquoise4', W, 2, 0)
	begin_fab_label = Window.label(FabWindow, frame2, 1, 30, 'Debut de fabrication:', 'gray1', 'turquoise4', W, 3, 0)
	end_fab_label = Window.label(FabWindow, frame2, 1, 30, 'Fin de fabrication:', 'gray1', 'turquoise4', W, 4, 0)


	doc_date_entry = Window.entry(FabWindow, frame2, 50, 'old lace', CENTER, FLAT, 0, 1)
	setbyy_entry = Window.entry(FabWindow, frame2, 50, 'old lace', CENTER, FLAT, 1, 1)
	validated_by_entry = Window.entry(FabWindow, frame2, 50, 'old lace', CENTER, FLAT, 2, 1)
	begin_fab_entry = Window.entry(FabWindow, frame2, 50, 'old lace', CENTER, FLAT, 3, 1)
	end_fab_entry = Window.entry(FabWindow, frame2, 50, 'old lace', CENTER, FLAT, 4, 1)

	fab_sql = 'INSERT INTO fiche_fab VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
	fab_val = (str(name.get()), str(ref.get()), str(s_n.get()), str(doc_date.get()), str(setby.get()), str(validatedby.get()), str(begin.get()), str(end.get()))
	cursor.execute(fab_sql, fab_val)
	robot_db.commit()

	fab_root.mainloop()



class PrincipalWindow (Window):
	''' 
	
	principal window
	inherites from class window
	'''

	def __init__(self, master):
		Window.__init__(self, master)
		self.master.title('Fenetre principale')

		self.frame1 = PrincipalWindow.frame(self, self.master, 'gray1', 0.2, GROOVE, TOP, 5, 5) 
		self.frame2 = PrincipalWindow.frame(self, self.master, 'gray1', 0.2, GROOVE, TOP, 5, 11) 

		self.label1 = PrincipalWindow.label(self, self.frame1, 1, 30, 'Nom du robot', 'gray1', 'turquoise4', W, 0, 0)
		self.label2 = PrincipalWindow.label(self, self.frame2, 1, 30, 'Version du robot', 'gray1', 'turquoise4', W, 1, 0)

		var1 = StringVar()
		var2 = StringVar()

		self.entry1 = PrincipalWindow.entry(self, self.frame1, 50, 'old lace', CENTER, FLAT, 0, 1, var1)
		self.entry2 = PrincipalWindow.entry(self, self.frame2, 50, 'old lace', CENTER, FLAT, 1, 1, var2)
		
		self.frame3 = PrincipalWindow.frame(self, self.master, 'light gray', 2, FLAT, TOP, 5, 20) 
		self.frame4 = PrincipalWindow.frame(self, self.master, 'light gray', 2, FLAT, TOP, 5, 20) 

		self.save_button = PrincipalWindow.window_button(self, self.frame3, 'Enregistrer', self.save_or_show, 'input')
		self.show_button = PrincipalWindow.window_button(self, self.frame4, 'Récupérer', self.save_or_show, 'output')

	def window_button(self, frame, texte, com, txt):
		self.button = Button(self.frame, text = texte, command = lambda : com(txt))
		self.button.pack()
		return self.button

	def open_and_save(self, txt):
				if txt == 'instal':
					install_window()

				elif txt == 'fab':
					fab_window()
					
				elif txt == 'config':
					config_window()

				
	def show(self, txt):
		if txt == 'instal':
			mycursor.execute("SELECT * FROM install_sql")
		elif txt == 'config':
			mycursor.execute("SELECT * FROM config_sql")
		elif txt == 'fab':
			mycursor.execute("SELECT * FROM fab_sql")
	
	def save_or_show(self,txt):
		if txt == 'input':
			self.config_button_frame = PrincipalWindow.frame(self, self.master, 'light gray', 0.2, FLAT, TOP, 10, 11)
			self.install_button_frame = PrincipalWindow.frame(self, self.master, 'light gray', 0.2, FLAT, TOP, 30, 11)
			self.fab_button_frame = PrincipalWindow.frame(self, self.master, 'light gray', 0.2, FLAT, TOP, 20, 11)
			
			self.config_button = PrincipalWindow.window_button(self, self.config_button_frame, 'Fiches de configuration', self.open_and_save, 'config')
			self.install_button = PrincipalWindow.window_button(self, self.install_button_frame, 'Fiches d installation', self.open_and_save, 'instal')
			self.fab_button = PrincipalWindow.window_button(self, self.fab_button_frame, 'Fiches de fabrication', self.open_and_save, 'fab')

		elif txt == 'ouput':
			self.config_button_frame = PrincipalWindow.frame(self, self.master, 'gray1', 2, GROOVE, TOP, 10, 11)
			self.install_button_frame = PrincipalWindow.frame(self, self.master, 'gray1', 2, GROOVE, TOP, 30, 11)
			self.fab_button_frame = PrincipalWindow.frame(self, self.master, 'gray1', 2, GROOVE, TOP, 20, 11)
			
			self.config_button = PrincipalWindow.window_button(self, self.config_button_frame, 'Fiches de configuration', self.show, 'config')
			self.install_button = PrincipalWindow.window_button(self, self.install_button_frame, 'Fiches d installation', self.show, 'instal')
			self.fab_button = PrincipalWindow.window_button(self, self.fab_button_frame, 'Fiches de fabrication', self.show, 'fab')
			


