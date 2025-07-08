#Malzeme Kontrol Listesi 

tarif_malzemeleri={"süt","un","yag","yumurta","seker"}

mevcut_malzeme=input("Lütfen mevcut olan malzemeleri virgül ile ayırarak yazın:") 
mevcut_malzeme=set(mevcut_malzeme.split(","))

eksik_malzemeler=tarif_malzemeleri-mevcut_malzeme 
extra_malzeme=mevcut_malzeme-tarif_malzemeleri 

print("\n---Malzeme Listesi---") 

if eksik_malzemeler:
    print(f"Aşağıdaki malzemeler eksik. {','.join(eksik_malzemeler)}")
else:
    print("Tüm malzemeler tam.") 

if extra_malzeme:
    print(f"Fazladan malzemeniz mevcut. {','.join(extra_malzeme)}")



