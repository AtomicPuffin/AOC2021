import os
import sys
os.chdir("/Users/andreas/Documents/GitHub/AOC2021/")
#print(os.getcwd())

#print(open("input2.txt").readlines())

plan = open("input2.txt").readlines()
distance = 0
depth = 0
aim = 0
for i in plan:
    t = i.split()[0]
    n = int(i.split()[1])
    if t == "forward":
        distance += n
        depth = depth + aim * n
    if t == "down":
        aim = aim + n
    if t == "up":
        aim = aim - n

print(distance * depth)






