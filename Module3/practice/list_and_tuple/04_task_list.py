# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.

# TODO: your code here
numbers = [-5,4,3,-10,10]
summa=0
for el in numbers:
    if el>0:
        summa=el+summa
print(summa)
