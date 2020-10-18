from windows import *
import re


class PrincipalWindow (Window):
    '''
    inherites from Window
    '''
    
    version = 'a'
    def __init__(self, master):
        Window.__init__(self, master)
        self.configure_gui()
        


    def configure_gui(self):
        Window.configure_gui(self)
        info = """Bienvenue dans cette interface graphique qui vous permettra d'enregistrer ou obtenir des données du robot PearlGuard! \nPour commencer, veuillez saisir la version S N du robot. \nEn suite, en appuyant sur les boutons ci-dessous, vous pouvez choisir entre la partie 'hardware' qu'on enregistre dans les fiches de fabrication ou la partie software du robot où on trouve les fiches de configuration et les fiches d'installation. \nDeux autres boutons s'afficheront par la suite. \nSi vous souhaitez faire entrer des informations dans la base de données du robot, il suffit de cliquer sur enregistrer. \nEn cas contraire, veuillez cliquer sur récupérer pour visualiser les informations de la base de données. """
        self.master.title('Fenetre principale')
        Window.info_button(self, self.master, 100, 110, info) 
        Window.label(self, self.master,'Version du robot', 180, 110)
        self.entry = Window.entry(self, self.master, 420, 110)
        self.entry['width'] = 39
        self.entry.insert(END, 'PGV--- ------- --')
        self.tick_button_func()
    

    def tick_button_func(self):
        self.photo = Image.open(r'C:\Users\Asus\Documents\GitHub\Enova-Application\packages\tick.png')
        self.photo = self.photo.resize((20,20), Image.ANTIALIAS)
        self.photo_tick = ImageTk.PhotoImage(self.photo)
        self.tick_button = Button(self.master, command= self.commande, image = self.photo_tick)
        self.tick_button.place(x= 790, y = 109)
    
    
    def commande(self):
        if not re.search("^PGV[0-9]{3} [0-9]{7} [0-9]{2}$", self.entry.get()):
            messagebox.showerror("Erreur", "Le format de la version du robot que vous avez inséré est incorrect\nVeuillez respecter le format demandé")
        else:
            PrincipalWindow.version = self.entry.get()
        self.tick_button['state'] = DISABLED