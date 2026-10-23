class Çalışan():
    def __init__(self,Ad="Bilgi Yok",Soyad="Bilgi Yok",Yaş="Bilgi Yok",Maaş="Bilgi Yok",Departman="Bilgi Yok"):
        self.Ad=Ad
        self.Soyad=Soyad
        self.Yaş=Yaş
        self.Maaş=Maaş
        self.Departman=Departman
def bilgileri_göster(self):
        print("""
Çalışan Sınıfının Özellikleri
Ad={}
Soyad={}
Yaş={}
Maaş={}
Departman={}
""".format(self.Ad,self.Soyad,self.Yaş,self.Maaş,self.Departman))
çalışan1=Çalışan("Çalışan 1","Çalışan 1 Soyad",25,10.000,"İnsan Kaynakları")
çalışan2=Çalışan()
bilgileri_göster(çalışan2)

        