"""
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

# Смешивание цветов

first_color = input('Введите первый цвет(красный, синий или желтый): ').capitalize()
second_color = input('Введите второй цвет(красный, синий или желтый): ').capitalize()


if first_color == 'Красный' and second_color == 'Синий' or first_color == 'Синий' and second_color == 'Красный':
    print('Фиолетовый')
elif first_color == 'Красный' and second_color == 'Желтый' or first_color == 'Желтый' and second_color == 'Красный':
    print('Оранжевый')
elif first_color == 'Синий' and second_color == 'Желтый' or first_color == 'Желтый' and second_color == 'Синий':
    print('Зеленый')
else:
    print('Ошибка цвета')
"""