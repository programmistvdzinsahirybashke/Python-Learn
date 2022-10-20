
arr = [1, 2, 3, 4, 5]
x = sum(arr)
count = 0

for i in arr:
    count += 1

print('Сумма:',x, 'Среднее арифметическое:', x / count)
print('================================')
arr = [3, 2, 52, 4, 60]
arr_new = []
arr_menshe = []
count = 0
count2 = 0

for i in arr:
    if i >= 50:
        arr_new.append(i)
        count +=1
    if i < 50:
        arr_menshe.append(i)
        count2+=1

z = sum(arr_menshe)
x = sum(arr_new)

print('Ср. арифм. элементов 0-50: ', z/count2)
print('Ср. арифм. элементов 50-100: ', x/count)