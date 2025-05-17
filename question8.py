#for

sayi = int(input("Bir sayı girin: "))

faktoriyel = 1
for i in range(1, sayi + 1):
    faktoriyel *= i

print(f"{sayi}! = {faktoriyel}")
#while

sayi = int(input("Bir sayı girin: "))

faktoriyel = 1
i = 1
while i <= sayi:
    faktoriyel *= i
    i += 1

print(f"{sayi}! = {faktoriyel}")
