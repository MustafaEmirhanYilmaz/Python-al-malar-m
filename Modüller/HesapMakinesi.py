"""
print("Hesap Makinesi Programına Hoşgeldiniz")
işlem 1:toplama
işlem 2:çıkarma
işlem 3:çarpma
işlem 4:bölme
işlem 5:üs alma
işlem 6:karekök alma
Çıkmak İçin "q" ya basın.

"""


import math
islem=(input("Yapmak istediğiniz işlemi seçin: "))
if islem=="q":
    print("Programdan çıkılıyor...")
else:
    islem=int(islem)
    if islem==1:
        sayi1=int(input("Birinci sayıyı girin: "))
        sayi2=int(input("İkinci sayıyı girin: "))
        print("Toplam:",sayi1+sayi2)
    elif islem==2:
        sayi1=int(input("Birinci sayıyı girin: "))
        sayi2=int(input("İkinci sayıyı girin: "))
        print("Fark:",sayi1-sayi2)
    elif islem==3:
        sayi1=int(input("Birinci sayıyı girin: "))
        sayi2=int(input("İkinci sayıyı girin: "))
        print("Çarpım:",sayi1*sayi2)
    elif islem==4:
        sayi1=int(input("Birinci sayıyı girin: "))
        sayi2=int(input("İkinci sayıyı girin: "))
        print("Bölüm:",sayi1/sayi2)
    elif islem==5:
        sayi1=int(input("Birinci sayıyı girin: "))
        sayi2=int(input("İkinci sayıyı girin: "))
        print("Üs:",sayi1**sayi2)
    elif islem==6:
        sayi1=int(input("Bir sayı girin: "))
        print("Karekök:",math.sqrt(sayi1))