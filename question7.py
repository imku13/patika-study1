for _ in range(1000):  # Yüksek sayıda tekrar hakkı (örnek olarak 1000)
    value = int(input("Pozitif bir sayı girin: "))
    if value > 0:
        print("Tebrikler! Pozitif bir sayı girdiniz:", value)
        break
    else:
        print("Lütfen pozitif bir sayı girin.")
