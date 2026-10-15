print(""" Faktöriyel Bulma Programı
Çıkmak için "q" ya basınız.
""")
while True:
    sayi=input("Lütfen Bir Sayı Giriniz")
    if sayi =="q":
        print("Program Sonlandırılıyor.")
        break
    else:
        sayi=int(sayi)
        faktoriyel=1
        for i in range(2,sayi+1):
            faktoriyel*=i
            print(faktoriyel)

          

