from windows import *
from database import *
from setWindow import *


class ViewDataWindow (Window):
    '''
    window to show data
    inherites from Window
    '''
    db = DataBase()

    def get_config4G(self):
        c = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        self.master.title('Fiche de configuration du module 4G')
        labels = ['Version du robot']
        labels.extend(EnterDataWindow.fourG_labels)
        labels.extend(EnterDataWindow.config_labels)
        self.create_table(c, 2420, 75, 220, labels, DataBase.get_4G(self.db))


    def get_configCam(self):
        c = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        self.master.title('Fiche de configuration de la caméra optique')
        labels = ['Version du robot']
        labels.extend(EnterDataWindow.cam_labels)
        labels.extend(EnterDataWindow.config_labels)
        self.create_table(c, 2420, 75, 220, labels, DataBase.get_Cam(self.db))


    def get_configControl(self):
        c = (0, 1, 2, 3, 4, 5, 6, 7, 8)
        self.master.title('Fiche de configuration du controlleur')
        labels = ['Version du robot']
        labels.extend(EnterDataWindow.control_labels)
        labels.extend(EnterDataWindow.config_labels)
        self.create_table(c, 2000, 90, 220, labels, DataBase.get_configControl(self.db))


    def get_installImg(self):
        c = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        self.master.title('''Fiche d'installation de l'image disque''')
        labels = ['Version du robot']
        labels.extend(EnterDataWindow.img_labels)
        labels.extend(EnterDataWindow.install_labels)
        self.create_table(c, 2200, 85, 220, labels, DataBase.get_Img(self.db))


    def get_installControl(self):
        c = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        self.master.title('Fiche de configuration du module 4G')
        labels = ['Version du robot']
        labels.extend(EnterDataWindow.control_labels)
        labels.extend(EnterDataWindow.install_labels)
        self.create_table(c, 2200, 85, 220, labels, DataBase.get_installControl(self.db))


    def get_fab(self):
        c = (0, 1, 2, 3, 4, 5, 6, 7)
        self.master.title('Fiche de fabrication des sous systèmes')
        labels = ['Version du robot']
        labels.extend(EnterDataWindow.fab_labels)
        self.create_table(c, 1600, 100, 200, labels, DataBase.get_fab(self.db))


    def create_table(self, clmns , x, w, minw, labels = [] , data = []):
        self.frame = Frame(self.master)
        self.canvas=Canvas(self.frame, bg = 'grey94', width = 830, scrollregion = (0, 0, x, 0))
        self.table = ttk.Treeview(self.canvas, columns = clmns, show = 'headings')
        self.hbar = Scrollbar(self.frame, orient = HORIZONTAL)
        self.hbar.pack(side = BOTTOM, fill = X)
        self.hbar.config(command = self.table.xview)
        self.canvas.config(xscrollcommand = self.hbar.set)
        i = 0
        for label in labels:
            self.table.column(i, stretch = 1, width = w, minwidth = minw)
            self.table.heading(i, text = label)
            i += 1
        for x in data:
            self.table.insert('', index = 'end', values = x)
        self.frame.pack(expand = True)
        self.table.place(x = 10, y = 0)
        self.canvas.pack()
        self.table.column(stretch = 1, width = w, minwidth = minw)