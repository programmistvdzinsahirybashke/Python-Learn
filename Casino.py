import random
from random import randrange
print ("Хотите играть? y/n")
answer = input()

if answer == "y":

    print ("Начинаем!")
    combinations = {111:"+10$" , 222:"+20$", 333:"+20$", 444:"+20$", 555:"+20$", 666:"-100$", 777:"+70", 888:"+80", 999:"+90"}
    balance = {111: 10, 222: 20, 333: 30, 444: 40, 555: 50, 666: -100, 777: 70, 888: 80, 999: 90}
    capital = int(input("С каким балансом вы хотите начать играть?\n"))

    tries = int(input("Сколько раз будем играть?\n"))

    for i in range(1, tries ):

        capital = capital - 0.2
        print("Ваш баланс:" , capital)
        randNum = random.randrange(111, 999)
        print (randNum)

        if randNum in combinations:
            if (randNum in combinations):

                print("\nПоздравляем, вы выиграли:" , combinations[randNum], end='', )
                print ("\n")

                capital = capital + balance[randNum]
                print("Ваш баланс:", capital)

        if answer == "n":
            breakpoint()
