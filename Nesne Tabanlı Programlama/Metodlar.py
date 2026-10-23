class Yazılımcı():
    def __init__(self, isim, soyisim, yaş, numara, maaş, diller):
        self.isim = isim
        self.soyisim = soyisim
        self.yaş = yaş
        self.numara = numara
        self.maaş = maaş
        self.diller = diller

    def bilgilerigoster(self):
        print("""
Yazılımcı Objesinin Özellikleri
isim={}
soyisim={}
yaş={}
numara={}
maaş={}
Bildiği_diller={}
""".format(self.isim, self.soyisim, self.yaş, self.numara, self.maaş, self.diller))

    def zamyap(self, zammiktari):
        print("Zam Yapılıyor...")
        self.maaş += zammiktari

    def dilekle(self, yenidil):
        print("Dil Ekleniyor...")
        self.diller.append(yenidil)



yazılımcı1 = Yazılımcı("Örnek", "Kullanıcı", 0, "00000000000", 0, ["c", "python", "java"])


yazılımcı1.zamyap(5000)

yazılımcı1.bilgilerigoster()