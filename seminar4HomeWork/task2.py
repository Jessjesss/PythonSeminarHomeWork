# 2'. Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

# * 6 -> [2,3]
# * 144 -> [2,3]

import sympy
n = int(input('Введите натуральное число n: '))
list_s = list(sympy.primerange(n))
res = []
for i in range(len(list_s)):
    if n % list_s[i] == 0:
        res.append(list_s[i])
    else:
        i += i
print(res)
