# 5'. Реализуйте алгоритм перемешивания списка.

# import random

# list_l = [3, 6, 9, 22, 5, 112, 6, 8, 4]
# print(f'Заданный список: {list_l}')

# for i in range(len(list_l)-1, 0, -1):
#     j = random.randint(0, i + 1) 
#     list_l[i], list_l[j] = list_l[j], list_l[i]
# print(f'Перемешанный список: {list_l}')


#Улучшение:


from random import random
list_l = [3, 6, 9, 22, 5, 112, 6, 8, 4]
shuffled_list = sorted(list_l, key=lambda x: random())
print(shuffled_list)