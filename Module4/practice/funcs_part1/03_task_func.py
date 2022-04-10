# Даны координаты двух точек на плоскости.
# Напишите функцию нахождения расстояния между двумя точками.


    def distance(x1, y1, x2, y2):
    d=(2*(x1-x2)+2*(y1-y2))**0.5
    return d
x1=12
y1=8
x2=12
y2=6
res=distance(x1, y1, x2, y2)
print(res)


# Тестируем функцию
print(distance(2, 4, 2, 9))
print(distance(12, 8, 12, -9))
print(distance(23, 0, 15, 32))
