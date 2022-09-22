# 1
euros_count = 100
dollars = euros_count * 1.25
rubles = dollars * 60
print(dollars)
print(rubles)

# 2
stark = "Arya"
print(f"Do you want to eat, {stark}?")
print("Yes, I'm hungry, mom.")

# 3
one = "Naharis"
two = "Mormont"
three = "Sand"
print(one[2] + two[1] + three[3] + two[4] + two[2])

# @
value = "Hexlet"
print(value[2:5])

# 5
a = str(2)
s = "times"
print(a, s)

# 6
value = "-42"
value = int(value)
value = abs(value)
print(value)

# 7
company1 = "Apple"
company2 = "Samsung"

length1 = len(company1)
length2 = len(company2)

print(length1 + length2)

# 8
num1 = 10
num2 = -13

num3 = num1 + num2
num4 = abs(num3)

print(num4)

#  9
number = 10.1234
number1 = round(number)
number2 = hex(number1)

print(number2)

#  10
from random import randint

print(randint(1, 10))

#  11
motto = "Family, Duty, Honor"
print(type(motto))

# 12
text = "When \t\n you play a \t\n game of thrones you win or you die."
print(len(text[5:16].strip()))

# 13
def print_motto():
    print("Winter is coming")


print_motto()

# 14
def say_hurray_three_times():
    return "hurray! hurray! hurray!"


result = say_hurray_three_times()
print(result)

# 15
def truncate(text, index):
    return text[:index] + "..."


print(truncate("Hexlet", 3))

# 16
def get_hidden_card(card_id, index=4):
    return ("*" * index+card_id[12:16])


print(get_hidden_card('2034399002121100', 1))  # "*1100"
print(get_hidden_card('1234567812345678', 2))  # "**5678"
print(get_hidden_card('1234567812345678', 3))  # "***5678"
print(get_hidden_card('1234567812345678'))    # "****5678"

# 17
def trim_and_repeat(text , offset = 0 , repetitions = 1):
	return(text[offset:6]*repetitions)

text = 'python'
print(trim_and_repeat(text, offset=3, repetitions=2))  # honhon
print(trim_and_repeat(text, repetitions=3))  # pythonpythonpython
print(trim_and_repeat(text))  # python

# 18
def get_age_difference(int1,int2):
   return(int2-int1)

actual = get_age_difference(2001, 2018)
print('The age difference is',actual)  # => The age difference is 17

