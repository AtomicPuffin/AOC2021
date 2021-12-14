import os
import sys
#import itertools
#from itertools import starmap
#import numpy as np
#import statistics
os.chdir("/Users/andreas/Documents/GitHub/AOC2021/")
input = open("input14.txt").readlines()
#input = open("input14 copy.txt").readlines()

def readLines(lines):
    start = {}
    temp1 = lines.pop(0).rstrip()
    temp2 = [temp1[i:i+2] for i in range(len(temp1[1:]))]
    for i in temp2:
        start[i] = start.get((i),0) + 1
    lines.pop(0)
    pins = {i[:2]: i.rstrip()[-1] for i in lines}
    return start, pins
        
def insert(start, pins):
    end = {}
    for i in start:
        if i in pins:
            i2 = ''.join([i[0],pins[i]])
            i3 = ''.join([pins[i],i[1]])
            end[i2] = end.get((i2),0) + start[i]
            end[i3] = end.get((i3),0) + start[i]
        else:
            end[i] = end.get((i),0) + start[i]
    return end

def spin(start, pins, spins):
    for _ in range(spins):
        start = insert(start, pins)
    return start

def calc1(end):
    result = {}
    for i in end:
        result[i[0]] = result.get((i[0]),0) + end[i]/2
        result[i[1]] = result.get((i[1]),0) + end[i]/2
        print(result)
    most = max(result, key=result.get)
    least = min(result, key=result.get)
    return result[most] - result[least]



s, p = readLines(input)

end = spin(s, p, 40)

#print(end)
print(calc1(end))
