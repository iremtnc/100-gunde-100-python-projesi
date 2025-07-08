#Basit Hesap Makinesi

sayi1=float(input("1. sayıyı giriniz:"))
sayi2=float(input("2. sayıyı giriniz:")) 

toplama= sayi1+sayi2 
cikarma= sayi1-sayi2
carpma= sayi1*sayi2 
bolme= sayi1/sayi2  if sayi2!=0 else "Sayı sıfıra bölünemez." 
mod= sayi1%sayi2 
usAlma= sayi1**sayi2 

print("----Sonuçlar----") 
print(f"Toplama= + {toplama}")
print(f"Çıkarma= + {cikarma}")
print(f"Çarpma= + {carpma}")
print(f"Bölme= + {bolme}") 
print(f"Mod= + {mod}") 
print(f"Üs= + {usAlma}") 



