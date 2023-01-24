import math
a = float(input("Введите длину большего основания а: "))
b = float(input("Введите длину меньшего основания b: "))
angle = float(input("Введите угол при большем основании в градусах: "))
alpha = angle * math.pi / 180
area = (a ** 2 - b ** 2) / 4 * math.tan(alpha)
print("Площад трапеции = %.2f" %area)