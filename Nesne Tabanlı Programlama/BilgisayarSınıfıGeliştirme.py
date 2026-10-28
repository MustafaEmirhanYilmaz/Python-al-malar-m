import time


class Bilgisayar:
    def __init__(self,bilgisayar_durumu="Kapalı",ses =0, internet_durumu="Bağlantı Yok",bluetooth="Kapalı" ):
        self.bilgisayar_durumu=bilgisayar_durumu
        self.ses=ses
        self.internet_durumu=internet_durumu
        self.bluetooth=bluetooth


    def pc_ac(self):
        if self.bilgisayar_durumu=="Açık":
            print("Bilgisayar Zaten Açık")
        else:
            print("Bilgisayar Açılıyor")
            self.bilgisayar_durumu="Açık"

    def pc_kapa(self):
        if self.bilgisayar_durumu=="Açık":
            print("Bilgisayar Açık ")
        else:
            print("Bilgisayar Kapatılıyor")
            self.bilgisayar_durumu="Kapalı"

    def ses_ac(self):
        while True:
            if self.ses==32:
                print("Ses Maksimum Düzeyde")
                print("Ses:", self.ses)
                break
            else:
                print("Ses Arttırılıyor...")
                time.sleep(1)
                self.ses+=1
                print("Ses:",self.ses)
                
    def ses_kapa(self):
        while True:
            if self.ses==0:
                print("Ses Minimum Düzeyde.")
                print("Ses:", self.ses)
                break
            else:
                print("Ses azaltılıyor...")
                time.sleep(1)
                self.ses-=1
                print("Ses:",self.ses)
                
    def baglantı(self):
        if self.internet_durumu == "Bağlı":
            print("İnternete Zaten Bağlısınız.")
        else:
            sifre = int(input("Lütfen Şifreyi Giriniz (Şifre: 123): "))
            if sifre == 123:
                time.sleep(1)
                print("İnternete Bağlandınız.")
                self.internet_durumu = "Bağlı"
            else:
                time.sleep(1)
                print("Yanlış Şifre Girildi. Lütfen Tekrar Deneyiniz.")
                
    def bluetooth_baglanti(self):
        if self.bluetooth=="Açık":
            print("Bluetooth Açık")
        else:
            print("Bluetooth Kapalı Lütfen Bluetooth açın.")

print("""
Bilgisayara Hoşgeldiniz
1.Bilgisayarı Aç
2.Bilgisayarı Kapa
3.Ses Aç
4.Ses Kapa
5.İnternete Bağlan (şifre=123)
6.Bluetooth aç
""")
bilgisayar1=Bilgisayar()
işlem=int(input("Lütfen Yapmak İstediğiniz İşlemi Girin:"))

if işlem==1:
    bilgisayar1.pc_ac()
    print("Bilgisayar Açılıyor.")
elif işlem==2:
    bilgisayar1.pc_kapa()
    print("Bilgisayar Kapatılıyor.")
elif işlem==3:
    bilgisayar1.ses_ac()
    print("Ses Açılıyor")
elif işlem==4:
    bilgisayar1.ses_kapa()
    print("Ses Kısılıyor.")
elif işlem==5:
    bilgisayar1.baglantı()
    print("İnternet Bağlantısı Kontrol Ediliyor.")
elif işlem==6:
    bilgisayar1.bluetooth_baglanti()
    print("Bluetooth Bağlantısı Kontrol Ediliyor")