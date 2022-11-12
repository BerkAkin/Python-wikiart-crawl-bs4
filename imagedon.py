import PIL
import os
import os.path
from PIL import Image, ImageOps
from PIL import ImageFilter

#KLASÖR İSİMLERİ#
klasorler=["caravaggio","claude-monet","edvard-munch","frida-kahlo","gustav-klimt","leonardo-da-vinci","pablo-picasso","paul-cezanne","paul-gauguin","raphael","salvador-dali","vincent-van-gogh"]
for i in klasorler:
    #KLASÖRLER İÇİNDE GÖRÜNTÜLERİ DÖNMEK#
    f = r'c://Users/berka/Desktop/scrap/images/'+ i
    for file in os.listdir(f):
        try:
            #ALGORİTMA GÖRÜNTÜYÜ BULABİLSİN DİYE 
            f_img = f+"/"+file
            img = Image.open(f_img)
            #GÖRÜNTÜ BOYUTUNU 200X200 YAPIP KAYDETMEK#
            img = img.resize((200,200))
            img = ImageOps.grayscale(img)
            img = img.filter(ImageFilter.SHARPEN)
            img.save(f_img)
        except:
            print("Görüntü Değiştirilemedi")
