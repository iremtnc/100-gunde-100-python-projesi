#Dosya İşlemleri - Not Alma Uygulaması

import datetime 

zaman=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

dosya_adi="notlarim.txt" 

def menu_goster():
    print("---Not Defteri---") 
    print("1. Not Ekle")
    print("2. Tüm Notları Görüntüle")
    print("3. Tüm Notları Sil") 
    print("4. Çıkış") 


def not_ekle():
    
    notlar=input("Notunuzu girin:")
    with open(dosya_adi,"a") as file:
        file.write(f"{zaman} {notlar}\n")
    print("Not başarıyla eklendi.")


def not_goruntule(): 
    try:
        with open(dosya_adi,"r") as file:
            icerik=file.read() 
            if icerik:
                print("\n---Notlarınız---")
                print(icerik) 
            else:
                print("Not bulunamadı.") 

    except FileNotFoundError:
        print("Not bulunamadı.")


def not_sil():
    confirm=input("Tüm notları silmek istediğinizden emin misiniz? (Evet/h)")
    if confirm.lower()=="evet":
        with open(dosya_adi,"w") as file:
            pass 
        print("Tüm notlar silindi.")
    else:
        print("Silme işlemi iptal edildi.") 



while True:
    menu_goster() 
    secim=input("Seçiminizi girin(1-4):") 

    if secim=="1":
        not_ekle()
    elif secim=="2":
        not_goruntule() 
    elif secim=="3":
        not_sil() 
    elif secim=="4":
        print("Hoşça kalın!") 
        break 
    else:
        print("Geçersiz seçim,lütfen tekrar deneyin.") 



        
 






