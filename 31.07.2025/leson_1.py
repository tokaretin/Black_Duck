
def name_sur(name, surname):


    if name.isalpha() and surname.isalpha():
        print(f'Привет {name} твая фамилия как у меня {surname}')
    else:
        print("Error")

while True:
    name = input("Введите имя: ")
    surname = input('Ведите фамилию: ')

    name_sur(name, surname)
    if name == '0':
        break