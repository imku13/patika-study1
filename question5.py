#if

sayi = int(input("Bir sayı girin: "))

if sayi < 2:
    print("asal değil")
else:
    asal = True
    for i in range(2, sayi):
        if sayi % i == 0:
            asal = False
            break
    if asal:
        print("asal")
    else:
        print("asal değil")

#while döngüsü

sayi = int(input("Bir sayı girin: "))

if sayi < 2:
    print("asal değil")
else:
    asal = True
    i = 2
    while i < sayi:
        if sayi % i == 0:
            asal = False
            break
        i += 1

    if asal:
        print("asal")
    else:
        print("asal değil")

