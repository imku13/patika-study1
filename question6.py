notlar = [45, 85, 75, 50]
print(notlar.index(75))

#alternatif
notlar = [45, 85, 75, 50]

for i in range(len(notlar)):
    if notlar[i] == 75:
        print("75'in indisi:", i)
        break  # Eğer sadece ilk geçtiği yeri bulmak istiyorsan
