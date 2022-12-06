# 1'. Вычислить число Пи c заданной точностью d

# *Пример:* 

# - при d = 0.001, π = 3.141
# - при d = 0.0001, π = 3.1415  

import math
d = input('Задайте точность: ')
d = d.replace('.', '').replace(',', '')
print(d)
# print(round(math.pi, d))

