# Даны два списка одинаковой длины. Необходимо создать из них словарь таким образом,
# чтобы элементы первого списка были ключами, а элементы второго — соответственно значениями нашего словаря.

keys = ['name', 'surname', 'age', 'rate']
values = ['Петр', 'Первый', 42, 1300]

# TODO: your code here
# Нужно получить словарь:
# {'name': 'Петр', 'surname': 'Первый', 'age': 42, 'rate': 1300}
keys = ['name', 'surname', 'age', 'rate']
values = ['Петр', 'Первый', 42, 1300]
i = 0
people = {
    keys[0]: values[0],
    keys[1]: values[1],
    keys[2]: values[2],
    keys[3]: values[3]
}
print(people)
print(people['name'])
