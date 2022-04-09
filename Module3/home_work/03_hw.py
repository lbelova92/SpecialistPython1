# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

# TODO: your code here
from random import randint
n=int(input('n:'))
k=0
summa=0
numbers=[]
for i in range(n):
    numbers.append(randint(-100,100))
print(numbers)
#print(numbers[0])
while k<n:
    if numbers[k]>0 and numbers[k]%2==0:
        summa=summa+numbers[k]
    else:
        summa=summa
    k+=1
print(summa)
