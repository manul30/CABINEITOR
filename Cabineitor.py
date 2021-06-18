# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 15:04:15 2021

@author: Manuel
"""
'''
import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk

root=tk.Tk()

canvas=tk.Canvas(root,width=500,height=600)

canvas.grid(columnspan=3,rowspan=3)

#logo
logo=Image.open("CABINEITOR.png")
logo=ImageTk.PhotoImage(logo)
logo_label=tk.Label(image=logo)
logo_label.image=logo
logo_label.grid(column=1, row=0)

#instructions
instructions= tk.Label(root, text="Ingrese su número de DNI:",font="Raleway")
instructions.grid(columnspan=3,column=0,row=1)

#browse button

browse_text=tk.StringVar()
browse_btn=tk.Button(root, textvariable=browse_text, font="Raleway", bg="#212121",fg="white")
browse_text.set("DNI")
browse_btn.grid(column=1, row=2)


root.mainloop()

'''
#Santiago Garcia Arango, 18 Enero 2020
#TKINTER CON POO, MULTIPLES FRAMES CON AYUDA DE CONTAINER
#-----------------------------------------------------------------------------
'''
El objetivo de este codigo, es maximizar la capacidad y uso de nuestra APP, con
ayuda de la alternativa de un MENU, que a su vez nos lleve a diferentes frames.
Cada Frame tendra sus propias funcionalidades y la capacidad de inter-relacionarse.

Ademas, estos metodos van a ser el pilar para creacion de apps mas complejas y con 
mayor cantidad de funcionalidades y ventanas.

Ahora se debe tener muy claro la estrategia de programacion con POO, su relacion, sus
herencias y su forma de relacionarse, porque se complican mas los codigos y es fundamental
tener entendido el efecto de los frames y su efecto en clase de tipo tk.Tk (principal)

METODOLOGIA PARA TENER MULTIPLES FRAMES:
1. Crear todos los frames en clases separadas, con su info y caracteristicas propias...
   nota: como si agregaramos capas de pinturas y se debe elegir cual usar.
   nota: se TIENEN que almacenar estas frames (TODAS) en clase principal de tk.Tk, de lo
         contrario, NO se podran acceder a estas. (dict --> self.frames)
2. Tener claro la interaccion o forma en que se desee pasar entre frames (botones, enters, etc)
   nota: esto es para que se llame a funcion especial de tkinter (ver paso 3)
3. Al querer cambiar de Frame, llamar a funcion "FRAME.tkraise()"... que la poseen todos los
   frames, por lo que se vuelve una manera de "llamar al top" este frame creado previamente.
   nota: se debe acceder a uno de los frames almacenados en dict --> self.frames 
4. Organizar correctamente la logica y estructura, para acceder y jugar entre frames mostradas

'''
#-----------------------------------------------------------------------------
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

import tkinter as tk
from tkinter import ttk
import tkinter.font as font

class APP(tk.Tk):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.configure(bg = "black")

        font.nametofont("TkDefaultFont").configure(size = 12, underline = True)

        self.title("TKINTER CON FRAME Y POO")
        
        self.columnconfigure( 0, weight = 1 )
        self.rowconfigure(0, weight = 1)

        contenedor_principal = tk.Frame( self ,bg = "yellow")
        contenedor_principal.grid( padx = 40, pady = 50 , sticky = "nsew")

        self.todos_los_frames = dict()

        for F in (Frame_1, Frame_2):

            frame = F( contenedor_principal , self)

            self.todos_los_frames[F] = frame

            frame.grid(row = 0, column = 0, sticky = "nsew")
        
        self.show_frame( Frame_1 )

    def show_frame(self,contenedor_llamado):
 
        frame = self.todos_los_frames[contenedor_llamado]
            
        self.bind( "<Return>", frame.saludarme )
        self.bind( "<KP_Enter>", frame.saludarme )

        frame.L_3.configure( text = "" )
        frame.entrada_usuario.set( "" )
        frame.E_1.focus()
        
        frame.tkraise()

class Frame_1(tk.Frame):

    def __init__(self, container, controller,*args, **kwargs):

        super().__init__(container, *args, **kwargs)
        self.configure(bg = "yellow")

        self.entrada_usuario = tk.StringVar()

        L_1 = tk.Label( self, text = "MI PRIMER FRAME CON POO Y TKINTER", font = ("Times New Roman",14,"bold"),bg = "yellow",fg = "blue" )
        L_1.grid(row = 0, column = 0, columnspan = 4, sticky = "n")
        L_2 = tk.Label( self, text = "Ingrese Nombre: ", font = ("Times New Roman",12),bg = "yellow" )
        L_2.grid(row = 1, column = 0, sticky = "w")

        self.E_1 = ttk.Entry( self, textvariable = self.entrada_usuario )
        self.E_1.focus()
        self.E_1.grid(row = 1, column = 1, columnspan = 2, padx = (0,10))

        B_1 = ttk.Button( self, text = "SALUDARME" , command = self.saludarme )
        B_1.grid(row = 1, column = 3, sticky = "e")

        self.L_3 = tk.Label( self, textvariable = "", font = ("Times New Roman",12,"bold"),bg = "yellow" )
        self.L_3.grid(row = 2, column = 0, columnspan = 4, sticky = "nsew")

        B_2 = ttk.Button( self, text = "ingles", command = lambda:controller.show_frame( Frame_2 ) )
        B_2.grid(row = 3, column = 0)

    def saludarme(self, *args):
        self.L_3.configure( text = "Buenos Dias : {}.".format( self.entrada_usuario.get() ) )

class Frame_2(tk.Frame):

    def __init__(self, container,controller,*args, **kwargs):

        super().__init__(container, *args, **kwargs)
        self.configure(bg = "yellow")

        self.entrada_usuario = tk.StringVar()

        L_1 = tk.Label( self, text = "MI FIRST FRAME WITH OOP AND TKINTER", font = ("Times New Roman",14,"bold"),bg = "yellow",fg = "blue" )
        L_1.grid(row = 0, column = 0, columnspan = 4, sticky = "n")
        L_2 = tk.Label( self, text = "Entry name: ", font = ("Times New Roman",12),bg = "yellow" )
        L_2.grid(row = 1, column = 0, sticky = "w")

        self.E_1 = ttk.Entry( self, textvariable = self.entrada_usuario )
        self.E_1.focus()
        self.E_1.grid(row = 1, column = 1, columnspan = 2, padx = (0,10))

        B_1 = ttk.Button( self, text = "SAY HI" , command = self.saludarme )
        B_1.grid(row = 1, column = 3, sticky = "e")

        self.L_3 = tk.Label( self, textvariable = "", font = ("Times New Roman",12,"bold"),bg = "yellow" )
        self.L_3.grid(row = 2, column = 0, columnspan = 4, sticky = "nsew")

        B_2 = ttk.Button( self, text = "espannol", command = lambda:controller.show_frame( Frame_1 ) )
        B_2.grid(row = 3, column = 0)
    
    def saludarme(self, *args):
        self.L_3.configure( text = "Good Morning, {}.".format( self.entrada_usuario.get() ) )


root = APP()

root.mainloop()