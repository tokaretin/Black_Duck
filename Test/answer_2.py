# Создай переменные: age = 12, height = 1.65, name = "Иван", is_student = True.
# Выведи их с поясняющим текстом: Имя: Иван, Возраст: 12.
# Измени значение переменной age на 13 и выведи снова.
# Преобразуй float в int и наоборот.

age = 12
height = 1.65
name = "Иван"
is_student = True

print(f'Имя: {name}, Возврат: {age}, Рост: {height} , Студент: {is_student}')

age = 13

print(f'Новый возраст: {age}')

print(f'Преобразование float в int: height = {int(height)}')
print(f'Преобразование int в float: age = {float(age)}')
