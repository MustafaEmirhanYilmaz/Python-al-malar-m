print(""" Atm Makinesine Hoşgeldiniz
1. işlem =bakiye sorgulama
2. işlem= para yatırma
3.işlem=para çekme
Çıkmak için "q" ya basın.
""")
bakiye=1000
print("Bakiyeniz:",bakiye)
işlem=input("Yapmak İstediğiniz işlemi giriniz:")
while True:
    if işlem=="q":
        print("Çıkış yapılıyor.")
        break
    elif işlem=="1":
        print("Bakiyeniz",bakiye)
        break
    elif işlem=="2":
        miktar=int(input("Yatırmak İstediğiniz Miktarı Giriniz:"))
        bakiye+=miktar
        print("Bakiyeniz",bakiye)
        break
    elif işlem == "3":
        miktar=int(input("Çekmek İstediğiniz Miktarı Giriniz:"))
        if bakiye<=miktar:
            print("Bu İşlem Gerçekleştirilemedi...")
            break
        else:
            bakiye=bakiye-miktar
            print("Bakiyeniz:",bakiye)
            break
    else:
        print("Geçersiz İşlem")
        break
    