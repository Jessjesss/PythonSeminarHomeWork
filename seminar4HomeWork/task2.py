# 2'. Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

# * 6 -> [2,3]
# * 144 -> [2,3]

import sympy
n = int(input('Введите натуральное число n: '))

list(sympy.primerange(0, 100))
print(list)