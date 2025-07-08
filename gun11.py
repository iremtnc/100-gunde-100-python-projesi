#Hata Yakalama - Hesap Makinesi 



def toplama(x,y):
    return x+y 

def cikarma(x,y):
    return x-y 

def carpma(x,y):
    return x*y

def bolme(x,y):
    if y==0: 
        raise ZeroDivisionError("Sayı 0'a bölünemez.")
        
    return x/y 

def mod(x,y):
    if y==0:
        raise ZeroDivisionError("Sayı 0'a bölünemez.") 
    return x//y 

def us(x,y):
    return x**y

def menu_goster():
    print("\n---Hesap Makinesi---")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma") 
    print("4. Bölme") 
    print("5. Kalan:")
    print("6. Üssünü al")
    print("7. Çıkış yap")
    


while True:
    menu_goster()
    secim=input("Lütfen yapmak istediğiniz işlemi seçiniz(1-5):") 

    if secim=="7": 
        print("Hoşça kalın!") 
        break 

    try:
        sayi1=float(input("1. sayıyı giriniz:"))
        sayi2=float(input("2. sayıyı giriniz:")) 

        if secim=="1":
            print("Sonuç:",toplama(sayi1,sayi2)) 

        elif secim=="2":
            print("Sonuç:",cikarma(sayi1,sayi2))

        elif secim=="3":
            print("Sonuç:",carpma(sayi1,sayi2))

        elif secim=="4":
            print("Sonuç:",bolme(sayi1,sayi2)) 

        elif secim=="5":
            print("Sonuç:",mod(sayi1,sayi2)) 

        elif secim=="6":
            print("Sonuç:", us(sayi1,sayi2))

        else:
            print("Geçersiz seçim. Lütfen tekrar deneyiniz.") 

    except ValueError:
        print("Lütfen geçerli sayılar girin.") 
    except ZeroDivisionError as e:
        print(f"Hata: {e}") 
    except Exception as e:
        print(f"Beklenmedik bir hata oluştu: {e}")    

    finally:
        print("Hesap makinesini kullandığınız için teşekkürler.") 



    
    


