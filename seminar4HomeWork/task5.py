# 5'. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

# В file1.txt :
# 2*x**2 + 4*x + 5

# В file2.txt:
# 4*x**2 + 1*x + 4

# Результирующий файл:
# 6*x**2 + 5*x + 9

import sympy
x = sympy.symbols('x')

with open('file4.txt', 'r') as f:
    p1 = f.read()
    print(f' Первый многочлен: {p1}')

with open('file5.txt', 'r') as f2:
    p2 = f2.read()
    print(f' Второй многочлен: {p2}') 

sum_p = sympy.simplify(p1 + '+' + p2)
sum_p = str(sum_p)

with open('task5result.txt', 'w') as f:
    f.write(sum_p)