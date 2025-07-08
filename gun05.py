#Geri Sayım 

import time

basla=float(input("Lütfen başlamak istediğiniz sayıyı giriniz:")) 
aralik=float(input("Zaman aralığını giriniz:" ))

yarilanma_noktasi=basla/2 


print("---Geri Sayım Başlıyor!---") 

while basla>0:
     if basla==yarilanma_noktasi:
        print("Zaman yarılandı!")
     else: 
        print(basla)
     time.sleep(aralik) 
     basla-=aralik
    


print("Geri sayım tamamlandı!")  
    
