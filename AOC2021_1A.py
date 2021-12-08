# AOC 1 A

import os
os.chdir("/Users/andreas/Documents/GitHub/AOC2021/")
#print(os.getcwd())

#print(open("input1A.txt").readlines())

measurements = open("input1A.txt").readlines()
prev = 999999
counter = 0
for i in measurements:
    if int(i) > prev:
        counter += 1
    prev = int(i)
print(counter)






