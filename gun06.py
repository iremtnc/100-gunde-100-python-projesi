#Basit Matematik Quiz Oyunu 

import random

def soru_olustur():
    sayi1 = random.randint(0, 10)
    sayi2 = random.randint(0, 10)
    operator = random.choice(["-", "+", "*"])

    if operator == "-":
        cevap = sayi1 - sayi2
    elif operator == "+":
        cevap = sayi1 + sayi2
    else:
        cevap = sayi1 * sayi2

    return f"{sayi1} {operator} {sayi2}", cevap


def quiz():
    skor = 0
    tur =int(input("Kaç tur oynamak istersiniz?")) 

    print("Matematik Quiz Oyununa Hoş Geldiniz!")
    print("Karşınıza çıkan sorulara doğru cevaplar vermeniz gerekecek.")

    for i in range(tur):
        soru, dogru_cevap = soru_olustur()
        print(f"\nSoru {i+1}: {soru}")
        try:
            kullanici_cevap = int(input("Cevabınız: "))
        except ValueError:
            print("Geçersiz giriş! Sayı girmen gerekiyor.")
            continue

        if kullanici_cevap == dogru_cevap:
            print("Doğru!")
            skor += 1
        else:
            print(f"Yanlış cevap! Doğru cevap şudur: {dogru_cevap}")

    print("\nOyun Bitti!")
    print(f"Skorunuz: {skor}/{tur}")

    if skor == tur:
        print("Tebrikler! Tüm soruları doğru cevapladınız.")
    elif skor >= tur // 2:
        print("İyi iş çıkardın!")
    else:
        print("Pratik yapmaya devam! Gelecek sefer daha iyi olacaksın.")


# Programı başlat
quiz()

    
 