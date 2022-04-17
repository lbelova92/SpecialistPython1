# Найдите количество чисел являющихся палиндромами в диапазоне от a до b включительно
# Известно, что a и b целые положительные числа.

def palindrome(number):
    return str(number) == str(number)[::-1]


a = 10
b = 85
num_palindromes = 0

for num in range(a,b+1):
        if palindrome(num):
            num_palindromes = num_palindromes + 1
print(num_palindromes)
