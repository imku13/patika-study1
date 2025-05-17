def asal_mi(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def faktoriyel(n):
    sonuc = 1
    for i in range(1, n+1):
        sonuc *= i
    return sonuc

sayi = int(input("Bir sayı girin: "))
print("Asal mı?", asal_mi(sayi))
print("Faktöriyeli:", faktoriyel(sayi))
