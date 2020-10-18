from windows import *
from principalWindow import *
from database import *
import datetime
import re


class EnterDataWindow(Window):

    db = DataBase()

    config_labels = ['Configuré par:', 'Début de configuration', 'Fin de configuration']
    fourG_labels = ['Nom du module', 'Reference interne module', 'Adresse IP : Port (par defaut):', 'Mot de passe (par defaut):', 'Adresse IP: Port (modifiée):', 'Mot de passe (modifiée):', 'Nom du fichier de configuration']
    control_labels = ['Type du controlleur', 'S/N fabricant du controlleur', 'Référence interne:', 'Version firmware:', 'Version profile:']
    cam_labels = ['Type de caméra:', 'Reference interne de la caméra:', 'Nom du fichier de configuration:', 'Version du firmware:','Adresse IP:', 'Nom de l utilisateur:', 'Mot de passe:']
    install_labels = ['Installé par:', 'Verifié par:', '''Début d'installation:''', '''Fin d'installation:''']
    img_labels = ['Nom du PC:', 'Nom de l image:', 'Ref PC:', 'Taille du disque en Go:', 'Date du document:']
    fab_labels = ['Nom du sous systeme:', 'Réference du sous systeme:', 'Date du document:', 'Fabriqué par:', 'Verifié par:', 'Début de fabrication:', 'Fin de fabrication:']


    def __init__(self, master):
        Window.__init__(self, master)
        self.configure_gui()
        self.version = PrincipalWindow.version


    def configure_gui(self):
        Window.configure_gui(self)
        info = ''' Bienvenue une autre fois sur cette fenêtre!\n Veuillez saisir toutes les informations nécessaires de cette fiche et finir par appuyer sur le bouton 'entrer' pour qu'elles passent à la base de données.'''
        Window.info_button(self, self.master, 430, 60, info)
        

    def set_config(self):
        values = ["Module 4G", "Caméra", "Controlleur"]
        self.master.title('Fiche de configuration')
        self.create_combobox(values, self.config_choose)


    def config_choose(self, choice):
        self.create_labels(self.config_labels, 140)

        if choice == "Module 4G":
            y = 225
            self.configurated_by_entry = self.set_entry(140)
            self.begin_config_entry = self.set_entry(165, '../../....  ..:..')
            self.end_config_entry = self.set_entry(190, '../../....  ..:..')

            self.create_labels(self.fourG_labels, 225)

            self.module_name_entry = self.set_entry(y)
            self.module_ref_entry = self.set_entry(y+25)
            self.ip_adress_entry = self.set_entry(y+50, '---.---.---.---:')
            self.password_entry = self.set_entry(y+75)
            self.ip_adress_mod_entry = self.set_entry(y+100, '---.---.---.---:')
            self.password_mod_entry = self.set_entry(y+125)
            self.name_entry = self.set_entry(y+150)

            self.create_enter_button(self.check_enter_4G)
        
        if choice == "Caméra":
            var2 = StringVar()
            y = 225
            entries = ["Thermique AXIS", "Optique AXIS", "Frontale VIVOTEK", "Arrière VIVOTEK"]
            type_cam_entry = Window.combobox(self, self.master, entries, 370, y, var2)
            type_cam_entry['width'] = 49

            cam_configurated_by_entry = self.set_entry(140)
            cam_begin_config_entry = self.set_entry(165, '../../....  ..:..')
            cam_end_config_entry = self.set_entry(190, '../../....  ..:..')

            self.create_labels(self.cam_labels, 225)

            cam_ref_entry = self.set_entry(y+25)
            file_name_entry = self.set_entry(y+50)
            firmware_entry = self.set_entry(y+75)
            ip_entry = self.set_entry(y+100)
            username_entry = self.set_entry(y+125)
            password_entry = self.set_entry(y+150) 

            def cam_cmd():
                cam_entred = [self.version, str(type_cam_entry.get()), str(cam_ref_entry.get()), str(file_name_entry.get()), str(firmware_entry.get()), str(ip_entry.get()), str(username_entry.get()), str(password_entry.get()), cam_configurated_by_entry.get()]
                self.check_enter(self.db.config_camera_commande, cam_entred, cam_begin_config_entry.get(), cam_end_config_entry.get())
            self.create_enter_button(cam_cmd)

        if choice == "Controlleur":
            y = 225
            control_configurated_by_entry = self.set_entry(140)
            control_begin_config_entry = self.set_entry(165, '../../....  ..:..')
            control_end_config_entry = self.set_entry(190, '../../....  ..:..')
            
            self.create_labels(self.control_labels, 225)

            type_entry = self.set_entry(y)
            sn_fabricant_entry = self.set_entry(y+25)
            ref_entry = self.set_entry(y+50)
            firmware_entry = self.set_entry(y+75)
            profile_entry = self.set_entry(y+100)

            def control_cmd():
                control_entred = [self.version, str(type_entry.get()), str(sn_fabricant_entry.get()), str(ref_entry.get()), str(firmware_entry.get()), str(profile_entry.get()), control_configurated_by_entry.get()]
                self.check_enter(self.db.config_controlleur_commande, control_entred, control_begin_config_entry.get(), control_end_config_entry.get())
            self.create_enter_button(control_cmd)


    def set_install(self):
        values = ["Image disque", 'Controlleur']
        self.master.title('Fiche d installation')
        self.create_combobox(values, self.install_choose)


    def install_choose(self, choice):
        y = 140
        y2 = 250
        self.create_labels(self.install_labels, 140)
        if choice == "Image disque":
            setbyy_entry = self.set_entry(y)
            validated_by_entry = self.set_entry(y+25)
            begin_install_entry = self.set_entry(y+50, '../../....  ..:..')
            end_install_entry = self.set_entry(y+75, '../../....  ..:..')

            self.create_labels(self.img_labels, 250)

            pc_name_entry = self.set_entry(y2)
            image_name_entry = self.set_entry(y2+25)
            pc_ref_entry = self.set_entry(y2+50)
            disk_size_entry = self.set_entry(y2+75)
            doc_date_entry = self.set_entry(y2+100)
            
            def img_cmd():
                entred = [self.version, str(pc_name_entry.get()), str(image_name_entry.get()), str(pc_ref_entry.get()), str(disk_size_entry.get()), str(doc_date_entry.get()), setbyy_entry.get(), validated_by_entry.get()]
                self.check_enter(self.db.install_img_commande, entred, begin_install_entry.get(), end_install_entry.get())
            self.create_enter_button(img_cmd)

        if choice == 'Controlleur':
            setbyy_entry = self.set_entry(y)
            validated_by_entry = self.set_entry(y+25)
            begin_install_entry = self.set_entry(y+50, '../../....  ..:..')
            end_install_entry = self.set_entry(y+75, '../../....  ..:..')

            self.create_labels(self.control_labels, 250)

            type_entry = self.set_entry(y2)
            sn_fabricant_entry = self.set_entry(y2+25)
            ref_entry = self.set_entry(y2+50)
            firmware_entry = self.set_entry(y2+75)
            profile_entry = self.set_entry(y2+100)

            def cmd():
                entred = [self.version, str(type_entry.get()), str(sn_fabricant_entry.get()), str(ref_entry.get()), str(firmware_entry.get()), str(profile_entry.get()), setbyy_entry.get(), validated_by_entry.get()]
                self.check_enter(self.db.install_controlleur_commande, entred, begin_install_entry.get(), end_install_entry.get())
            self.create_enter_button(cmd)


    def set_fab(self):
        y = 140
        self.master.title('Fiche de fabrication')
        self.create_labels(self.fab_labels, 140)
        sys_name_entry = self.set_entry(y)
        sys_ref_entry = self.set_entry(y+25)
        doc_date_entry = self.set_entry(y+50)
        setbyy_entry = self.set_entry(y+75)
        validated_by_entry = self.set_entry(y+100)
        begin_fab_entry = self.set_entry(y+125, '../../....  ..:..')
        end_fab_entry = self.set_entry(y+150, '../../....  ..:..')
        
        def cmd():
            entred = [self.version, str(sys_name_entry.get()), str(sys_ref_entry.get()), str(doc_date_entry.get()), str(setbyy_entry.get()), str(validated_by_entry.get())]
            self.check_enter(self.db.fab_commande, entred, begin_fab_entry.get(), end_fab_entry.get())
        self.create_enter_button(cmd)


    def create_enter_button(self, cmd):
        Window.button(self, self.master, cmd, 425, 420, 'Entrer')


    def check_enter_4G(self):
        if not re.search("^[0-9]{3}[.][0-9]{3}[.][0-9]{3}[.][0-9]{3}[:][0-9]*$", self.ip_adress_entry.get()) or not re.search("^[0-9]{3}[.][0-9]{3}[.][0-9]{3}[.][0-9]{3}[:][0-9]*$", self.ip_adress_mod_entry.get()):
            messagebox.showerror("Erreur", "Veuillez respecter le format demandé de l'adresse IP")
            entred = []
        else:
            entred = [self.version, self.module_name_entry.get(), self.module_ref_entry.get(), self.ip_adress_entry.get(), self.password_entry.get(), self.ip_adress_mod_entry.get(), self.password_mod_entry.get(), self.name_entry.get(),self.configurated_by_entry.get()]
        self.check_enter(self.db.config_4G_commande, entred, self.begin_config_entry.get(), self.end_config_entry.get())


    def check_enter(self, cmd, param, begin, end):
        x = True
        try:
            checked_begin = datetime.datetime.strptime(begin, '%d/%m/%Y %H:%M')
            checked_end = datetime.datetime.strptime(end, '%d/%m/%Y %H:%M')
            param.extend([checked_begin, checked_end])
        except:
            messagebox.showerror("Erreur", "Veuillez respecter le format demandé de la date")
            x = False
        for i in param:
            if i == '':
                messagebox.showerror("Erreur",'Un des champs est vide')
                x = False
                break
        if x == True:
            cmd(param)


    def create_combobox(self, values, choose):
        def callbackFunc(event):
            choose(str(combo.get()))
        var = StringVar()
        combo = Window.combobox(self, self.master, values, 365, 100, var)
        combo.current()
        combo.bind("<<ComboboxSelected>>", callbackFunc)

    
    def create_labels(self, labels , y):
        for label in labels:
            Window.label(self, self.master, label, 130, y)
            y += 25

    
    def set_entry(self, y, expected = ''):
        self.e = Window.entry(self, self.master, 370, y)
        self.e.insert(END, expected)
        return (self.e)
