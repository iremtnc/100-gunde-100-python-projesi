#İletişim Defteri 

kisiler={} 

def menuyu_goster(): 
    print("\n---İletişim Defteri---")
    print("1.Kişileri Görüntüle")
    print("2.Kişi Ekle:")
    print("3.Kişi Ara:")
    print("4.Kişiyi Düzenle:")
    print("5.Kişiyi Sil:")
    print("6.Çıkış") 

def kisi_ekle():
    isim=input("İsim:")
    numara=input("Telefon-no:")
    email=input("E-posta adresi (eklemek istemiyorsanız ENTER'a basın):") 
    kisiler[isim]={"numara":numara, "email":email}  
    print(f"{isim} kişisi iletişim defterinize eklendi.")  


def kisi_goruntule(): 
    if kisiler:
        print("\n---Kişi Listesi---")
        for isim, details in kisiler.items():
            print(f"Name: {isim}")
            print(f"Telefon-no: {details['numara']}") 
            print(f"E-posta: {details['email']}")   

    else:
        print("Kişi listeniz boş.") 


def kisi_ara():
    isim=input("Aramak istediğiniz kişinin ismini giriniz:") 
    if isim in kisiler:
        print(f"\n---{isim} Kişisinin İletişim Bilgileri:") 
        print(f"İsim: {isim}")
        print(f"Telefon no: {kisiler[isim]['numara']}") 
        print(f"E-posta: {kisiler[isim]['email']}") 
    else:
        print("Aradığınız kişi bulunamadı.")


def kisi_duzenle():
    isim=input("Düzenlemek istediğiniz kişinin ismini giriniz:")
    if isim in kisiler: 
      numara=input("Telefon Numarasını Düzenle:")
      email=input("E-posta Adresini Düzenle:")
      kisiler[isim]={"numara":numara, "email":email} 
      print(f"{isim} kişisinin bilgileri başarıyla düzenlendi.")
    else:
        print("Kişi bulunamadı.")  


def kisi_sil():
    isim=input("Silmek istediğiniz kişinin ismini giriniz:")
    if isim in kisiler:
        del kisiler[isim]
        print(f"{isim} kişisi silindi.")
    else:
        print(f"{isim} kişisi bulunamadı.") 


while True:
    menuyu_goster() 
    secim=input("Yapmak istediğiniz işlemi seçin (1-6):")

    if secim=="1":
        kisi_goruntule() 
    elif secim=="2":
        kisi_ekle() 
    elif secim=="3": 
        kisi_ara() 
    elif secim=="4":
        kisi_duzenle() 
    elif secim=="5":
        kisi_sil()
    elif secim=="6":
        print("Hoşça kalın!")
        break
    else:
        print("Geçersiz seçim, lütfen 1 ve 6 arasında bir seçim yapın.")   
