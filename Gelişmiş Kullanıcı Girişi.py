kullanıcıadi="python"
kullanıcısifre=1234
girisyapmahakki=3
print("3 Giriş Yapma Hakkınız Vardır.")
while True:
    if girisyapmahakki>0:
        ka=input("Kullanıcı Adını Giriniz:")
        sifre=int(input("Şifrenizi Giriniz"))
        if kullanıcıadi!=ka and kullanıcısifre==sifre:
            print("Kullanıcı Adı Yanlış.")
            girisyapmahakki-=1
            print("Giriş yapma hakkınız",girisyapmahakki)
            continue
        elif kullanıcıadi==ka and kullanıcısifre!=sifre:
            print("Sifre yanlış girilmiştir.")  
            girisyapmahakki-=1
            print("Giriş yapma hakkınız",girisyapmahakki)
            continue
        elif kullanıcıadi!=ka and kullanıcısifre!=sifre:
            print("Bilgiler Yanlış Girilmiştir")
            girisyapmahakki-=1
            print("Giriş yapma hakkınız",girisyapmahakki)
            continue
        elif girisyapmahakki==0:
            print("Giriş yapma hakkınız bitmiştir.")
            break
        else:
            print("Başarıyla giriş yapılmıştır")
            break