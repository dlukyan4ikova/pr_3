def zad1():
    r = int(input("Введите радиус "))
    pi = 3.14159
    s = pi * r * r
    print("Площадь равна: ", s)

def zad2():
    a = int(input('Введите "a" '))
    b = int(input('Введите "b" '))
    x = -b/a
    print("X равен: ", x)

def zad3():
    c = int(input("Введите температуру по цельсию "))
    f = 95 * c + 32
    print("Температура по Фаренгейту ", f)

def zad4():
    a = int(input("Введите первое число "))
    b = int(input("Введите второе число "))
    c = int(input("Введите третье число "))
    cr = (a + b + c) / 3
    print("Среднее арифметическое ", cr)

def zad5():
    a = 5 + 2 * 3 - 4 // 2
    b = (3 + 5) * (2 + 4) // 2
    c = -3 + 6 // 2 * 4
    d = 5 + 4 * 5 ** 2 + 7
    print(a, b, c, d)

e = int(input('Введите номер задания..'))
if e == 1:
    zad1()
if e == 2:
    zad2()
if e == 3:
    zad3()
if e == 4:
    zad4()
if e == 5:
    zad5()

