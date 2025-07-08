#Fonksiyonlar - Sıcaklık Dönüştürücü 

def celcius_to_fahrenheit(celcius):
    return (celcius * 9/5) +32 

def celcius_to_kelvin(celcius):
    return(celcius +273.15)

def fahrenheit_to_celcius(fahrenheit):
    return(fahrenheit-32) *5/9 

def fahrenheit_to_kelvin(fahrenheit):
    return(fahrenheit-32)*5/9 + 273.15

def kelvin_to_celcius(kelvin):
    return kelvin - 273.15 

def kelvin_to_fahrenheit(kelvin):
    return((kelvin-273.15) *9/5) +32 


def menuyu_goster(): 
    print("\n---Sıcaklık Dönüştürme Menüsü---") 
    print("1.Celcius ---> Fahrenheit&Kelvin:")
    print("2.Fahreheit ---> Celcius&Kelvin:") 
    print("3.Kelvin ---> Celcius&Fahrenheit:")
    print("4.Çıkış")


    while True:
        menuyu_goster()
        secim=input("Lütfen yapmak istediğiniz işlemi seçiniz(1-4):") 

        if secim=="1":
            celcius=float(input("Celcius değerini giriniz:"))
            print(f"Fahrenheit: {celcius_to_fahrenheit(celcius):.2f}")
            print(f"Kelvin: {celcius_to_kelvin(celcius):.2f}") 

        elif secim=="2":
            fahrenheit=float(input("Fahrenheit değerini giriniz:"))
            print(f"Celcius: {fahrenheit_to_celcius(fahrenheit):.2f}")
            print(f"Kelvin: {fahrenheit_to_kelvin(fahrenheit):.2f}") 
        
        elif secim=="3":
            kelvin=float(input("Kelvin değerini giriniz:"))
            print(f"Celcius: {kelvin_to_celcius(kelvin):.2f}")
            print(f"Fahrenheit: {kelvin_to_fahrenheit(kelvin):2f}") 

        elif secim=="4":
            print("Bu programı kullandığınız için teşekkürler!")
            break 

        else:
            print("Geçersiz seçim, lütfen tekrar deneyiniz.") 


            


        

       
 
