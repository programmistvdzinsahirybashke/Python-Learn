import random

a = [random.randint(1, 20) for x in range(10)]
print("Список:", a)

count_a = 0
proiz_a = 1
sum_a = 0

for i in a:
    if i > 10:
        count_a += 1
    if i < 10:
        proiz_a = proiz_a * i
        sum_a = sum_a + i

print('Количество чисел больше 10 =', count_a)
print('Произведение чисел меньше 10 =', proiz_a)
print('Сумма чисел меньше 10 =', sum_a)
print("Максимальное число в списке", max(a), "Индекс этого числа = ", a.index(max(a)))

c = a[0:5]
print("Список с 0 по 5:", c)

d = random.sample(a,len(a))
print("Перемешанный список:", d)

e = ((a[:len(a)//2][::-1]))
print("Реверс первой половины списка:", e)

print("==========================")

b = [random.randint(1, 20) for b in range(10)]
b = tuple(b)
print("Кортеж:", b)

proiz_b = 1
sum_b = 0
count_b = 0

for i in b:
    if i > 10:
        count_b += 1
    if i < 10:
        proiz_b = proiz_b * i
        sum_b = sum_b + i

print('Количество чисел больше 10 =', count_b)
print('Произведение чисел меньше 10 =', proiz_b)
print('Сумма чисел меньше 10 =', sum_b)
print("Максимальное число в кортеже", max(b), "Индекс этого числа = ", b.index(max(b)))