"""Çalışan Sınıfı oluşturulacak özellikleri isim maaş departman
içine çalışan sınıfının init fonksiyonu özellikleri tanımla
bilgileri göster metodunu yaz 
departman değiştir metodunu yaz
Yönetici sınıfı oluştur ve çalışanın özelliklerini al"""
class Çalışan():
    def __init__(self, isim, maaş, departman):
        print("Çalışan sınıfının İnit Fonksiyonu Çalıştı.")
        self.isim = isim
        self.maaş = maaş
        self.departman = departman

    def bilgileri_göster(self):
        print("Çalışan Sınıfının Özellikleri")
        print("İsim: {}, Maaş: {}, Departman: {}".format(self.isim, self.maaş, self.departman))

    def departman_değiştir(self, yeni_departman):
        print("Departman Değiştiriliyor...")
        self.departman = yeni_departman  
class Yönetici(Çalışan):
    def zamyap(self,zammiktarı):
        self.maaş+=zammiktarı
yönetici1 = Yönetici("Murat Kınacı", 3000, "Bilişim Departmanı")
yönetici1.bilgileri_göster()
yönetici1.departman_değiştir("İnsan Kaynakları")
yönetici1.bilgileri_göster()
yönetici1.zamyap(3000)
yönetici1.bilgileri_göster()
