from windows import *
import mysql.connector

class DataBase:
    robot_db = mysql.connector.connect(host = "127.0.0.1", user = "root", password = "enovarobotics@123", port = 3306, database = "fiches_robot_bd")
    cursor = robot_db.cursor()
    
    
    def config_4G_commande(self, config_val):
        config_sql = ("INSERT INTO fiche_config_4G VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        self.cursor.execute(config_sql, config_val)
        self.robot_db.commit()
        
        
    def config_camera_commande(self, config_val):
        config_sql = ("INSERT INTO fiche_config_cam VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        self.cursor.execute(config_sql, config_val)
        self.robot_db.commit()
        
        
    def config_controlleur_commande(self, config_val):
        config_sql = ("INSERT INTO fiche_config__controlleur VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
        self.cursor.execute(config_sql, config_val)
        self.robot_db.commit()
        
        
    def install_img_commande(self, install_val):
        install_sql = ('INSERT INTO fiche_install_img_disque VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)')
        self.cursor.execute(install_sql, install_val)
        self.robot_db.commit()
        
        
    def install_controlleur_commande(self, install_val):
        install_sql = ('INSERT INTO fiche_install_controlleur VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)')
        self.cursor.execute(install_sql, install_val)
        self.robot_db.commit()
        
        
    def fab_commande(self, fab_val = ()):
        fab_sql = ('INSERT INTO fiche_fab VALUES (%s, %s, %s, %s, %s, %s, %s, %s)')
        self.cursor.execute(fab_sql, fab_val)
        self.robot_db.commit()
        
        
    def get_4G(self):
        self.cursor.execute("SELECT * FROM fiche_config_4G")
        self.data_4G = self.cursor.fetchall()
        return self.data_4G  


    def get_Cam(self):
        self.cursor.execute("SELECT * FROM fiche_config_cam")
        self.data_cam = self.cursor.fetchall()
        return self.data_cam  


    def get_configControl(self):
        self.cursor.execute("SELECT * FROM fiche_config__controlleur")
        self.data_control = self.cursor.fetchall()
        return self.data_control  


    def get_Img(self):
        self.cursor.execute("SELECT * FROM fiche_install_img_disque")
        self.data_img = self.cursor.fetchall()
        return self.data_img 


    def get_installControl(self):
        self.cursor.execute("SELECT * FROM fiche_install_controlleur")
        self.data_instal_control = self.cursor.fetchall()
        return self.data_instal_control


    def get_fab(self):
        self.cursor.execute("SELECT * FROM fiche_fab")
        self.data_fab = self.cursor.fetchall()
        return self.data_fab  