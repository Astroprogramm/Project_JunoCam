#Libraries:
import numpy as np
from matplotlib import image
import matplotlib.pyplot as plt
from PIL import Image,ImageFilter  
from PIL import ImageEnhance  
from PIL.ImageFilter import DETAIL

#Las imagenes se pueden descargar de acá: https://www.missionjuno.swri.edu/junocam/processing
class EditorImagenes:
    def __init__(self):
        #Reading images to numpy arrays:
        self.red = Image.open('Imagenes/JNCE_2021246_36C00061_V01-red.png')
        self.green = Image.open('Imagenes/JNCE_2021246_36C00061_V01-green.png')
        self.blue = Image.open('Imagenes/JNCE_2021246_36C00061_V01-blue.png')
        self.map= Image.open('Imagenes/JNCE_2021246_36C00061_V01-mapprojected.png')
        self.raw_stripes=Image.open('Imagenes/JNCE_2021246_36C00061_V01-raw.png')

        #Combining the images:
        self.imageRGB = np.dstack((self.red, self.green, self.blue))
        #Converting to PIL image:
        self.imageRGB = Image.fromarray(self.imageRGB)

    #Punto 5: Combinacion de los canales de color en orden diferente:
    #Se puede hacer intercambiando los argumentos de la función np.dstack, algo así:
    def color_combinate(self,color1,color2,color3):
        self.imageRGB = np.dstack((color1, color2, color3)) 


    # To show images in prompt of this line:
    def showImage(self):
        plt.imshow(self.imageRGB)
        plt.show()

    #2.  Image processing features like brightness adjustment, color and contrast enhancement, etc.
    #Color 
    
    #Brigtness adjustment:
        # A value of 1.0 will preserve the original image
        # Values 1.0+ will brighten the image
        # A value of 0 will return a pitch-black image
    #An enhancement factor of 0.0 gives a black image. A factor of 1.0 gives the original image.
    def brightness_adjustment(self,factor):
        image = ImageEnhance.Brightness(self.imageRGB)
        final_image= image.enhance(factor)
        #Para mostrar la imagen (sale en un visor de imagenes)
        self.imageRGB.show('Imagen Inicial')
        final_image.show('Imagen Final')
        #Para guardar las imagenes:
        final_image.save('ImagenFinal.png')

    #Color adjustment:
    #An enhancement factor of 0.0 gives a black and white image. A factor of 1.0 gives the original image.
    def color_adjustment(self,factor):
        image =  ImageEnhance.Color(self.imageRGB)
        final_image= image.enhance(factor)
        #Para mostrar la imagen (sale en un visor de imagenes)
        self.imageRGB.show('Imagen Inicial')
        final_image.show('Imagen Final')
        #Para guardar las imagenes:
        final_image.save('ImagenFinal.png')


    # #Contrast adjustment:
    #     A value of 1.0 will preserve the original image
    #     Values 1.0+ will add contrast to the image
    #     A value of 0 will return a solid-gray image
    #An enhancement factor of 0.0 gives a solid grey image. A factor of 1.0 gives the original image.
    def contrast_adjustment(self,factor):
        image =  ImageEnhance.Contrast(self.imageRGB)
        final_image= image.enhance(factor)
        #Para mostrar la imagen (sale en un visor de imagenes)
        self.imageRGB.show('Imagen Inicial')
        final_image.show('Imagen Final')
        #Para guardar las imagenes:
        final_image.save('ImagenFinal.png')

    #Sharpness adjustment:
    #An enhancement factor of 0.0 gives a blurred image, a factor of 1.0 gives the original image, and a factor of 2.0 gives a sharpened image.
    def sharpness_adjustment(self,factor):
        image =  ImageEnhance.Sharpness(self.imageRGB)
        final_image= image.enhance(factor)
        #Para mostrar la imagen (sale en un visor de imagenes)
        self.imageRGB.show('Imagen Inicial')
        final_image.show('Imagen Final')
        #Para guardar las imagenes:
        final_image.save('ImagenFinal.png')

    def detail_adjustment(self):
        final_image=self.imageRGB.filter(DETAIL)
        #Para mostrar la imagen (sale en un visor de imagenes)
        self.imageRGB.show('Imagen Inicial')
        final_image.show('Imagen Final')
        #Para guardar las imagenes:
        final_image.save('ImagenFinal.png')

