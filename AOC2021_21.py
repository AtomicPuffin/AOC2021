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
input = [x.rstrip() for x in open("input19.txt").readlines()]
input2 = [x.rstrip() for x in open("input19 copy.txt").readlines()]


pos1 = 8
pos2 = 1
#pos1 = 4
#pos2 = 8

deltas = []

for x in range(3):
    for y in range(3):
        for z in range(3):
            deltas.append(x+1+y+1+z+1)
t = {}
for i in deltas:
    if i in t:
        t[i] += 1
    else:
        t[i] = 1

deltas = t

# each turn creates 3^3 universes

def qturn(turn,score1,score2,pos1,pos2):
    if score1 >= 21:
        return [1,0]
    elif score2 >= 21:
        return [0,1]
    if turn == 1:
        res = [0,0]
        for i in range(3,10): # dont calculate identical dimensions, just multiply them
            pos = ((pos1 +i -1) % 10)+1
            t = qturn(2, score1 +pos, score2, pos, pos2)
            res[0] += t[0]*deltas[i]
            res[1] += t[1]*deltas[i]
        return res
    elif turn == 2:
        res = [0,0]
        for i in range(3,10):
            pos = ((pos2 +i -1) % 10)+1
            t = qturn(1, score1, score2 +pos, pos1, pos)
            res[0] += t[0]*deltas[i]
            res[1] += t[1]*deltas[i]
        return res

print(qturn(1,0,0,pos1,pos2))


#print(deltas)


''' Part 1

player1 = 0
player2 = 0
board = (1,10)
#pos1 = 8
#pos2 = 1
pos1 = 4
pos2 = 8
rolls = 0

turn = 1 # starting turn

dierolls = []

while player1 < 1000 and player2 < 1000:
    if len(dierolls) < 5:
        dierolls += [i+1 for i in range(100)]
    if turn == 1:
        pos = ((pos1 +dierolls.pop(0) +dierolls.pop(0) +dierolls.pop(0) -1) % 10)+1
        rolls += 3
        player1 += pos
        pos1 = pos
        print('p1 ' + str(player1)) 
        turn = 2
    elif turn == 2:
        pos = ((pos2 +dierolls.pop(0) +dierolls.pop(0) +dierolls.pop(0) -1) % 10)+1
        rolls += 3
        player2 += pos
        pos2 = pos
        turn = 1
        print('p2 ' + str(player2))


print(player1)
print(player2)
print(rolls)
print(min(player1,player2)*rolls)

'''