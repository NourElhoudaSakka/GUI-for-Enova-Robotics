from windows import *
import mysql.connector

class bd:
    def __init__(self):
        self.robot_db = mysql.connector.connect(host = "127.0.0.1", user = "root", password = "EnovaRobotics123", port = 3306, database = "fiches_robot_bd")
        self.cursor = robot_db.cursor()
    
    def config_commande(self, config_val = ()):
        config_sql = ("INSERT INTO fiche_config VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        cursor.execute(config_sql, config_val)
        self.robot_db.commit()
        
    def install_commande(self, install_val = ()):
        install_sql = ('INSERT INTO fiche_install VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)')
        cursor.execute(install_sql, install_val)
        self.robot_db.commit()
        
    def fab_commande(self, fab_val = ()):
        fab_sql = ('INSERT INTO fiche_fab VALUES (%s, %s, %s, %s, %s, %s, %s, %s)')
        cursor.execute(fab_sql, fab_val)
        self.robot_db.commit()
        
    def show(self, txt):
        if txt == 'instal':
            self.cursor.execute("SELECT * FROM install_sql")
        elif txt == 'config':
            self.cursor.execute("SELECT * FROM config_sql")
        elif txt == 'fab':
            self.cursor.execute("SELECT * FROM fab_sql")

#cursor.execute("CREATE TABLE fiche_config (SN_Robot VARCHAR(50), Nom_du_module VARCHAR(50), Reference_interne_du_module VARCHAR(50), Adresse_IP_Port_par_defaut VARCHAR(50), Mot_de_passe_par_defaut VARCHAR(50), Adresee_IP_Port_modifiée VARCHAR(50), Mot_de_passe_modifié VARCHAR(50), Nom_du_fichier_de_configuration VARCHAR(50), Configuré_par VARCHAR(50), Debut_de_configuration VARCHAR(50), Fin_de_configuration VARCHAR(50))")
#cursor.execute("CREATE TABLE fiche_install (SN_Robot VARCHAR(50), Nom_du_PC VARCHAR(50), Nom_de_limage VARCHAR(50), Reference_PC  VARCHAR(50), Taille_du_disque_en_Go VARCHAR(50), Date_du_document VARCHAR(50), Installé_par VARCHAR(50), Vérifié_par VARCHAR(50), Debut_dinstallation VARCHAR(50), Fin_d_installation VARCHAR(50))")
#cursor.execute("CREATE TABLE fiche_fab (Nom_du_sous_système VARCHAR(50), Reference_du_sous_système VARCHAR(50), SN_Robot VARCHAR(50), Date_du_document VARCHAR(50), Fabriqué_par VARCHAR(50), Vérifié_par VARCHAR(50), Debut_de_fabrication VARCHAR(50), Fin_de_fabrication VARCHAR(50))")
