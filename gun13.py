# Öğrenci Not Hesaplama Sistemi 

ogrenci_notları=input("Notları virgüllerle ayırarak giriniz:")
notlar=[float(notlar) for notlar in ogrenci_notları.split(",")] 

harf_notu= [
    "A" if notlar>=90 else 
    "B" if notlar>=80 else 
    "C" if notlar>=70 else 
    "D" if notlar>=60 else 
    "F" for notlar in notlar 

]

gecen_ogrenciler=[notlar for notlar in notlar if notlar>=60] 
kalan_ogrenciler=[notlar for notlar in notlar if notlar<60] 

print("\n---Öğrenci Notları---") 
for i, (notlar, harf_notu) in enumerate(zip(notlar,harf_notu), start=1):
    print(f"Öğrenci {i}: Not:{notlar} Harf Notu:{harf_notu}") 

print("\n---Dersten Kalan ve Geçen Öğrenciler---") 
print(f"Geçenler: {gecen_ogrenciler}") 
print(f"Kalanlar: {kalan_ogrenciler}") 




