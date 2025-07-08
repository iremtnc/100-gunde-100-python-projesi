# Sayı Karşılaştırıcı ---> if-else yapısı 

sayi1=float(input("1. sayıyı giriniz:")) 
sayi2=float(input("2. sayıyı giriniz:")) 

if sayi1==sayi2:
    print("Girilen sayılar eşittir.")

elif sayi1>sayi2: 
    print(f"{sayi1}büyüktür {sayi2}.") 

else:
    print(f"{sayi1} küçüktür {sayi2}.")
 
if sayi1==0 or sayi2==0:
    print("Girilen sayılardan biri 0'dır.") 
else:
    print("Girilen sayılar 0'dan farklıdır.") 

soru=input("Başka bir sayı daha girmek ister misiniz?(E/H)").upper() 

if soru=="E": 
    sayi3=float(input("3. sayıyı giriniz:")) 
else: 
    print("Görüşmek üzere!") 

en_buyuk=max(sayi1, sayi2, sayi3) 
print(f"Girilen en büyük sayı: {en_buyuk}") 

if sayi3==0:
    print("3. sayı 0'dır.") 
else: 
    print("3. sayı 0'dan farklıdır.") 



