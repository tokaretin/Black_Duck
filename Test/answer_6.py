# С помощью for выведи числа от 1 до 20.
for i in range(1, 21):
    print(i)
print()

# С помощью while выведи числа от 10 до 1.
n = 10
while n >= 1:
    print(n)
    n -= 1
print()

# Выведи таблицу умножения для числа 5.
for i in range(1, 10):
    print(f'5 * {i} = {5 * i}')
print()

# Спроси у пользователя число и посчитай факториал (n!).
num = int(input("Введите число: "))

factorial = 1

for i in range(1, num + 1):
    factorial *= i
print(f'Факториал числа {num}! = {factorial}')