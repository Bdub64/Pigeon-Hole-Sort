import random

rngLst = input("Input the range you want shuffled and sorted (lower integer, higher integer) make sure to seperate the two values with a comma and a space!").split(", ")

random.shuffle(range(rngLst[0], rngLst[1]))

