# Напишите функцию, находящую среднее арифметическое всех аргументов
# Функция должна вызываться с любым количеством аргументов

def average(*args):
    summa=0
    for argument in args:
        summa=summa+argument
    summa_avg=summa/len(args)
    return summa_avg
print(average(2,2,2))


print(average(3, 4, 8))
print(average(1, 4, 5, -3, 8, 4))
print(average(-10, 12, 6.3, -5.5, 7, 0.2))
