#Kişiselleştirilmiş Selamlama 

from datetime import datetime

isim=input("Adınız:") 
dogum_tarihi=int(input("Doğum yılınız:")) 
renk=(input("En sevdiğiniz renk:"))

yil=datetime.now().year
yas= yil - dogum_tarihi 

print(f"Hoş Geldin {isim}! Sen {yas} yaşındasın ve en sevdiğin renk {renk}.") 