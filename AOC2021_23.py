import os
import sys
import math
import ast
import re

from collections import Counter
#from queue import PriorityQueue
import itertools
#from itertools import starmap
import numpy as np
#import statistics
os.chdir("/Users/andreas/Documents/GitHub/AOC2021/")
input = [x.rstrip() for x in open("input22.txt").readlines()]
input2 = [x.rstrip() for x in open("input22 copy.txt").readlines()]
input3 = [x.rstrip() for x in open("input22 copy 2.txt").readlines()]
input4 = [x.rstrip() for x in open("input22 copy 3.txt").readlines()]


def readLines(lines):
    instructions = []
    for i in lines:
        coor = i.split()[1]
        onf = 1 if i.split()[0] == 'on' else 0
        coor = coor.split(',')
        x = coor[0][2:]
        y = coor[1][2:]
        z = coor[2][2:]
        x1,x2 = x.split('..')
        y1,y2 = y.split('..')
        z1,z2 = z.split('..')
#        cube  = (int(x1) <= x <= int(x2)) & (int(y1) <= y <= int(y2)) & (int(z1) <= z <= int(z2))
 #       instructions.append(onf, cube)
        instructions.append((onf, int(x1), int(x2), int(y1), int(y2), int(z1), int(z2)))
    return instructions

def overlapping(a,b):
    corners = [[0,0,0], [1,1,1], [0,0,1], [0,1,0], [1,0,0], [0,1,1], [1,0,1], [1,1,0]]
    for i in corners: # bs corner in a
        if (a[1] <= b[1+i[0]] <= a[2] and 
            a[3] <= b[3+i[1]] <= a[4] and 
            a[5] <= b[5+i[2]] <= a[6]):
            return i
    for i in corners:    
        if (b[1] <= a[1+i[0]] <= b[2] and 
            b[3] <= a[3+i[1]] <= b[4] and 
            b[5] <= a[5+i[2]] <= b[6]):
            return i
    return []

inps = readLines(input)
off = [i for i in inps if i[0] == 0]
on = [i for i in inps if i[1]]

print (len(off))

off2 = []
for i in range(len(off)):
    test = True
    for y in range(len(off)):
        if i != y:
            if (off[y][1] <= off[i][1] <= off[i][2] <= off[y][2] and
                off[y][3] <= off[i][3] <= off[i][4] <= off[y][4] and
                off[y][5] <= off[i][5] <= off[i][6] <= off[y][6]):
                test = False
    if test:
        off2.append(i)
print(len(off2))





# add cube | cube 

