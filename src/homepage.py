
__author__="Jose Diaz - email: jozz.18x@gmail.com"
__date__ ="$04/03/2015 03:55:19 AM$"

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import smtplib #Envio de correos
import webbrowser

class Homepage(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.cargar_imagenes()
        self.cargar_estilos()
        # Crear todos los widgets.
        self.cabecera = self.crear_cabecera()
        self.toolbar = self.crear_toolbar()
        self.cuerpo = self.crear_cuerpo()
        self.btn_flotante = self.crear_btn_flotante()
        # Posicionar los widgets.
        self.cabecera.pack(side=TOP, fill=X)
        self.toolbar.pack(side=LEFT, fill=Y)
        self.cuerpo.pack(side=LEFT, fill=BOTH, expand=True)
    
    def cargar_imagenes(self):
        ibtn= Image.open(r"images\boton.png")
        self.imagenBotton = ImageTk.PhotoImage(ibtn)
        iprueba = Image.open(r"images\icon_prueba.png")
        self.imagenPrueba = ImageTk.PhotoImage(iprueba)
        
    def cargar_estilos(self):
        self.BACKGROUND_MENU = "#20b3ac"
        self.BACKGROUND_TOOLBAR = "#33333b"
        self.FOREGROUND = "#A7FFEB"
        self.FOREGROUND_TOOLBAR = "#B0BEC5"
        self.ACTIVEBACKGROUND = "#1DE9B6"
        self.ACTIVEBACKGROUND_TOOLBAR = "#29282e"
        self.ACTIVEFOREGROUND_TOOLBAR = "#20b3ac"
        self.FONT = ("Arial", 11)
        
      
    def crear_btn_flotante(self):
        boton = Button(self, command=self.ventana_enviar_correo, image=self.imagenBotton, 
                                cursor="hand2", relief=FLAT, bd=0, bg=self.text['bg'], activebackground=self.text['bg'])
        boton.place(in_=self, relx=1, rely=1, x=-50, y=-50, anchor=SE, bordermode="outside")
        # Retorna el Button
        return boton
        
    def crear_cabecera(self):
        frame_cabecera = Frame(self, bg=self.BACKGROUND_MENU)
        # Crear widget interno.
        label = Button(frame_cabecera, text= 'PYBROWSER SEARCH', command=self.abrir_facebook, cursor="hand2", font=(self.FONT[0],11,"bold"), relief=FLAT, bd=0,
                        bg=frame_cabecera['bg'], fg="#FFFFFF", activebackground=frame_cabecera['bg'], activeforeground="#FFFFFF")
        label.pack(side=LEFT, padx=5)
        
        button = Menubutton(frame_cabecera, text='Search', cursor="hand2", relief=FLAT, bd=0, font=self.FONT, bg="TEAL", fg="#FFFFFF", activebackground=self.ACTIVEBACKGROUND, highlightbackground="#166d6d", highlightcolor="#16837e", highlightthickness=1)
        button.pack(side=RIGHT, padx=5, pady=5, ipady=3)
        button.bind("<Button-1>", lambda e: self.search_google())
        
        self.var_entry_search_google = StringVar()
        entry = Entry(frame_cabecera, textvariable=self.var_entry_search_google, font=self.FONT, width=50, relief=FLAT, bd=0, highlightbackground=frame_cabecera['bg'], highlightcolor="TEAL", highlightthickness=1)
        entry.pack(side=RIGHT, fill=X, pady=5, ipady=3)
        entry.bind("<Return>", lambda e: self.search_google())
        
        label = Label(frame_cabecera, text= 'e', font=("Adobe Naskh Medium",20), bg=frame_cabecera['bg'], fg="red")
        label.pack(side=RIGHT)
        label = Label(frame_cabecera, text= 'l', font=("Adobe Naskh Medium",20), bg=frame_cabecera['bg'], fg="green")
        label.pack(side=RIGHT)
        label = Label(frame_cabecera, text= 'g', font=("Adobe Naskh Medium",20), bg=frame_cabecera['bg'], fg="blue")
        label.pack(side=RIGHT)
        label = Label(frame_cabecera, text= 'o', font=("Adobe Naskh Medium",20), bg=frame_cabecera['bg'], fg="yellow")
        label.pack(side=RIGHT)
        label = Label(frame_cabecera, text= 'o', font=("Adobe Naskh Medium",20), bg=frame_cabecera['bg'], fg="red")
        label.pack(side=RIGHT)
        label = Label(frame_cabecera, text= 'G', font=("Adobe Naskh Medium",20), bg=frame_cabecera['bg'], fg="blue")
        label.pack(side=RIGHT)
        
        mnbtn_home = Menubutton(frame_cabecera, text='OTHERS...', cursor="hand2", relief=FLAT, borderwidth=1, height=3, font=self.FONT, fg=self.FOREGROUND, bg=frame_cabecera['bg'], activebackground=self.ACTIVEBACKGROUND)
        mnbtn_home.pack(side=RIGHT)
        mnbtn_atras = Menubutton(frame_cabecera, text='CELEBRITIES', cursor="hand2", relief=FLAT, borderwidth=1, height=3, font=self.FONT, fg=self.FOREGROUND, bg=frame_cabecera['bg'], activebackground=self.ACTIVEBACKGROUND)
        mnbtn_atras.pack(side=RIGHT)
        mnbtn_home = Menubutton(frame_cabecera, text='BUSSINES', cursor="hand2", relief=FLAT, borderwidth=1, height=3, font=self.FONT, fg=self.FOREGROUND, bg=frame_cabecera['bg'], activebackground=self.ACTIVEBACKGROUND)
        mnbtn_home.pack(side=RIGHT)
        mnbtn_refrescar = Menubutton(frame_cabecera, text='SPORTS', cursor="hand2", relief=FLAT, borderwidth=1, height=3, font=self.FONT, fg=self.FOREGROUND, bg=frame_cabecera['bg'], activebackground=self.ACTIVEBACKGROUND)
        mnbtn_refrescar.pack(side=RIGHT)
        mnbtn_siguiente = Menubutton(frame_cabecera, text='NEWS', cursor="hand2", relief=FLAT, borderwidth=1, height=3, font=self.FONT, fg=self.FOREGROUND, bg=frame_cabecera['bg'], activebackground=self.ACTIVEBACKGROUND)
        mnbtn_siguiente.pack(side=RIGHT)
        mnbtn_atras = Menubutton(frame_cabecera, text='HOME', cursor="hand2", relief=FLAT, borderwidth=1, height=3, font=self.FONT, fg=self.FOREGROUND, bg=frame_cabecera['bg'], activebackground=self.ACTIVEBACKGROUND)
        mnbtn_atras.pack(side=RIGHT)
        # Retorna el Frame.
        return frame_cabecera
        
    def crear_toolbar(self):
        frame_toolbar = Frame(self, bg=self.BACKGROUND_TOOLBAR)
        # Crear widget interno.
        btn = Menubutton(frame_toolbar, text=" Favorites", image=self.imagenPrueba, compound=LEFT, cursor="hand2", relief=FLAT, width=180, font=self.FONT, anchor="w", 
                bg=frame_toolbar['bg'], fg=self.FOREGROUND_TOOLBAR, activebackground=self.ACTIVEBACKGROUND_TOOLBAR, activeforeground=self.ACTIVEFOREGROUND_TOOLBAR)
        btn.pack(fill=X, pady=1)
        separador = Frame(frame_toolbar, bg="#3b464c", height=1)
        separador.pack(fill=X)
        btn = Menubutton(frame_toolbar, text=" Events", image=self.imagenPrueba, compound=LEFT, cursor="hand2", relief=FLAT, width=180, font=self.FONT, anchor="w", 
                bg=frame_toolbar['bg'], fg=self.FOREGROUND_TOOLBAR, activebackground=self.ACTIVEBACKGROUND_TOOLBAR, activeforeground=self.ACTIVEFOREGROUND_TOOLBAR)
        btn.pack(fill=X)
        separador = Frame(frame_toolbar, bg="#3b464c", height=1)
        separador.pack(fill=X)
        btn = Menubutton(frame_toolbar, text=" Comunity", image=self.imagenPrueba, compound=LEFT, cursor="hand2", relief=FLAT, width=180, font=self.FONT, anchor="w", 
                bg=frame_toolbar['bg'], fg=self.FOREGROUND_TOOLBAR, activebackground=self.ACTIVEBACKGROUND_TOOLBAR, activeforeground=self.ACTIVEFOREGROUND_TOOLBAR)
        btn.pack(fill=X)
        separador = Frame(frame_toolbar, bg="#3b464c", height=1)
        separador.pack(fill=X)
        btn = Menubutton(frame_toolbar, text=" Documentation", image=self.imagenPrueba, compound=LEFT, cursor="hand2", relief=FLAT, width=180, font=self.FONT, anchor="w", 
                bg=frame_toolbar['bg'], fg=self.FOREGROUND_TOOLBAR, activebackground=self.ACTIVEBACKGROUND_TOOLBAR, activeforeground=self.ACTIVEFOREGROUND_TOOLBAR)
        btn.pack(fill=X)
        separador = Frame(frame_toolbar, bg="#3b464c", height=1)
        separador.pack(fill=X)
        btn_recordatorio = Menubutton(frame_toolbar, text=" Stories", image=self.imagenPrueba, compound=LEFT, cursor="hand2", relief=FLAT, width=180, font=self.FONT, anchor="w", 
                bg=frame_toolbar['bg'], fg=self.FOREGROUND_TOOLBAR, activebackground=self.ACTIVEBACKGROUND_TOOLBAR, activeforeground=self.ACTIVEFOREGROUND_TOOLBAR)
        btn_recordatorio.pack(fill=X)
        separador = Frame(frame_toolbar, bg="#3b464c", height=1)
        separador.pack(fill=X)
        btn_contactos = Menubutton(frame_toolbar, text=" About", image=self.imagenPrueba, compound=LEFT, cursor="hand2", relief=FLAT, width=180, font=self.FONT, anchor="w", 
                bg=frame_toolbar['bg'], fg=self.FOREGROUND_TOOLBAR, activebackground=self.ACTIVEBACKGROUND_TOOLBAR, activeforeground=self.ACTIVEFOREGROUND_TOOLBAR)
        btn_contactos.pack(fill=X)
        separador = Frame(frame_toolbar, bg="#3b464c", height=1)
        separador.pack(fill=X)
        # Retorna el Frame.
        return frame_toolbar
        
    def crear_cuerpo(self):
        frame_cuerpo = Frame(self)
        # Crear widget interno.
        self.text = Text(frame_cuerpo, font=("Arial",10), cursor='arrow', state='normal', autoseparators=5, spacing1=5, wrap=WORD, bg="#f9f9f9")
        scroller = ttk.Scrollbar(frame_cuerpo, command=self.text.yview)
        self.text.config(yscrollcommand=scroller.set)
        scroller.pack(side=RIGHT, fill=Y)
        self.text.pack(fill=BOTH, expand=True)
        self.text.configure(state="disabled")
        # Retorna el Frame.
        return frame_cuerpo
        
        
    def search_google(self):
        if self.var_entry_search_google.get() != "":
            google = self.var_entry_search_google.get()
            webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s' % google)
        else:
            pass
        
    def abrir_facebook(self):
        url = 'https://www.facebook.com/jozz.diaz.m'
        webbrowser.open_new_tab(url)
        
            
    def ventana_enviar_correo(self):
        top_enviar_correo = Toplevel(self)
        top_enviar_correo.overrideredirect(True)
        top_enviar_correo.geometry("600x420+420+150")
        top_enviar_correo.focus_set()
        #top_enviar_correo.grab_set()
        
        top_enviar_correo.bind("<Escape>", lambda e: top_enviar_correo.destroy())
        
        frame = Frame(top_enviar_correo, highlightbackground="dark gray", highlightthickness=1)
        frame.pack(fill=BOTH, expand=True)
        frame.bind("<FocusOut>", lambda e: top_enviar_correo.destroy())
        
        fr_superior = Frame(frame, bg=self.BACKGROUND_MENU)
        fr_superior.pack(side=TOP, fill=X)
        fr_inferior = Frame(frame)
        fr_inferior.pack(side=BOTTOM, fill=X)
        fr_to = Frame(frame, bg="#FFFFFF")
        fr_to.pack(side=TOP, fill=X)
        Frame(frame, bg="dark gray", height=1).pack(fill=X)
        fr_from = Frame(frame, bg="#FFFFFF")
        fr_from.pack(side=TOP, fill=X)
        #separador = Frame(frame, bg="dark gray", height=1).pack(fill=X, pady=2)
        fr_mensaje = Frame(frame)
        fr_mensaje.pack(side=TOP, fill=BOTH)
        
        Label(fr_superior, text="New Message", font=(self.FONT[0], 12), justify="left", anchor="w", height=2, bg=fr_superior['bg'], fg="#FFFFFF").pack(side=LEFT, padx=5)
        
        Label(fr_to, text="To", font=(self.FONT[0], 10, "bold"), justify="left", anchor="w", width=5, height=2, bg=fr_to['bg']).pack(side=LEFT, padx=5)
        self.var_entry_to = StringVar()
        entry_to = Entry(fr_to, textvariable=self.var_entry_to, relief=FLAT, bd=1)
        self.var_entry_to.set("Example@email.dominio")
        entry_to .pack(side=LEFT, fill=X, expand=True, anchor=W, padx=10, pady=5)
        entry_to.focus_set()
        entry_to.bind("<Enter>", self.var_entry_to.set(""))
        entry_to.bind("<Enter>", self.var_entry_to.set("Example@email.dominio"), entry_to.config(fg="#546E7A"))
        entry_to.bind('<FocusIn>', lambda evt: self.var_entry_to.set(""), entry_to.config(fg="#000000"))
        entry_to.bind('<FocusOut>', lambda evt: self.var_entry_to.set("Example@email.dominio"),entry_to.config(fg="#546E7A"))
        
        Label(fr_from, text="From", font=(self.FONT[0], 10, "bold"), justify="left", anchor="w", width=5, height=2, bg=fr_from['bg']).pack(side=LEFT, padx=5)
        self.var_entry_from = StringVar()
        entry_from  = Entry(fr_from, textvariable=self.var_entry_from, relief=FLAT, bd=1)
        self.var_entry_from.set("Example@email.dominio")
        entry_from .pack(side=LEFT, fill=X, expand=True, anchor=W, padx=10, pady=5)
        entry_from.bind("<Enter>", self.var_entry_from.set(""))
        entry_from.bind("<Enter>", self.var_entry_from.set("Example@email.dominio"), entry_from.config(fg="#546E7A"))
        entry_from.bind('<FocusIn>', lambda evt: self.var_entry_from.set(""), entry_from.config(fg="#000000"))
        entry_from.bind('<FocusOut>', lambda evt: self.var_entry_from.set("Example@email.dominio"), entry_from.config(fg="#546E7A"))
        
        self.mensaje = Text(fr_mensaje, font=self.FONT, state='normal', autoseparators=5, spacing1=5, wrap=WORD)
        self.mensaje.pack(fill=BOTH, expand=True)
        
        btn_send = Button(fr_inferior, text="Send", command=self.enviar_correo, cursor="hand2", font=self.FONT, relief=FLAT, bd=0, width=10, bg=self.BACKGROUND_MENU, fg="#FFFFFF")
        btn_send.pack(side=RIGHT, padx=10, pady=5)
    
    def enviar_correo(self):
        if self.var_entry_to.get()=="" and self.var_entry_from.get()=="":
            self.message_estado("Ingrese campos requeridos para el envio.")
        elif self.var_entry_to.get()=="Example@email.dominio" or self.var_entry_from.get()=="Example@email.dominio":
            self.message_estado("Ingrese campos requeridos para el envio.")
        else:
            try:
                server = smtplib.SMTP('smtp.gmail.com:587') #localhost
                server.sendmail(self.var_entry_to.get(), self.var_entry_from.get(), self.mensaje.get(0.0, END))
                server.quit()
            except ConnectionRefusedError as e:
                msj = "No se puede establecer una conexion ya que el equipo de destino denego expresamente dicha conexion"
                self.message_estado(msj)
                
    def message_estado(self, text):
        """ Muestra un mensaje en la parte inferior de la ventana principal.
            Tiene como parametro el texto del mensaje."""
        msj_estado = Message(self, text=text, bg='#c6dedd', font=("Arial",8), width=1400)
        msj_estado.place(in_=self, relx=0, rely=1, x=0, y=0, anchor="sw", bordermode="outside")
        msj_estado.after(2000,lambda: msj_estado.destroy())