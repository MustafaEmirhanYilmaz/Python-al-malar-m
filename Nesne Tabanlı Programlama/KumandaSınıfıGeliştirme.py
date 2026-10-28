import random
import time
class Kumanda():

    def __init__(self,tv_durumu="Kapalı",tv_ses=0,kanal_listesi=["TRT"],kanal="TRT"):

        self.tv_durumu=tv_durumu

        self.tv_ses=tv_ses

        self.kanal_listesi=kanal_listesi

        self.kanal=kanal

    def tv_ac(self):

        if self.tv_durumu=="Açık":
            print("Televizyon Açık")

        else:
            print("Televizyon Açılıyor")
            self.tv_durumu=="Açık"
    def tv_kapa(self):

        if self.tv_durumu=="Kapalı":
            print("Televizyon Kapalı")

        else:
            print("Televizyon Açılıyor")
            self.tv_durumu=="Açık"
    def ses_ayarlari(self):
        while True:
            cevap=input("Sesi Azalt: '<' , Sesi Arttır: '>' Çıkış: Çıkış ")

            if cevap =="<":
                if self.tv_ses !=0:
                    self.tv_ses-=1
                    print("ses:",self.tv_ses)
            elif cevap ==">":
                if self.tv_ses!=32:
                    self.tv_ses+=1
                    print("ses:", self.tv_ses)
            else:
                print("Ses Güncellendi",self.tv_ses)
                break
    def kanal_ekle(self,kanal_ismi):

        print("Kanal Ekleniyor")
        time.sleep(1)
        self.kanal_listesi.append(kanal_ismi)
        print("Kanal Eklendi")
    def rastgele_kanal(self):

        rastgele=random.randint(0,len(self.kanal_listesi)-1)

        self.kanal=self.kanal_listesi(rastgele)

        print("Şuan ki Kanal:",self.kanal)
    def __len__(self):
        return len(self.kanal_listesi)
    def __str__(self):

        return "Tv Durumu: {},Tv Ses: {},Kanal Listesi : {}, Şuan ki Kanal: {}".format(self.tv_durumu,self.tv_ses,self.kanal_listesi,self.kanal)

kumanda=Kumanda()
print("""
Televizyon Uygulaması


1. TV Aç
2.Tv Kapat
3.Ses Ayarları
4.Kanal Ekle
5.Kanal Sayısı Bilgi
6.Rastgele Kanala Geçme
7.TV Bilgileri
Çıkmak için "q" ya basın.

""")

while True:
    işlem=input("İşlemi Seçiniz")
    if işlem == "q":
        print("Program Sonlandırılıyor.")
        break
    elif işlem == "1":
        kumanda.tv_ac
    elif işlem=="2":
        kumanda.tv_kapa
    elif işlem=="3":
        kumanda.ses_ayarlari
    elif işlem=="4":
        kanal_isimleri=input("Kanal İsimlerini virgül ile ayırarak giriniz.")

        kanal_listesi=kanal_isimleri.split(",")

        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)
    elif işlem =="5":

        print("Kanal Sayısı:",len(kumanda))
    elif işlem=="6":

        kumanda.rastgele_kanal
    elif işlem =="7":

        print(kumanda)
    else:
        print("Geçersiz İşlem")

            
