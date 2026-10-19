"""
print("Hesap Makinesi Programına Hoşgeldiniz")
işlem 1:toplama
işlem 2:çıkarma
işlem 3:çarpma
işlem 4:bölme
işlem 5:üs alma
işlem 6:karekök alma
işlem 7:Logaritma alma
işlem 8:Sinüs alma
işlem 9:Kosinüs alma
işlem 10:Tanjant alma
işlem 11:Kosekan alma
işlem 12:Sekant alma
işlem 13:Kotanjant alma
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
    elif islem==7:
        sayi1=int(input("Bir sayı girin: "))
        print("Logaritma:",math.log(sayi1))
    elif islem==8:
        sayi1=int(input("Bir açı girin: "))
        print("Sinüs:",math.sin(sayi1))
    elif islem==9:
        sayi1=int(input("Bir açı girin: "))
        print("Kosinüs:",math.cos(sayi1))
    elif islem==10:
        sayi1=int(input("Bir açı girin: "))
        print("Tanjant:",math.tan(sayi1))
    elif islem==11:
        sayi1=int(input("Bir açı girin: "))
        print("Kosekan:",1/math.sin(sayi1))
    elif islem==12:
        sayi1=int(input("Bir açı girin: "))
        print("Sekant:",1/math.cos(sayi1))
    elif islem==13:
        sayi1=int(input("Bir açı girin: "))
        print("Kotanjant:",1/math.tan(sayi1))