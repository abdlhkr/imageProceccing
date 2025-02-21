from PIL import Image
from PIL import ImageOps 
import numpy as np
import os
import image_methods

# dosya yolu verirken r kullanırsak raw string olur ve \ işaretini algılamaz
# bu şekilde invalid escape sequence warning almamış oluruz
my_image = r'images\image1.jpg'
img1 = Image.open(r"images\image2.jpg")
img2 = Image.open(r"images\image3.jpg")

image4 = Image.open(my_image)

print(img1.size)
print(img1.format)
print(img1.mode)

# img1.show()
print(image4.size)
print(image4.format)
print(image4.mode)
cwd = os.getcwd()
print(cwd)
image_path = os.path.join(cwd, my_image)
# ben ona relative path verdim o bana absolute path verdi
print(image_path)
# contacted_image = image_methods.contactImage(img1,img2)
# bu metodu dört resim için değiştirdim
# contacted_image.show()

# load metodu ile resmin pixel değerlerine ulaşabiliriz
# intensity olarak adlandırılan bir tuple döner
# intensity = (r,g,b)
# siyah beyaz resimde 0-255 arasında bir değer döner

pixel_of_image = img1.load() # load metodu pixelAxess dçner
print(pixel_of_image[0,0])

img1.save(r"images\image1_cpy.png")


image_gray = ImageOps.grayscale(img1)
# direk basit mantık resmi siyah beyaz yapıyor
# image_gray.show()
# siyah beyaz bi resimde 0 yaklaştıkça daha koyu olur
print(image_gray.size)
print(image_gray.format) # format olarak none döner
""" PIL (Pillow) kütüphanesinde, bir görüntü nesnesinin 
.format özelliği yalnızca Image.open() ile açılan dosyalar için format
bilgisini saklar. Eğer bir görüntü yeni oluşturulmuş veya dönüştürülmüşse,
.format None döner.  """
print(image_gray.mode)
# L modeu siyah beyaz resimlerde kullanılır
# renkli resimlerde RGB modeu kullanılır
image_gray.save(r"images\image1_gray.png")

## quantize metodu remin renklerini azaltır
# 256 renk varsa 128 renk yapılabilir mesela şimdi 256 
# renkten oluşan imagı sadece siyah beyaz bi image halime getireceğim

siyah_beyaz = image_gray.quantize(2) 
# burdaki iki sayısı orjinale 256 yaklaştıkça dosya boyutu artar
# siyah_beyaz.show()
print(siyah_beyaz.mode) #L siyah beyazdı P 1 bit ya siyah ya beyaz olur


img3 = Image.open(r"images\profil.jpg")
# img3.show()
red, green, blue = img3.split()
contacted_image = image_methods.contactImage(image1=img3,image2=red,image3=green,image4=blue)
contacted_image.show()