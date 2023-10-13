import random
import numpy as np
import time

rngLst = input("Input the range you want shuffled and sorted (lower integer, higher integer, duplicates(True/False)) make sure to seperate the values with a comma and a space!\n").split(", ")

rngMin = int(rngLst[0])
rngMax = int(rngLst[1])

rng = rngMax - rngMin + 1

startShuffle = time.time()

if rngLst[2] == 'True':

    lstToSort = np.random.choice([*range(rngMin, rngMax + 1)], rng, replace = True)
    
else: 

    lstToSort = [*range(rngMin, rngMax + 1)]

random.shuffle(lstToSort)

endShuffle = time.time()
print("Shuffle took ", endShuffle - startShuffle, " seconds, or ", (endShuffle - startShuffle )* 1000, " miliseconds!")

lst = [0] * rng

print(lst)

startSort = time.time()
for i in lstToSort:

    lst[i - 1] += 1

endSort = time.time()
print("Sorting took ", endSort - startSort, " seconds, or ", (endSort - startSort) * 1000, " miliseconds!")

print(lst)


lstToSort = []

for i in range(len(lst)):

    tmpLst = [i + 1] * lst[i]
    lstToSort.extend(tmpLst)

startPrint = time.time()
print(lstToSort)
endPrint = time.time()

print("Shuffle took ", endShuffle - startShuffle, " seconds, or ", (endShuffle - startShuffle )* 1000, " miliseconds!")
print("Sorting took ", endSort - startSort, " seconds, or ", (endSort - startSort) * 1000, " miliseconds!")
print("printing took ", endPrint - startPrint, " seconds, or ", (endPrint - startPrint) * 1000, " miliseconds!")