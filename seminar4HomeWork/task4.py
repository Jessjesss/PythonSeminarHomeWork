# 4'. Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов
#  (значения от 0 до 100) многочлена и записать в файл многочлен степени k.(записать в строку)

# Пример:

# k=2 => 2*x^2 + 4*x + 5 или x^2 + 5 или 10*x**2
# k=3 => 2*x^3 + 4*x^2 + 4*x + 5

from random import randint

k = int(input('Введите натуральную степень k:'))

list_n = [randint(0,100)]
r_list = []

def Rand():
    while list_n[0] == 0:
        list_n[0] = randint(0,100)
    for i in range(1, k+1):
        list_n.append(randint(0,100)) 
    return list_n

def PolynomGenerate(list_n, r_list):
    if list_n[0] == 1:
        r_list.append(f'*x**{k}')
    else:
        r_list.append(f'{list_n[0]}*x**{k}')
    for i in range(1, k+1):
        if list_n[i] != 0:
            if list_n[i] > 0:
                r_list.append(' + ')
            if list_n[i] != 1:
                r_list.append(f'{list_n[i]}')
            if i != k and i != k-1:
                r_list.append(f'*x**{k-i}')
            elif i == k-1:
                r_list.append('*x')
    r_list = [str(i) for i in r_list]
    res_list = ''.join(r_list)
    return res_list


Rand()
with open('file4.txt', 'w') as f:
    f.write(PolynomGenerate(list_n, r_list))

list_n = [randint(0,100)]
r_list = []
Rand()

with open('file5.txt', 'w') as s:
    s.write(PolynomGenerate(list_n, r_list))
