# Спроси у пользователя имя и возраст, выведи приветствие:
# "Привет, Иван! Тебе 12 лет?".
# Спроси два числа, сложи их и выведи результат.
# Спроси строку и выведи её в верхнем регистре (.upper()).

# name = input("Как тебя зовут? ")
# age = input("Сколько тебе лет? ")
#
# print(f'Привет, {name}! Тебе {age} лет?')
# print()
#
# num_1 = int(input("Введи 1-е число: "))
# num_2 = int(input("Введи 2-е число: "))
#
# print(f'Сложение двух чисел = {num_1 + num_2}')
# print()

text = input("Введи строку: ")
# верхний регистр
upper_register = text.upper()
# нижний регистр
lower_register = text.lower()
# первая буква заглавная, остальные строчные
capitalize = text.capitalize()

print(f'(.upper()) верхний регистр - {text} = {upper_register}')
print(f'(.lower()) нижний регистр - {text} = {lower_register}')
print(f'(.capitalize()) первая буква заглавная, остальные строчные - {text} = {capitalize}')

