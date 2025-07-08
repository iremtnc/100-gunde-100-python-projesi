# Hoş Geldin Mesajı Üretici 

from datetime import datetime



isim=input("Adınız nedir?:") 
isim=isim.upper() 

renk=input("En sevdiğiniz renk nedir?:") 
renk=renk.upper() 

simdi=datetime.now() 
tarih_str=simdi.strftime("%d-%m-%Y") 

print(f"Hoş geldin {isim}! Bugünün tarihi {tarih_str}. {renk} gerçekten harika bir renk.") 


