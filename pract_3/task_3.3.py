god = int(input("Введите год: "))

if (god % 4 == 0 and god % 100 != 0) or (god % 400 == 0):
    res = "високосный"
else:
    res = "не високосный"
print(f"Год {god} - {res}")
