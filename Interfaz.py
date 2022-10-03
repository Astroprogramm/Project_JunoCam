import tkinter
from EditorImagenes import *

editor = EditorImagenes()

ventana = tkinter.Tk()
ventana.geometry("700x500")

etiqueta = tkinter.Label(ventana, text = "Editor de Imágenes", bg="gray", width=50, height=5)
etiqueta.grid(row=0, column=0)

etiqueta_brillo = tkinter.Label(ventana, text = "Ajustar brillo", bg="gray", width=10, height=1)
etiqueta_color = tkinter.Label(ventana, text = "Ajustar color", bg="gray", width=10, height=1)
etiqueta_contraste = tkinter.Label(ventana, text = "Ajustar contraste", bg="gray", width=14, height=1)
etiqueta_nitidez = tkinter.Label(ventana, text = "Ajustar nitidez", bg="gray", width=12, height=1)
etiqueta_detalle = tkinter.Label(ventana, text = "Ajustar detalles", bg="gray", width=12, height=1)

#Preparar Ambiente
def main(boton):
   if boton == 1:
    botonMain.destroy()
    botonImage.grid(row=0, column=1)

    botonBrillo.grid(row=0, column=2)
    cajaBrillo.grid(row=2, column=2)
    etiqueta_brillo.grid(row=2, column=1)

    botonColor.grid(row=3, column=2)
    cajaColor.grid(row=5, column=2)
    etiqueta_color.grid(row=5, column=1)

    botonContraste.grid(row=6, column=2)
    cajaContraste.grid(row=7, column=2)
    etiqueta_contraste.grid(row=7, column=1)

    botonNitidez.grid(row=3, column=0)
    cajaNitidez.grid(row=4, column=0)
    etiqueta_nitidez.grid(row=5, column=0)

    botonDetalle.grid(row=6, column=0)
    etiqueta_detalle.grid(row=7, column=0)

#Mostrar Imagen
def images(boton):
   if boton == 1:   
      EditorImagenes().showImage()

#Ajustar Brillo
def ajustarBrillo(boton):
   if boton == 1:
      ajuste = float(getTexto(cajaBrillo))
      EditorImagenes().brightness_adjustment(ajuste)

#Ajustar Color
def ajustarColor(boton):
   if boton == 1:
      ajuste = float(getTexto(cajaColor))
      EditorImagenes().color_adjustment(ajuste)


#Ajustar Contraste
def ajustarContraste(boton):
   if boton == 1:
      ajuste = float(getTexto(cajaContraste))
      EditorImagenes().contrast_adjustment(ajuste)

#Ajustar Nitidez
def ajustarNitidez(boton):
   if boton == 1:
      ajuste = float(getTexto(cajaNitidez))
      EditorImagenes().sharpness_adjustment(ajuste)

#Ajustar Detalles
def ajustarDetalle(boton):
   if boton == 1:
      EditorImagenes().detail_adjustment()

def getTexto(caja):
   text = caja.get()
   return text

botonMain = tkinter.Button(ventana, text = "Menú", width=10, height=5, command= lambda:main(1))
botonImage = tkinter.Button(ventana, text = "Dibujar", width=10, height=5, command= lambda:images(1))
botonBrillo = tkinter.Button(ventana, text = "Ajustar Brillo", width=10, height=5, command= lambda:ajustarBrillo(1))
botonColor = tkinter.Button(ventana, text = "Ajustar Color", width=10, height=5, command= lambda:ajustarColor(1))
botonContraste = tkinter.Button(ventana, text = "Ajustar Contraste", width=14, height=5, command= lambda:ajustarContraste(1))
botonNitidez = tkinter.Button(ventana, text = "Ajustar Nitidez", width=12, height=5, command= lambda:ajustarNitidez(1))
botonDetalle = tkinter.Button(ventana, text = "Ajustar Detalles", width=12, height=5, command= lambda:ajustarDetalle(1))


cajaBrillo = tkinter.Entry(ventana, text="Ajustar brillo")
cajaColor = tkinter.Entry(ventana, text="Ajustar Color")
cajaContraste = tkinter.Entry(ventana, text="Ajustar Contraste")
cajaNitidez = tkinter.Entry(ventana, text="Ajustar Nitidez")

botonMain.grid(row=1, column=0)

ventana.mainloop()