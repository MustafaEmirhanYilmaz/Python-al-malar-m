sayi=int(input("Bir sayı girin: "))
def okunusbulma(sayi):
    birler={"bir":1,"iki":2,"üç":3,"dört":4,"beş":5,"altı":6,"yedi":7,"sekiz":8,"dokuz":9}
    onlar={"bir":10,"iki":20,"üç":30,"dört":40,"beş":50,"altı":60,"yedi":70,"sekiz":80,"dokuz":90}
    onlar= sayi // 10
    birler= sayi % 10
    if onlar==1:
        print("on")
    elif onlar==2:              
        print("yirmi")
    elif onlar==3:
        print("otuz")
    elif onlar==4:
        print("kırk")
    elif onlar==5:
        print("elli")
    elif onlar==6:
        print("altmış")
    elif onlar==7:
        print("yetmiş")
    elif onlar==8:
        print("seksen")
    elif onlar==9:
        print("doksan")
    if birler==1:
        print("bir")
    elif birler==2:
        print("iki")
    elif birler==3:
        print("üç")
    elif birler==4:
        print("dört")
    elif birler==5:
        print("beş")
    elif birler==6:
        print("altı")
    elif birler==7:
        print("yedi")
    elif birler==8:
        print("sekiz")
    elif birler==9:
        print("dokuz")
okunusbulma(sayi)