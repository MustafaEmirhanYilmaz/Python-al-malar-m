"""
Kullanıcıdan 2 tane sayı alarak 
bu sayıların en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın.
"""
sayi1=int(input("Birinci sayıyı girin: "))
sayi2=int(input("İkinci sayıyı girin: "))
def ebobbulma(sayi1,sayi2):
    if sayi1>sayi2:
        kucuksayi=sayi2
    else:
        kucuksayi=sayi1
    for i in range(kucuksayi,0,-1):
        if sayi1%i==0 and sayi2%i==0:
            print("EBOB:",i)
            break
ebobbulma(sayi1,sayi2)
    