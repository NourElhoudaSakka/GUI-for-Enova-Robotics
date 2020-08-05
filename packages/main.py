import mysql.connector
from windows import *
from database import *

root = Tk()
principal_window = PrincipalWindow(root)
bd = DataBase()

def config_window():
    config_root = Tk()
    ConfigWindow = Window(config_root)
    config_root.title('Fiche de configuration')

    frame1 = Window.frame1(ConfigWindow, config_root)
    frame2 = Window.frame1(ConfigWindow, config_root)

    var = StringVar()
    values = ["Module 4G", "Caméra", "Controlleur"]
    combo = Window.combobox(ConfigWindow, config_root, values, 2, 5, var)
    combo.set('choisir un module')
    combo.current()
    
    def choose(txt):
        config_val = list()
        if txt == "Module 4G":
            Window.label(ConfigWindow, frame1, 'Nom du module:', 1, 0)
            Window.label(ConfigWindow, frame1, 'Reference interne module:', 2, 0)
            Window.label(ConfigWindow, frame1, 'Adresse IP : Port (par defaut):', 3, 0)
            Window.label(ConfigWindow, frame1, 'Mot de passe (par defaut):', 4, 0)
            
            module_name_entry = Window.entry(ConfigWindow, frame1, 1, 1)
            module_ref_entry = Window.entry(ConfigWindow, frame1, 2, 1)
            ip_adress_entry = Window.entry(ConfigWindow, frame1, 3, 1)
            password_entry = Window.entry(ConfigWindow, frame1, 4, 1)
            
            Window.label(ConfigWindow, frame2, 'Adresse IP: Port (modifiée):', 0, 0)
            Window.label(ConfigWindow, frame2, 'Mot de passe (modifiée):', 1, 0)
            Window.label(ConfigWindow, frame2, 'Nom du fichier de configuration:', 2, 0)
            
            ip_adress_mod_entry = Window.entry(ConfigWindow, frame2, 0, 1)
            password_mod_entry = Window.entry(ConfigWindow, frame2, 1, 1)
            name_entry = Window.entry(ConfigWindow, frame2, 2, 1)

        if txt == "Caméra":
            var2 = StringVar()
            entries = ["Thermique AXIS", "Optique AXIS", "Frontale VIVOTEK", "Arrière VIVOTEK"]

            Window.label(ConfigWindow, frame1, 'Type de caméra:', 1, 0)
            Window.label(ConfigWindow, frame1, 'Reference interne de la caméra:', 2, 0)
            Window.label(ConfigWindow, frame1, 'Nom du fichier de configuration:', 3, 0)
            type_cam_entry = Window.combobox(ConfigWindow, frame1, entries, 1, 1, var2)
            cam_ref_entry = Window.entry(ConfigWindow, frame1, 2, 1)
            file_name_entry = Window.entry(ConfigWindow, frame1, 3, 1)
            
            Window.label(ConfigWindow, frame2, 'Version du firmware:', 0, 0)
            Window.label(ConfigWindow, frame2, 'Adresse IP:', 1, 0)
            Window.label(ConfigWindow, frame2, 'Nom de l utilisateur:', 2, 0)
            Window.label(ConfigWindow, frame2, 'Mot de passe:', 3, 0)
            
            firmware_entry = Window.entry(ConfigWindow, frame2, 0, 1)
            ip_entry = Window.entry(ConfigWindow, frame2, 1, 1)
            username_entry = Window.entry(ConfigWindow, frame2, 2, 1)
            password_entry = Window.entry(ConfigWindow, frame2, 3, 1) 

        if txt == "Controlleur":
            Window.label(ConfigWindow, frame1, 'Nom du module:', 1, 0)
            Window.label(ConfigWindow, frame1, 'Reference interne module:', 2, 0)
            Window.label(ConfigWindow, frame1, 'Adresse IP : Port (par defaut):', 3, 0)
            Window.label(ConfigWindow, frame1, 'Mot de passe (par defaut):', 4, 0)
            
            module_name_entry = Window.entry(ConfigWindow, frame1, 1, 1)
            module_ref_entry = Window.entry(ConfigWindow, frame1, 2, 1)
            ip_adress_entry = Window.entry(ConfigWindow, frame1, 3, 1)
            password_entry = Window.entry(ConfigWindow, frame1, 4, 1)
            
            Window.label(ConfigWindow, frame2, 'Adresse IP: Port (modifiée):', 0, 0)
            Window.label(ConfigWindow, frame2, 'Mot de passe (modifiée):', 1, 0)
            Window.label(ConfigWindow, frame2, 'Nom du fichier de configuration:', 2, 0)
            
            ip_adress_mod_entry = Window.entry(ConfigWindow, frame2, 0, 1)
            password_mod_entry = Window.entry(ConfigWindow, frame2, 1, 1)
            name_entry = Window.entry(ConfigWindow, frame2, 2, 1)

        def set(x):
            config_val = [str(configurated_by_entry.get()), str(begin_config_entry.get()), str(end_config_entry.get())]
            if txt == "Module 4G":   
                config_val.extend([str(module_name_entry.get()), str(module_ref_entry.get()), str(ip_adress_entry.get()), str(password_entry.get()), str(ip_adress_mod_entry.get()), str(password_mod_entry.get()), str(name_entry.get())])
                bd.config_4G_commande(config_val)

            elif txt == "Caméra":   
                config_val.extend([str(type_cam_entry.get()), str(cam_ref_entry.get()), str(file_name_entry.get()), str(firmware_entry.get()), str(ip_entry.get()), str(username_entry.get()), str(password_entry.get())])
                bd.config_camera_commande(config_val)
                '''

            elif txt == "Controlleur":   
                config_val.extend([str(module_name_entry.get()), str(module_ref_entry.get()), str(ip_adress_entry.get()), str(password_entry.get()), str(ip_adress_mod_entry.get()), str(password_mod_entry.get()), str(name_entry.get())])
                bd.config_controlleur_commande(config_val)
                '''
        print (config_val)

        Window.button(ConfigWindow, config_root, set, 1, 2, 45)
        
    def callbackFunc(event):
        choose(str(combo.get()))   
            
    
    Window.label(ConfigWindow, frame2, 'Configuré par:', 3, 0)
    Window.label(ConfigWindow, frame2, 'Debut de configuration:', 4, 0)
    Window.label(ConfigWindow, frame2, 'Fin de configuration:', 5, 0)

    configurated_by_entry = Window.entry(ConfigWindow, frame2, 3, 1)
    begin_config_entry = Window.entry(ConfigWindow, frame2, 4, 1)
    end_config_entry = Window.entry(ConfigWindow, frame2, 5, 1)

    combo.bind("<<ComboboxSelected>>", callbackFunc)
    frame1.pack(padx = 2, pady = 15)
    frame2.pack(padx = 2, pady = 30)  

    config_root.mainloop()

def install_window():
    install_root = Tk()
    InstallWindow = Window(install_root)
    install_root.title('Fiche d installation')
    
    frame1 = Window.frame1(InstallWindow, install_root)
    frame2 = Window.frame1(InstallWindow, install_root)

    def choose(txt):
        install_val = list()
        if (txt == "Image disque"):
            Window.label(InstallWindow, frame1, 'Nom du PC:', 1, 0)
            Window.label(InstallWindow, frame1, 'Nom de l image:', 2, 0)
            Window.label(InstallWindow, frame1, 'Ref PC:', 3, 0)
            
            pc_name_entry = Window.entry(InstallWindow, frame1, 1, 1)
            image_name_entry = Window.entry(InstallWindow, frame1, 2, 1)
            pc_ref_entry = Window.entry(InstallWindow, frame1, 3, 1)
            
            Window.label(InstallWindow, frame2, 'Taille du disque en Go:', 0, 0)
            Window.label(InstallWindow, frame2, 'Date du document:', 1, 0)
            
            disk_size_entry = Window.entry(InstallWindow, frame2, 0, 1)
            doc_date_entry = Window.entry(InstallWindow, frame2, 1, 1)
            def set(x):
                install_val = [str(pc_name_entry.get()), str(image_name_entry.get()), str(pc_ref_entry.get()), str(disk_size_entry.get()), str(doc_date_entry.get()), str(setbyy_entry.get()), str(validated_by_entry.get()), str(begin_install_entry.get()), str(end_install_entry.get())]
                bd.install_commande(install_val)
                print (install_val)
        Window.button(InstallWindow, install_root, set, 1, 2, 45)

          
    def callbackFunc(event):
        choose(str(combo.get()))   

    var = StringVar()
    values = ["Image disque"]
    combo = Window.combobox(InstallWindow, install_root, values, 2, 5, var)
    combo.set('choisir un module')
    combo.current()

    Window.label(InstallWindow, frame2, 'Installé par:', 2, 0)
    Window.label(InstallWindow, frame2, 'Verifié par:', 3, 0)
    Window.label(InstallWindow, frame2, 'Debut d installation:', 4, 0)
    Window.label(InstallWindow, frame2, 'Fin d installation:', 5, 0)
    
    setbyy_entry = Window.entry(InstallWindow, frame2, 2, 1)
    validated_by_entry = Window.entry(InstallWindow, frame2, 3, 1)
    begin_install_entry = Window.entry(InstallWindow, frame2, 4, 1)
    end_install_entry = Window.entry(InstallWindow, frame2, 5, 1)
        
    combo.bind("<<ComboboxSelected>>", callbackFunc)
    frame1.pack(padx = 5, pady = 5)
    frame2.pack(padx = 5, pady = 5)  

    install_root.mainloop() 

def fab_window():
    fab_root = Tk()
    FabWindow = Window(fab_root)
    fab_root.title('Fiche de fabrication')
    
    var = StringVar()
    values = ["Module 4G", "Caméra", "Controlleur", "Image disque"]
    combo = Window.combobox(FabWindow, fab_root, values, 2, 5, var)
    combo.set('choisir un module')
    combo.current()
    
    frame1 = Window.frame(FabWindow, fab_root, 5, 5)
    frame2 = Window.frame(FabWindow, fab_root, 5, 5)
    
    sys_name_label = Window.label(FabWindow, frame1, 'Nom du sous systeme:', 0, 0)
    sys_ref_label = Window.label(FabWindow, frame1, 'Reference du sous systeme:', 1, 0)
    s_n_label = Window.label(FabWindow, frame1, 'S N robot:', 2, 0)
    
    sys_name_entry = Window.entry(FabWindow, frame1, 0, 1)
    sys_ref_entry = Window.entry(FabWindow, frame1, 1, 1)
    s_n_entry = Window.entry(FabWindow, frame1, 2, 1)
    
    doc_date_label = Window.label(FabWindow, frame2, 'Date du document:', 0, 0)
    made_by_label = Window.label(FabWindow, frame2, 'Fabriqué par:', 1, 0)
    validated_by_label = Window.label(FabWindow, frame2, 'Verifié par:', 2, 0)
    begin_fab_label = Window.label(FabWindow, frame2, 'Debut de fabrication:', 3, 0)
    end_fab_label = Window.label(FabWindow, frame2, 'Fin de fabrication:',  4, 0)
    
    doc_date_entry = Window.entry(FabWindow, frame2, 0, 1)
    setbyy_entry = Window.entry(FabWindow, frame2, 1, 1)
    validated_by_entry = Window.entry(FabWindow, frame2, 2, 1)
    begin_fab_entry = Window.entry(FabWindow, frame2, 3, 1)
    end_fab_entry = Window.entry(FabWindow, frame2, 4, 1)
    
    fab_val = (str(sys_name_entry.get()), str(sys_ref_entry.get()), str(s_n_entry.get()), str(doc_date_entry.get()), str(setbyy_entry.get()), str(validated_by_entry.get()), str(begin_fab_entry.get()), str(end_fab_entry.get()))
    enter_fab = Window.button(FabWindow, fab_root, bd.fab_commande, fab_val, 2, 45)
    
    fab_root.mainloop()   


config_button_frame = Window.frame(principal_window, root, 10, 11, 'light gray')
install_button_frame = Window.frame(principal_window, root, 30, 11, 'light gray')
fab_button_frame = Window.frame(principal_window, root, 20, 11, 'light gray')

def open_and_save(txt):
    if txt == 'instal':
        install_window()
    elif txt == 'fab':
        fab_window()
    elif txt == 'config':
        config_window()

def save_or_show(txt):
    if txt == 'input':
        config_button = PrincipalWindow.window_button(principal_window, config_button_frame, 'Fiches de configuration', open_and_save, 'config')
        install_button = PrincipalWindow.window_button(principal_window, install_button_frame, 'Fiches d installation', open_and_save, 'instal')
        fab_button = PrincipalWindow.window_button(principal_window, fab_button_frame, 'Fiches de fabrication', open_and_save, 'fab')
    
    elif txt == 'ouput':
        config_button = PrincipalWindow.window_button(principal_window, config_button_frame, 'Fiches de configuration', bd.show, 'config')
        install_button = PrincipalWindow.window_button(principal_window, install_button_frame, 'Fiches d installation', bd.show, 'instal')
        fab_button = PrincipalWindow.window_button(principal_window, fab_button_frame, 'Fiches de fabrication', bd.show, 'fab')

save_button = PrincipalWindow.window_button(principal_window, principal_window.frame3, 'Enregistrer', save_or_show, 'input')
show_button = PrincipalWindow.window_button(principal_window, principal_window.frame4, 'Récupérer', save_or_show, 'output')

root.mainloop()

