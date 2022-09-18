# Задача А
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

sum = a + b + c
multiply = a * b * c
srednee = (a + b + c) / 3

print("Сумма:", sum)
print("Произведение:", multiply)
print("Среднее арифметическое:", srednee)

# Задача B
x1 = float(input("Введите координаты точки A: "))
y1 = float(input("Введите координаты точки A: "))
x2 = float(input("Введите координаты точки B: "))
y2 = float(input("Введите координаты точки B: "))

length = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
print(length)
