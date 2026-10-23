class Öğrenci():
    def __init__(self,Ad="Bilgi Yok",Soyad="Bilgi Yok",No="Bilgi Yok",Sınıf="Bilgi Yok"):
        self.Ad=Ad
        self.Soyad=Soyad
        self.No=No
        self.Sınıf=Sınıf
def bilgileri_göster(self):
        print("""
Öğrenci Sınıfının Özellikleri
Ad ={}
Soyad={}
No={}
Sınıf={}
""".format(self.Ad,self.Soyad,self.No,self.Sınıf)
)

öğrenci1=Öğrenci("Murat","Kınacı",12345,4)
öğrenci2=Öğrenci(No=5)
bilgileri_göster(öğrenci2)
        