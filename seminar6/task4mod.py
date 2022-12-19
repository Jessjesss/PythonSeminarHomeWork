# 4'. Задайте список из N элементов, 
# заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
# (для продвинутых - с файлом, вариант минимум - ввести позиции в консоли)

# -2 -1 0 1 2
# Позиции: 0,1 -> 2

# with open('file.txt','r') as f:
#     a = int(f.readline())
#     b = int(f.readline(2))
#     c = int(f.readline(3))

# n = int(input('Введите N: '))
# list_n = []
# for i in range(-n, n+1):
#     list_n.append(i)

# result = list_n[a] * list_n[b] * list_n[c]
# print(f'Список элементов от -n до n: {list_n}')
# print(f'Позиции элементов из файла: {a, b, c}')
# print(f'Произведение элементов: {result}')



#Улучшение:

with open('file.txt','r') as f:
    a = int(f.readline())
    b = int(f.readline(2))
    c = int(f.readline(3))

n = int(input('Введите N: '))
list_n = [i for i in range(-n, n+1)]

result = list_n[a] * list_n[b] * list_n[c]
print(f'Список элементов от -n до n: {list_n}')
print(f'Позиции элементов из файла: {a, b, c}')
print(f'Произведение элементов: {result}')

