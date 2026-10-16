
def tambolenbulma(sayi):
    bolenler=[]
    for i in range (1,sayi+1,1):
        if sayi%i==0:
                bolenler.append(i)
                
    return bolenler
sonuc = tambolenbulma(100)
print("Tam Bölenler:",sonuc)
