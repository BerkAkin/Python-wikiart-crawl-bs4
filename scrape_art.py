import requests, bs4
import shutil
import pandas as pd
import os

#RESSAMLARIN LİSTESİ#
ressamlar=["vincent-van-gogh", "leonardo-da-vinci","caravaggio","claude-monet","gustav-klimt","edvard-munch","salvador-dali","raphael","frida-kahlo","paul-cezanne","paul-gauguin","pablo-picasso"]

#KAYDEDİLEN GÖRÜNTÜLERİ İSİMLENDİRMEK İÇİN SAYAÇ#
sayac=0


for don in ressamlar:
    #SIRAYLA CSV KLASÖRÜNDEKİ CSVLERİ OKUMAK#
    data=pd.read_csv('csv/'+ don +'.csv')
    #CSV ELEMANLARI#
    df=pd.DataFrame(data)
    #GÖRÜNTÜLERİN KAYDEDİLECEĞİ KLASÖRLERİN YERLERİNİ AYARLAMAK#
    newpath = r'images/'+don+'/'
    #CSV SATIRLARINI OKUMAK İÇİN DÖNGÜ BAŞLANGICI#
    for i, row in df.iterrows():
        q = row[don]
        res = requests.get(q)
        res.raise_for_status()
        #CSV İÇİNDEKİ OKUNAN SATIRDAKİ LİNKİ BS4 İLE YAKALAMAK#
        recipeSoup = bs4.BeautifulSoup(res.text, "html.parser")
        type(recipeSoup)
        #YAKALANAN LİNKTEKİ İMG ETİKETLERİNİ İTEMPROP ÖZELLİĞİ OLANA GÖRE ÇEKMEK#
        instructions = recipeSoup.find("img", itemprop="image")
        #KAYDEDİLECEK KLASÖR YOKSA KLASÖR AÇMAK İLK SEFERDE KULLANMAK İÇİN İDEAL#
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        r = requests.get(instructions['src'], stream=True)
        if r.status_code == 200:
            #DOSYAYI OLUŞTURMAK VE ADINI VERMEK#                    
            with open(newpath+str(sayac)+".jpg", 'wb') as f: 
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
                print(sayac , "." , don ,"resmi indirildi")
        sayac+=1
        
      
