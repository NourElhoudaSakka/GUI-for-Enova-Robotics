from tkinter import *
from principalWindow import *
from setWindow import *
from getWindow import *


def create_set_config():
    set_config_root = Toplevel()
    SetConfigWindow = EnterDataWindow(set_config_root)
    SetConfigWindow.set_config()


def create_get_config4G():
    get_config_root = Toplevel()
    GetConfigWindow = ViewDataWindow(get_config_root)
    GetConfigWindow.get_config4G()


def create_get_configCam():
    get_config_root = Toplevel()
    GetConfigWindow = ViewDataWindow(get_config_root)
    GetConfigWindow.get_configCam()


def create_get_configControl():
    get_config_root = Toplevel()
    GetConfigWindow = ViewDataWindow(get_config_root)
    GetConfigWindow.get_configControl()


def create_set_install():
    set_install_root = Toplevel()
    SetInstallWindow = EnterDataWindow(set_install_root)
    SetInstallWindow.set_install()


def create_get_installImg():
    get_install_root = Toplevel()
    GetInstallWindow = ViewDataWindow(get_install_root)
    GetInstallWindow.get_installImg()


def create_get_installControl():
    get_install_root = Toplevel()
    GetInstallWindow = ViewDataWindow(get_install_root)
    GetInstallWindow.get_installControl()


def create_set_fab():
    set_fab_root = Toplevel()
    SetFabWindow = EnterDataWindow(set_fab_root)
    SetFabWindow.set_fab()


def create_get_fab():
    get_fab_root = Toplevel()
    GetFabWindow = ViewDataWindow(get_fab_root)
    GetFabWindow.get_fab()


def config_choose():
    Window.button(PrincipalWindow, root, create_get_config4G, 480, 320, 'Modules 4G')
    Window.button(PrincipalWindow, root, create_get_configCam, 495, 355, 'Caméra')
    Window.button(PrincipalWindow, root, create_get_configControl, 485, 390, 'Controlleur')


def install_choose():
    Window.button(PrincipalWindow, root, create_get_installImg, 675, 320, 'Image disque')
    Window.button(PrincipalWindow, root, create_get_installControl, 675, 355, 'Controlleur')


def save_or_show(param):
    if param == 'config':
        Window.button(PrincipalWindow, root, create_set_config, 400, 280, 'Enregistrer')
        Window.button(PrincipalWindow, root, config_choose, 485, 280, 'Récupérer')
    elif param == 'install':
        Window.button(PrincipalWindow, root, create_set_install, 590, 280, 'Enregistrer')
        Window.button(PrincipalWindow, root, install_choose, 675, 280, 'Récupérer')


def hard_or_soft(param):
    if param == 'hard':
        Window.button(PrincipalWindow, root, create_set_fab, 185, 230, 'Enregistrer')
        Window.button(PrincipalWindow, root, create_get_fab, 270, 230, 'Récupérer')
    if param == 'soft':
        Window.button_with_param(PrincipalWindow, root, save_or_show, 'config', 410, 230, 'Fiches de configuration', 'sea green')
        Window.button_with_param(PrincipalWindow, root, save_or_show, 'install', 610, 230, """Fiches d'installation""", 'sea green')

root = Tk()
principal_window = PrincipalWindow(root)
Window.button_with_param(PrincipalWindow, root, hard_or_soft, 'hard', 170, 180, 'Hardware (Fiches de fabrication)')
Window.button_with_param(PrincipalWindow, root, hard_or_soft, 'soft', 550, 180, 'Software')
root.mainloop()