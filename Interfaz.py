import tkinter
from EditorImagenes import *

editor = EditorImagenes()

ventana = tkinter.Tk()
ventana.geometry("450x300")

#etiqueta = tkinter.Label(ventana, text = "Editor de Imágenes", bg="gray")
#etiqueta.pack(fill = tkinter.BOTH, expand = False)


#Preparar Ambiente
def main(boton):
   if boton == 1:
    botonMain.destroy()
    botonImage.pack()
    botonBrillo.pack()
    

#Mostrar Imagen
def images(boton):
   if boton == 1:   
      EditorImagenes().showImage()

#Ajustar Brillo
def ajustarBrillo(boton):
   if boton == 1:
      ajuste = int(getTexto())
      EditorImagenes().brightness_adjustment(ajuste)

def getTexto():
   text = cajaTexto.get()
   return text

botonMain = tkinter.Button(ventana, text = "Comenzar", padx=40, pady=50, command = lambda:main(1))
botonMain.pack()

botonImage = tkinter.Button(ventana, text = "Dibujar", padx=40, pady=50, command= lambda:images(1))

botonBrillo = tkinter.Button(ventana, text = "Ajustar Brillo", padx=40, pady=50, command= lambda:ajustarBrillo(1))

cajaTexto = tkinter.Entry(ventana)
cajaTexto.pack()

ventana.mainloop()