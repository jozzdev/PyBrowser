#!usr/bin/python
# -*- coding: utf-8 -*-

 
"""
PyBrowser es un proyecto que busca tener las cualidades de un 
Navegador web donde integra un buscador y una seccion de correo
electronico basico para el usuario.

LIBRERIAS UTILIZADOS:
    -Tkinter
    -urllib
    -Pillow
    -smtplib
    -webbrowser
    
CARACTERISTICAS ACTUALES:
    -Modulo homepage(gui e implementacion de widgets y metodos de busqueda en 
     Google search y envio de correo electronico para de la pagina de inicio 
     y servidor de correo electronico)
    -Modulo browser(gui e implementacion de widgets y metodos de busqueda 
     de url para el mavegador web)
    -Modulo navegador(Modulo Main) - (Gui de todo el contorno del navegador 
     web y ejecutor de todo el proyecto)
     
IMPORTANTE:
    Cabe resaltar que el proyecto aun no esta terminado, cualquier apoyo, ayuda
    o sugerencia para la implementacion es gratamente bienvenido.
"""

__author__ = "Jose Diaz"
__copyright__ = "Copyright (C) 2015, Jose Diaz"
__license__ = "GPL v3.0"
__version__ = "1.1"
__revision__ = "04"
__date__ = "$04/03/2015 07:14:10 AM$"
__status__ = "Desarrollo"
__contact__ = "966403361"
__email__ = "jozz.18x@gmail.com"

from browser import GuiBrowser
from tkinter import *
from tkinter import ttk

class NavegadorWeb(Frame):
    
    MENUBUTTON = dict(relief=FLAT, bd=0, width=12, height=30, 
                font=("Arial", 10), activebackground="#d6d9db", 
                cursor="hand2", fg="#1072bd")
    
    @classmethod
    def main(cls):
        """ Metodo principal."""
        root = Tk()
        root.title('PyBrowser')
        root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth()-6, root.winfo_screenheight()-64)) 
        root.resizable(False, False)
        vista = cls(root)
        vista.pack(fill=BOTH, expand=True)
        root.mainloop()
                
    def __init__(self, master):
        super().__init__(master)
        self.navegador = self.crear_navegador()
        self.navegador.pack(expand=True, fill=BOTH)
        
        
    def crear_navegador(self):
        navegador = ttk.Notebook(self)
        invalida = Frame(navegador)
        self.fr_inicio = Frame(navegador)
        navegador.add(invalida, text=' PyBrowser', padding=-3)
        navegador.add(self.fr_inicio, text=' Google', padding=-3)
        
        btn_cerrar = Menubutton(self, text='Cerrar pestania', **self.MENUBUTTON)
        btn_cerrar.place(in_=navegador, relx=1, anchor="e", y=10, x=-5, bordermode="outside", height=17)
        btn_cerrar.bind("<Button-1>", self.cerrar_pestania)
        
        btn_nuevo = Menubutton(self, text='Nueva pestania', **self.MENUBUTTON)
        btn_nuevo.place(in_=navegador, relx=1, anchor="e", y=10, x=-100, bordermode="outside", height=17)
        btn_nuevo.bind("<Button-1>", self.nueva_pestania)
        
        navegador.tab(invalida, state='disabled') # Desabilita la pestania
        navegador.select(self.fr_inicio) # Abre la pestania Inicio al iniciar
        
        browser = GuiBrowser(self.fr_inicio)
        browser.pack(fill=BOTH, expand=True)
        
        return navegador
    
    def nueva_pestania(self, event=None):
        self.pestania_nuevo = Frame(self.navegador)
        self.navegador.insert('end', self.pestania_nuevo, text=' Nueva Pestania ', padding=-3)
        browser = GuiBrowser(self.pestania_nuevo)
        browser.pack(fill=BOTH, expand=True)
        self.navegador.select(self.pestania_nuevo)
        
    def cerrar_pestania(self, event=None):
        self.navegador.hide(self.pestania_nuevo)
        
if __name__ == "__main__":
    NavegadorWeb.main()
