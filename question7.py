#Kullancidan pozitif bir sayi bekleyen, pozitifi de gördügü an bastiran, negatif sayi girildikçe bir daha soran yapi kuralim. (for döngüsü ile)
for _ in range(1000):  # Yüksek sayıda tekrar hakkı (örnek olarak 1000)
    value = int(input("Pozitif bir sayı girin: "))
    if value > 0:
        print("Tebrikler! Pozitif bir sayı girdiniz:", value)
        break
    else:
        print("Lütfen pozitif bir sayı girin.")
