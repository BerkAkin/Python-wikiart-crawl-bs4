from operator import contains
import requests
from bs4 import BeautifulSoup

#ÇEKİLİP CSV'YE YAZILACAK OLAN SANATÇILARIN LİSTESİ#
degisken=["vincent-van-gogh", "leonardo-da-vinci","caravaggio","claude-monet","gustav-klimt","edvard-munch","salvador-dali","raphael","frida-kahlo","paul-cezanne","paul-gauguin","pablo-picasso"]

#LİSTEYİ DÖNMEK#
for don in degisken:
    #LİSTEDEKİ İLK 10 ELEMANI ATLAMAK İÇİN SAYAÇ #
    sayac=0
    #SANATÇILARIN URL BİLGİERİ SABİT, YALNIZCA SANATÇI İSMİ DEĞİŞİYOR BURADA DA DÖNÜLEN LİSTE ELEMANI BASILIP LİNK DEĞİŞKENE ATILIYOR#
    url = 'https://www.wikiart.org/en/'+don+'/all-works/text-list'
    #URL E BAĞLANMAK İÇİN İSTEK OLUŞTURULUYOR#
    r = requests.get(url)
    #BS4 İLE BAĞLANILAN URL PLAIN TEXT OLARAK ALINIP DEGİSKENE ATILIYOR#
    soup = BeautifulSoup(r.text, "html.parser")
    #BULUNULAN DİZİNDE DONÜLÜNEN SANATÇI İSMİYLE BİR DOSYA OLUŞTURULUYOR FORMAT CSV DİL KODLAMASI UTF8#
    with open(don+'.csv', 'w', encoding="utf-8") as f:
        #OLUŞAN CSV YE SANATÇI ADI BAŞLIK OLARAK VERİLİYOR#
        f.write(don+'\n')
        #BS4 İLE ALINAN URL ADRESİ İÇİNDE LİSTE HALİNDE SANATÇININ YAPTIĞI RESİMLER MEVCUT BUNLAR BAŞKA BİR FOR DÖNGÜSÜ İLE ANCHOR ETİKETLERİ BULUNMAK SURETİYLE DÖNÜLÜYOR#
        for a in soup.find_all('a', href=True):
            #BULUNAN LİNKLER ESAS WEB SAYFASININ ADRESİ ÖNÜNE EKLENEREK RESİMLERİN ADRES BİLGİSİ TAMAMLANIYOR#
            link="https://www.wikiart.org"+a['href']
            #BAZI URL TEMİZLEME İŞLEMLERİ#
            if don not in link:
                continue
            elif sayac!=10:
                sayac+=1
                continue
            else:
                #RESİM URL'SİNİ CSV YE YAZMA VE ALT SATIRA GEÇME#
                f.write(link)
                f.write('\n')
    f.close()            
    
