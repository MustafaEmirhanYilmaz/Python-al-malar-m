"""1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın. 
Bunun için bir sayının mükemmel olup olmadığını dönen bir tane fonksiyon yazın.
Bir sayının bölenlerinin toplamı kendine eşitse bu sayı mükemmel bir sayıdır. 
Örnek olarak 6 mükemmel bir sayıdır (1 + 2 + 3 = 6)."""

def mukemmelmi():
    for i in range(1,1001,1):
        toplam=0
        for j in range(1,i,1):
            if i%j==0:
                toplam+=j
        if toplam==i:
            print(i,"mükemmel bir sayıdır.")
mukemmelmi()