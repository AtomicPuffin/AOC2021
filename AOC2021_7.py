import os
import sys
#import numpy as np
import statistics
os.chdir("/Users/andreas/Documents/GitHub/AOC2021/")
input = open("input7.txt").readlines()
#input = open("input7ex.txt").readlines()


def read_lines(lines):
    output = []
    for i in lines[0].split(","):
        output.append(int(i))
    return output

crabs = read_lines(input)
crabs.sort()
#med = statistics.median(crabs)
med = round(sum(crabs) / len(crabs))
med = med-1

result = 0
for i in crabs:
#    result += abs(i - med)
    temp = abs(i - med)
    for i in range(temp):
        result += i+1

print(result)


