# Напишите функцию, создающую(возвращающую) список заданной длины заполненный
# произвольными целыми числами в заданном диапазоне.
# , где size - размер генерируемого списка c элементами в диапазоне от of до to.

import random
def gen_list(size, of, to):
    random_list = []
    for _ in range(size):
        random_list.append(random.randint(of, to))
    return random_list
print(gen_list(3,0,10))

