import random
import time

"""print("Sayı Tahmin Oyununa Hoşgeldiniz!")
1 ile 40 arasında bir sayı tuttum. Tahmin etmeye çalışın.
"""
rastgele_sayi=random.randint(1,40)
while True:
    tahmin=int(input("Tahmininizi girin: "))
    if tahmin<rastgele_sayi:
        print("Bilgiler Sorgulanıyor...")
        time.sleep(1)
        print("Daha büyük bir sayı söyleyin.")
    elif tahmin>rastgele_sayi:
        print("Bilgiler Sorgulanıyor...")
        time.sleep(1)
        print("Daha küçük bir sayı söyleyin.")
    else:
        print("Bilgiler Sorgulanıyor...")
        time.sleep(1)
        print("Tebrikler! Doğru tahmin ettiniz.")
        break