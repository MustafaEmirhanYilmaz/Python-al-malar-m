def asalmi():
    sayi = int(input("Bir sayı girin: "))
    for i in range(2, sayi):
        if sayi % i == 0:
            print(sayi, "asal değildir.")
            break
    else:
        print(sayi, "asaldır.") 
asalmi()