import random
import numpy as np
rngLst = input("Input the range you want shuffled and sorted (lower integer, higher integer, duplicates(True/False)) make sure to seperate the values with a comma and a space!\n").split(", ")

rngMin = int(rngLst[0])
rngMax = int(rngLst[1])

rng = rngMax - rngMin + 1
if rngLst[2] == 'True':
    lstToSort = np.random.choice([*range(rngMin, rngMax + 1)], rng, replace = True)
else: 
    lstToSort = [*range(rngMin, rngMax + 1)]

random.shuffle(lstToSort)


lst = [0] * rng

print(lst)


for i in lstToSort:

    print(i)
    lst[i - 1] += 1

print(lst)


lstToSort = []

for i in range(len(lst)):

    tmpLst = [i + 1] * lst[i]
    lstToSort.extend(tmpLst)

print(lstToSort)