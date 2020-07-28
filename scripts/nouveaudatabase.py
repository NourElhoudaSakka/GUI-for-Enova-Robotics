from nouveauwindows import *
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