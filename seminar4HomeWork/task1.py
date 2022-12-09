# 1'. Вычислить число Пи c заданной точностью d

# *Пример:* 

# - при d = 0.001, π = 3.141
# - при d = 0.0001, π = 3.1415  

import math
d = input('Задайте точность: ')
if ('.') in d or (',') in d:
    d = d.replace('.', '').replace(',', '')
    d = len(d)-1
else:
    d = int(d)
print(round(math.pi, d))

