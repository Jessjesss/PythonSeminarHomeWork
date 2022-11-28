# Напишите программу, которая принимает на вход
#  вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

number = input('Введите вещественное число: ')
str_number = number.replace('.', '').replace(',', '').replace('-', '')
result = sum(map(int, list(str_number)))
print(f"Сумма цифр числа: {result}")