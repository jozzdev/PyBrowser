#!usr/bin/python

__author__="Jose Diaz - email: jozz.18x@gmail.com"
__date__ ="$04/03/2015 05:55:19 AM$"

from homepage import Homepage
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from urllib.request import urlopen # Interaccion con la web
from urllib.error import HTTPError,URLError # Excepciones


class GuiBrowser(ttk.Frame):
    
    MENUBUTTON = dict(relief=FLAT, bd=0, width=30, height=30, 
                font=("Arial", 11), activebackground="#d6d9db", 
                cursor="hand2")
    ENTRY = dict(relief=FLAT, bd=1, font=("Arial", 11), width=50, 
                highlightbackground="#acb1b4", highlightcolor="#549beb", 
                highlightthickness=1)
    TEXT = dict(font=("Arial",10), cursor='arrow', state='normal', 
                autoseparators=5, spacing1=5, wrap=WORD)
    FONT = ("Arial", 11)
    
    def __init__(self, master):
        """ Contructor."""
        super().__init__(master)
        self.cargar_imagenes()
        self.variables_declarados()
        # Crear todos los widgets.
        self.barra_navegacion = self.crear_barra_navegacion()
        self.separador = Frame(self, bg="#8a9398", height=1)
        self.area_navegacion = self.crear_area_navegacion()
        self.area_detalles = self.crear_area_detalles()
        # Posicionar los widgets.
        self.barra_navegacion.pack(side=TOP, fill=X, expand=True)
        self.separador.pack(side=TOP, fill=X)
        self.area_navegacion.pack(side=TOP, fill=BOTH, expand=True)
        self.area_detalles.pack(side=BOTTOM, fill=X, expand=True)
    
    def cargar_imagenes(self):
        """ Carga todas las imagenes usados en este script."""
        imenu_option = Image.open(r"images\menu_option.png")
        self.imagenMenuOptions = ImageTk.PhotoImage(imenu_option)
        ihome = Image.open(r"images\home.png")
        self.imagenHome = ImageTk.PhotoImage(ihome)
        iprueba = Image.open(r"images\icon_prueba.png")
        self.imagenPrueba = ImageTk.PhotoImage(iprueba)
    
    def variables_declarados(self):
        """ Declaracion de variables. """
        self.var_entry_search_url = StringVar()
        self.var_entry_search_url.set("https://www.python.org/")
    
        
    def crear_barra_navegacion(self):
        """ Crea la barra de navegacion o cabecera del browser implementado con 
            sus widgets internos donde retona el frame principal."""
        barra_browser = Frame(self)
        # Crear widget interno.
        btn_home = Menubutton(barra_browser, image=self.imagenHome, bg=barra_browser['bg'], 
                                **self.MENUBUTTON)
        lb_url = Label(barra_browser, text= 'URL: ', font=(self.FONT[0],10,"bold"), 
                                bg=barra_browser['bg'])
        entry = Entry(barra_browser, textvariable=self.var_entry_search_url, 
                                **self.ENTRY)
        btn_menu = Menubutton(barra_browser, image=self.imagenMenuOptions, bg=barra_browser['bg'], 
                                **self.MENUBUTTON)
        # Posiciona los widgets.
        btn_home.pack(side=LEFT, padx=5, pady=5)
        lb_url.pack(side=LEFT)
        entry.pack(side=LEFT, fill=X, expand=True, pady=5)
        btn_menu.pack(side=RIGHT, padx=5, pady=5)
        # Eventos de los widgets.
        btn_home .bind("<Button-1>", lambda e: self.homepage())
        entry.bind("<Return>", lambda e: self.search_url())
        # Retorna el Frame.
        return barra_browser
    
    def crear_area_navegacion(self):
        """ Crea la area de navegacion o cuerpo del browser implementado con 
            sus widgets internos donde retona el frame principal."""
        area_navegacion = Frame(self)
        # Crear widget interno.
        self.text = Text(area_navegacion, **self.TEXT)
        scroller = ttk.Scrollbar(area_navegacion, command=self.text.yview)
        self.text.config(yscrollcommand=scroller.set)
        # Posiciona los widgets.
        scroller.pack(side=RIGHT, fill=Y)
        self.text.pack(fill=BOTH, expand=True)
        
        self.text.configure(state="disabled")
        # Retorna el Frame.
        return area_navegacion
        
    def crear_area_detalles(self):
        """ Crea un area para los detalles de la pagina consultada implementado 
            con sus widgets internos donde retona el frame principal."""
        area_detalles = Frame(self)
        # Crear widget interno.
        self.text_detalles = Text(area_detalles, **self.TEXT)
        scroller = ttk.Scrollbar(area_detalles, command=self.text_detalles.yview)
        self.text_detalles.config(yscrollcommand=scroller.set)
        # Posiciona los widgets.
        scroller.pack(side=RIGHT, fill=Y)
        self.text_detalles.pack(fill=BOTH, expand=True)
        #Retorna el Frame.
        return area_detalles
        
    def homepage(self):
        homepage = Homepage(self.text)
        homepage.pack(fill=BOTH, expand=True)
        
    def search_url(self):
        """ Metodo para Buscar y obtiener informacion de una url.
            Escribe y muestra los resultados en los widgets
            de Text creados anteriormente."""
        self.text.configure(state="normal")
        try:
            if self.var_entry_search_url.get()=="":
                self.message_estado("Ingrese url de una pagina web.")
            elif self.var_entry_search_url.get()=="https://":
                self.message_estado("Ingrese url de una pagina web.")
            else:
                try:
                    # Muestra los datos de la url el en area de navegacion principal.
                    self.message_estado("Leyendo archivos...")
                    self.text.delete(1.0, END)
                    data =  urlopen(self.var_entry_search_url.get())
                    self.text.insert(INSERT, data.read())
                    # Muestra la url de la pagina en la barra de estado.
                    geturl = data.geturl()
                    self.message_estado(geturl)
                    # Muestra los detalles de la url el en area de detalles.
                    self.text_detalles.configure(state="normal")
                    self.text_detalles.delete(1.0, END)
                    headers = data.info()
                    self.text_detalles.insert(INSERT, headers)
                    self.text_detalles.configure(state="disabled")
                    data.close()
                except URLError as e:
                    msj = "URL Error:",e.reason , self.var_entry_search_url.get()
                    self.message_estado(msj)
                except HTTPError as e:
                    msj = "HTTP Error:",e.code , self.var_entry_search_url.get()
                    self.message_estado(msj)
        except ValueError:
            self.message_estado("Ingrese url valida: Error digitacion: '%s'" %self.var_entry_search_url.get())
        self.text.configure(state="disabled")
    
                    
    def message_estado(self, text):
        """ Muestra un mensaje en la parte inferior de la ventana principal.
            Tiene como parametro el texto del mensaje."""
        msj_estado = Message(self, text=text, bg='#c6dedd', font=("Arial",8), width=1400)
        msj_estado.place(in_=self, relx=0, rely=1, x=0, y=0, anchor="sw", bordermode="outside")
        msj_estado.after(2000,lambda: msj_estado.destroy())
        