# Дано вещественное число x. Проверьте, является ли оно положительным или отрицательным.
# Формат входных данных: дано одно вещественное число number. Гарантируется, что number ≠ 0.
# Формат выходных данных: Требуется вывести тип числа текстом

number = float(input("Введите число: "))  # Считываем вещественное число
if number>0:
    print("положительное")
else:
    print("отрицательное")

