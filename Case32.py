# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
from random import randint

n = int(input())
elmax = int(input())
elmin = int(input())
s = list(randint(1,10) for i in range (n))
print(*s)
spis = []
for i in range(n):
    if elmin<=s[i]<=elmax:
        spis.append(i)
    
print(*spis)