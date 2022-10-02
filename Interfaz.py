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
    botonImage.pack()
    

#Mostrar Imagen
def images(boton):
   if boton == 1:   
      botonMain.destroy()
      EditorImagenes().showImage()


botonMain = tkinter.Button(ventana, text = "Comenzar", padx=40, pady=50, command = lambda:main(1))
botonMain.pack()
botonImage = tkinter.Button(ventana, text = "Dibujar", padx=40, pady=50, command= lambda:images(1))


ventana.mainloop()