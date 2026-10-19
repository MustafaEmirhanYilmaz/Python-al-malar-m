"""
Fonksiyonlarla EKOK Bulma
"""

sayi1=int(input("Birinci sayıyı girin: "))
sayi2=int(input("İkinci sayıyı girin: "))
def ekokbulma(sayi1,sayi2):
    if sayi1>sayi2:
        buyuksayi=sayi1
    else:
        buyuksayi=sayi2
    while True:
        if buyuksayi%sayi1==0 and buyuksayi%sayi2==0:
            print("EKOK:",buyuksayi)
            break
        buyuksayi+=1
ekokbulma(sayi1,sayi2)