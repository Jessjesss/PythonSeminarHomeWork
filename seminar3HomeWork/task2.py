# 2'. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list_p = [3, 1, 7, 2, -8, 5, 4, 7]
prod = []
if len(list_p) % 2 == 0:
    length = (len(list_p)//2)
else:
    length = (len(list_p)//2+1)
for i in range(0, length):
    prod.append(list_p[i] * list_p[-i -1])
print(f'Заданный список: {list_p}')
print(f'Произведение пар чисел списка: {prod}')

# for i in range(len(list_p)):
#     for j in range(len(list_p), -1, 1):
#         print(list_p[i] * list_p[j])


