# Alışveriş Listesi Uygulaması

alısveris_listesi=[] 

def menuyu_goster(): 
    print("\n---Alışveriş Listesi---") 
    print("1. Listeyi görüntüle") 
    print("2. Bir öge ekle") 
    print("3. Bir öge sil") 
    print("4. Listeyi temizle") 
    print("5. Ögeyi Düzenle") 
    print("Çıkış")

while True:
    
    secim=int(input("Yapmak istediğiniz işlemi giriniz (1-5):")) 

    if secim==1:
        print("\n---Alışveriş Listesi---") 
        if not alısveris_listesi:
            print("Listeniz boş.") 
        else:
         for index, item in enumerate(alısveris_listesi):
            print(f"{index+1}.{item}") 
    elif secim==2: 
       item=input("Bir öge ekleyiniz:") 
       alısveris_listesi.append(item)  
       print(f"{item} listeye eklenmiştir.")

    elif secim==3: 
       item=input("Silmek istediğiniz ögeyi yazınız:")
       if item in alısveris_listesi:
          alısveris_listesi.remove(item)
       else:
          print(f"{item} listede bulunamadı.")

    elif secim==4:
       alısveris_listesi.clear() 
       print("Liste temizlendi.") 

    elif secim==5:
       if item in alısveris_listesi:
        duzenlenmis_oge = input("Yeni halini yazınız: ")
        index = alısveris_listesi.index(item)    
        alısveris_listesi[index] = duzenlenmis_oge  
        print("Öge başarıyla düzenlendi!")
       else:
         print("Bu öge listede bulunamadı.")
      

    else:
     print("Görüşmek Üzere!")
     break
          
menuyu_goster() 

     

   



    
          
    
          
       
       


       
             