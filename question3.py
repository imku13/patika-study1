value = int(input("Enter a number: "))
if value > 80 and value <= 100:
    print("81-100 A")
elif value > 60 and value <= 80:
    print("61-80 B")
elif value > 40 and value <= 60:
    print("41-60 C")
elif value > 20 and value <= 40:
    print("21-40 D")
elif value >= 0 and value <= 20:
    print("0-20 F")
else:
    print("Please enter a value within range 0-100")