from random import randint

1
"""
euros_count = 100
dollars = euros_count * 1.25
rubles = dollars * 60
print(dollars)
print(rubles)
print('======================================')

# 2
stark = "Arya"
print(f"Do you want to eat, {stark}?")
print("Yes, I'm hungry, mom.")
print('======================================')

# 3
one = "Naharis"
two = "Mormont"
three = "Sand"
print(one[2] + two[1] + three[3] + two[4] + two[2])
print('======================================')

# @
value = "Hexlet"
print(value[2:5])
print('======================================')

# 5
a = str(2)
s = "times"
print(a, s)
print('======================================')

# 6
value = "-42"
value = int(value)
value = abs(value)
print(value)
print('======================================')

# 7
company1 = "Apple"
company2 = "Samsung"

length1 = len(company1)
length2 = len(company2)

print(length1 + length2)
print('======================================')

# 8
num1 = 10
num2 = -13

num3 = num1 + num2
num4 = abs(num3)

print(num4)
print('======================================')

#  9
number = 10.1234
number1 = round(number)
number2 = hex(number1)

print(number2)
print('======================================')

#  10
from random import randint

print(randint(1, 10))
print('======================================')

#  11
motto = "Family, Duty, Honor"
print(type(motto))
print('======================================')

# 12
text = "When \t\n you play a \t\n game of thrones you win or you die."
print(len(text[5:16].strip()))
print('======================================')

# 13
def print_motto():
    print("Winter is coming")


print_motto()
print('======================================')

# 14
def say_hurray_three_times():
    return "hurray! hurray! hurray!"


result = say_hurray_three_times()
print(result)
print('======================================')

# 15
def truncate(text, index):
    return text[:index] + "..."


print(truncate("Hexlet", 3))
print('======================================')

# 16
def get_hidden_card(card_id, index=4):
    return "*" * index + card_id[12:16]


print(get_hidden_card("2034399002121100", 1))  # "*1100"
print(get_hidden_card("1234567812345678", 2))  # "**5678"
print(get_hidden_card("1234567812345678", 3))  # "***5678"
print(get_hidden_card("1234567812345678"))  # "****5678"
print('======================================')

# 17
def trim_and_repeat(text, offset=0, repetitions=1):
    return text[offset:6] * repetitions


text = "python"
print(trim_and_repeat(text, offset=3, repetitions=2))  # honhon
print(trim_and_repeat(text, repetitions=3))  # pythonpythonpython
print(trim_and_repeat(text))  # python
print('======================================')

# 18
def get_age_difference(int1, int2):
    return int2 - int1


actual = get_age_difference(2001, 2018)
print("The age difference is", actual)  # => The age difference is 17
print('======================================')

# 19
def has_upper_case(string):
    return string.lower() != string


print(has_upper_case(""))  # False
print(has_upper_case("python"))  # False
print(has_upper_case("pyThon"))  # True
print('======================================')

# 20
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


print(is_leap_year(2018))  # False
print(is_leap_year(2017))  # False
print(is_leap_year(2016))  # True
print('======================================')

# 21
def string_or_not(value):
	return isinstance(value,str) and 'yes' or 'no'

print(string_or_not('Hexlet')) # yes
print(string_or_not(10)      ) # no
print(string_or_not('')      ) # yes
print(string_or_not(False)   ) # no
print('======================================')

# 22
def normalize_url(url):
    https = 'https://'
    if url[:8] == https:
        return url
    elif url[:7] == 'http://':
        return https + url[7:]
    else:
        return https + url

normalize_url('https://ya.ru')  # 'https://ya.ru'
normalize_url('google.com')  # 'https://google.com'
normalize_url('http://ai.fi')  # 'https://ai.fi'
print('======================================')

# 23
def print_numbers(last_number):
    i = last_number
    while i > 0:
        print(i)
        i = i - 1
    print('finished!')


print(print_numbers(12))
print('======================================')

# 24
def join_numbers_from_range(start,finish):
    i = start
    result = ''
    while i <= finish:
        result = result + str(i)
        i = i + 1
    return result


print(join_numbers_from_range(5, 10))
print('======================================')

# 25
def my_substr(str,length):
    i = 0
    result = ''

    while i < length:
        result = result + str[i]
        i += 1
    return result


string = 'If I look back I am lost'
print(my_substr(string, 7))  # => 'If I lo'
print('======================================')

# 26
def is_contains_char(str, char):
    count = 0
    index = 0

    while index < len(str):
        str = str.upper()
        current = str[index]
        if current == char or current == char.capitalize():
            count += 1
            return True
        index = index + 1
    else:
        return False


print(is_contains_char('Awesomeness', 'm'))  # => True
print(is_contains_char('Hexlet', 'H'))  # => True
print(is_contains_char('Hexlet', 'h'))  # => True
print(is_contains_char('Awesomeness', 'd'))  # => False
print(is_contains_char('Awesomeness', 'S'))  # => False

# 27
def filter_string(str,char):
    result = ''
    index = 0
    for symbol in str:
        if char.lower() != symbol.lower():
            result = result + symbol
            index += 1
    print(result.strip())


text = 'If I look forward I win'
filter_string(text, 'i')  # 'f  look forward  wn'
filter_string(text, 'O')  # 'If I lk frward I win

# 28
def is_palindrome(text):
    reversed_string = text[::-1]
    if text == reversed_string:
        print(text, ':', reversed_string)
        return True
    else:
        print(text, ':', reversed_string)
        return False


print(is_palindrome('') ) # True пустая строка тоже считается палиндромом
print(is_palindrome('radar')) # True
print(is_palindrome('a')) # True
print(is_palindrome('abs')) # False
print(is_palindrome('ишак ищет у тещи каши')) # True

# 29
def count_vowels(text):
    count = 0
    for char in text:
        if char in 'aeiou' or char in 'AEIOU' or char in 'аяуюоеёэиы' or char in 'АЯУЮОЕЁЭИЫ':
            count += 1
    return count


print(count_vowels('London is the capital of Great Britain'))  # 13
print(count_vowels('One'))  # 2
print(count_vowels('Ульяновск – столица мира'))



# 30
def choice_from_range(str, start, finish):
    a = randint(start, finish)
    return str[a]
# def choice_from_range(text, begin, end):
#    return text[random.randint(begin, end)]


text = "abcdef"
print(choice_from_range(text, 0, 0))  # d


# 31
def sort_pair(pair):
    (int1,int2) = pair
    if int1 < int2:
        return (int1, int2)
    else:
        pair = (int2, int1)
        return pair


print(sort_pair((5, 1)))
print(sort_pair((2, 2)))
print(sort_pair((7, 8)))
"""

