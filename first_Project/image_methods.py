from PIL import Image
import matplotlib.pyplot as plt

def contactImage(image1,image2,image3,image4):
    newImage =  Image.new("RGB",(image1.width + image2.width + image3.width + image4.width, image1.height))
    newImage.paste(image1,(0,0))
    newImage.paste(image2,(image1.width,0))
    newImage.paste(image3,(image1.width+image2.width,0))
    newImage.paste(image4,(image1.width+image2.width + image3.width,0))
    return newImage


def get_concat_h(image_gray,):
    for n in range(3, 8):
        plt.figure(figsize=(10,10))

        # Sol tarafta orijinal gri tonlama görüntüsü, sağ tarafta quantize edilmiş
        quantized_image = image_gray.quantize(256 // 2 ** n)
        plt.imshow(get_concat_h(image_gray.convert("RGB"), quantized_image.convert("RGB"))) 

        # Başlık ekleyin
        plt.title(f"256 Quantization Levels left vs {256 // 2**n} Quantization Levels right")
        plt.axis('off')  # Eksenleri gizle
        plt.show()