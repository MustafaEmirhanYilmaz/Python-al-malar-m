"""file=open("Notlar.txt","w",encoding="utf-8")
file.write("Ahmet Yılmaz, 85, 90, 78\nAyşe Demir, 95, 88, 92\nMehmet Kaya, 45, 60, 55\nZeynep Çelik, 70, 75, 80\nAli Arslan, 30, 40, 35\nFatma Şahin, 90, 95, 98\nMustafa Koç, 60, 65, 70\nElif Yıldız, 82, 78, 85\nCan Aydın, 50, 45, 55\nDeniz Öztürk, 75, 80, 72")"""

def not_hesapla(satır):
    
    satır=satır[:-1]

    liste=satır.split(",")

    isim=liste[0]
    not1=int(liste[1])
    not2=int(liste[2])
    not3=int(liste[3])
    son_not=not1 * (3/10) + not2 * (3/10) + not3 * (4/10)
    
    if son_not >=90 :
        harf="AA"
    elif son_not >=85:
        harf="BA"
    elif son_not >=80:
        harf="BB"
    elif son_not >=75:
        harf="CB"
    elif son_not >=70:
        harf="CC"
    elif son_not >=65:
        harf="DC"
    elif son_not >=60:
        harf="DD"
    elif son_not >=55:
        harf="FD"
    else:
        harf="FF"

    return isim +"," + harf 
    
with open("Notlar.txt","r",encoding="UTF-8") as file:

    eklenecekler_listesi=[]

    for i in file:
        eklenecekler_listesi.append(not_hesapla(i))
    print(eklenecekler_listesi)

    with open("HarfNotları.txt","w",encoding="UTF-8") as file2:
        for i in eklenecekler_listesi:
            file2.write(i)

    with open("HarfNotları.txt","r",encoding=("utf-8")) as file3:
        file3.read()
        harfnotu=eklenecekler_listesi[2]
        for i in eklenecekler_listesi:
            parca=i.split(",")
            harfnotu=parca[1]
            if harfnotu!="FF":
                with open("Geçenler.txt","a",encoding="UTF-8") as file4:
                    file4.write(i)
            else:
                with open("Kalanlar.txt","a",encoding="utf-8") as file5:
                    file5.write(i)
        
        
    
    
