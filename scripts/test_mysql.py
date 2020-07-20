import mysql.connector

robot_db = mysql.connector.connect(host = "127.0.0.1", user = "root", password = "EnovaRobotics123", port = 3306, database = "fiches_robot_bd")

cursor = robot_db.cursor()

cursor.execute("CREATE TABLE fiche_config (SN_Robot VARCHAR(50), Nom_du_module VARCHAR(50), Reference_interne_du_module VARCHAR(50), Adresse_IP_Port_par_defaut VARCHAR(50), Mot_de_passe_par_defaut VARCHAR(50), Adresee_IP_Port_modifiée VARCHAR(50), Mot_de_passe_modifié VARCHAR(50), Nom_du_fichier_de_configuration VARCHAR(50), Configuré_par VARCHAR(50), Debut_de_configuration DATE, Fin_de_configuration DATE)")
cursor.execute("CREATE TABLE fiche_install (SN_Robot VARCHAR(50), Nom_du_PC VARCHAR(50), Nom_de_limage VARCHAR(50), Reference_PC  VARCHAR(50), Taille_du_disque_en_Go VARCHAR(50), Date_du_document VARCHAR(50), Installé_par VARCHAR(50), Vérifié_par VARCHAR(50), Debut_dinstallation DATE, Fin_d_installation DATE)")
cursor.execute("CREATE TABLE fiche_fab (Nom_du_sous_système VARCHAR(50), Reference_du_sous_système VARCHAR(50), SN_Robot VARCHAR(50), Date_du_document VARCHAR(50), Fabriqué_par VARCHAR(50), Vérifié_par VARCHAR(50), Debut_de_fabrication DATE, Fin_de_fabrication DATE)")


''' 
	def open(self, txt):
		if txt == 'instal':
			install_window()
		elif txt == 'fab':
			fab_window()
		elif txt == 'config':
			config_window()
'''