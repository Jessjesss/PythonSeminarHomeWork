# 4'. Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

number = int(input('Введите номер четверти: '))

if (number == 1):
    print('Диапозон возможных координат точек x: от 0 до ∞, y: от 0 до ∞')
elif (number == 2):
    print('Диапозон возможных координат точек x: от 0 до -∞, y: от 0 до ∞')
elif (number == 3):
    print('Диапозон возможных координат точек x: от 0 до -∞, y: от 0 до -∞')
elif (number == 4):
    print('Диапозон возможных координат точек x: от 0 до ∞, y: от 0 до -∞')
else:
    print('Введите номер четверти от 1 до 4')