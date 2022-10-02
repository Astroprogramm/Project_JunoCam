#Libraries:
import numpy as np
from matplotlib import image
import matplotlib.pyplot as plt
from PIL import Image,ImageFilter  
from PIL import ImageEnhance  

#to download images from URL:
from PIL import Image
from urllib.request import urlopen

# Point 1: download images from URL:
#Revisé las urls de las imagenes pero son muy largas, no veo bien cómo automatizarlo,
# o se puede escoger por ahora digamos 5 fotos
#Las imagenes se pueden descargar de acá: https://www.missionjuno.swri.edu/junocam/processing
class EditorImagenes:
    def __init__(self):
        self.url = "https://python-pillow.org/images/pillow-logo.png"
        self.img = Image.open(urlopen(self.url))

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
    from PIL import ImageFilter
    from PIL.ImageFilter import DETAIL
    #Brigtness adjustment:
        # A value of 1.0 will preserve the original image
        # Values 1.0+ will brighten the image
        # A value of 0 will return a pitch-black image
    #An enhancement factor of 0.0 gives a black image. A factor of 1.0 gives the original image.
    def brightness_adjustment(imagen,factor):
        image = ImageEnhance.Brightness(imagen)
        final_image= image.enhance(factor)
        #Para mostrar la imagen (sale en un visor de imagenes)
        final_image.show()
        #Para guardar las imagenes:
        final_image.save()

    #Color adjustment:
    #An enhancement factor of 0.0 gives a black and white image. A factor of 1.0 gives the original image.
    def color_adjustment(imagen,factor):
        image =  ImageEnhance.Color(imagen)
        final_image= image.enhance(factor)
        #Para mostrar la imagen (sale en un visor de imagenes)
        final_image.show()
        #Para guardar las imagenes:
        final_image.save()


    # #Contrast adjustment:
    #     A value of 1.0 will preserve the original image
    #     Values 1.0+ will add contrast to the image
    #     A value of 0 will return a solid-gray image
    #An enhancement factor of 0.0 gives a solid grey image. A factor of 1.0 gives the original image.
    def contrast_adjustment(imagen,factor):
        image =  ImageEnhance.Contrast(imagen)
        final_image= image.enhance(factor)
        #Para mostrar la imagen (sale en un visor de imagenes)
        final_image.show()
        #Para guardar las imagenes:
        final_image.save()

    #Sharpness adjustment:
    #An enhancement factor of 0.0 gives a blurred image, a factor of 1.0 gives the original image, and a factor of 2.0 gives a sharpened image.
    def sharpness_adjustment(imagen,factor):
        image =  ImageEnhance.Sharpness(imagen)
        final_image= image.enhance(factor)
        #Para mostrar la imagen (sale en un visor de imagenes)
        final_image.show()
        #Para guardar las imagenes:
        final_image.save()

    def detail_adjustment(imagen):
        final_image=imagen.filter(DETAIL)
        #Para mostrar la imagen (sale en un visor de imagenes)
        final_image.show()
        #Para guardar las imagenes:
        final_image.save()


    #sharpness_adjustment(imageRGB,1.0)     #OK
    #brightness_adjustment(imageRGB,2.0)    #OK
    #color_adjustment(imageRGB,1.7)         #OK
    #contrast_adjustment(imageRGB,0.5)      #OK
    #detail_adjustment(imageRGB)            #OK

    #El punto 6 se puede hacer porque tenemos guardada la imagen original en las funciones como imagen, y la imagen modificada es final_image