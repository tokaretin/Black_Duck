from operator import index

#список
numbers1 = []
numbers2 = list()

# Обращение к элементам списка
people = ["Tom", "Sam", "Bob"]
# получение элементов с начала списка
print(people[0])  # Tom
print(people[1])  # Sam
print(people[2])  # Bob
# получение элементов с конца списка
print(people[-2])  # Sam
print(people[-1])  # Bob
print(people[-3])  # Tom

people[2] = "Ilia" # меняю Bob на Ilia
print(people[2])
print(people)
print()

#Перебор с помощью цикла for:
num = 0
peopleAll = ["Tom", "Sam", "Bob"]

# m = index()
# print(m)
for person in people:
    num += 1
    print(f'Перебор {num}-й {person}')
print()

#Перебор с помощью цикла while
people = ["Tom", "Sam", "Bob"]
i = 0
while i < len(people):
    print(people[i])    # применяем индекс для получения элемента
    i += 1
print()


some_l = [1, 2, 4, 9.0, "Cat", [321, 123], ('Trueeee')]  # list изменяемый и упорядоченнй тип данных(коллекция данных)
some_s = {1, 3, 3, True, False, 0, 4, 5, 2, 324, 36453, (32,3421)}  # set изменеямая и неупорядоченная коллекция уникальных элементов
some_t = (1, 3, 'Tr', [31])  # tuple неизменяемый и упорядоченный
some_d = {}  # dict изменяемый и упорядоченный

# print(some_l[len(some_l)//2:-1])
# some_l.append(5)
# del some_l[1]

# print(type(arr))
# print(type(some_l))
# some_s.add(43)
# some_s.add(32)

print(some_s)