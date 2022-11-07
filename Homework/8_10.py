# films = {
#     '1':'Человек-Паук 2',
#     '2':'Железный человек',
#     '3':'Бойцовский клуб'
# }
#
# times = {
#     '1': '16:20',
#     '2': '19:50',
#     '3': '23:30'
# }
#
# places = {
#     '1': '2 ряд 3 место',
#     '2': '54 ряд 27 место',
#     '3': '1 ряд 14 место'
# }
#
# for k,v in films.items():
#     print('Код фильма:', k, 'Название фильма:', v)
#
# film = input("На какой фильм вы хотите купить билет: ")
# film = films[film]
#
# for k,v in times.items():
#     print('Код времени:', k, 'Время:', v)
#
# time = input("На какое время вы хотите купить билет: ")
# time = times[time]
#
# for k,v in places.items():
#     print('Код места:', k, 'Место:', v)
#
# place = input("На какое место вы хотите купить билет: ")
# place = places[place]
#
# print('===================================')
# print('Вы купили билет на фильм:', film, '\nВремя:', time, '\nМесто:',place)


def subscript(a, b):
    print("a + b =", a+b)


def diff(a, b):
    print("a - b =", a-b)


def tangens(a, b):
    print("tg(a/b) =", a/b)


action = int(input(("""================================
Выберите операцию:
1 - сложение,
2 - разность,
3 - tg(a/b)
================================
""")))
print("================================")
a, b = map(int, input("Введите два числа: ").split())
print("================================")


if action == 1:
    subscript(a, b)
elif action == 2:
    diff(a,b)
elif action == 3:
    tangens(a,b)

