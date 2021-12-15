import os
import sys
from queue import PriorityQueue
#import itertools
#from itertools import starmap
#import numpy as np
#import statistics
os.chdir("/Users/andreas/Documents/GitHub/AOC2021/")
input = open("input15.txt").readlines()
input2 = open("input15 copy.txt").readlines()
#input2 = ['1163751742']

# cmap {(y,x): local cost, distance to origin, visited}
# nv priority queue


# builds map with n copies
def buildMap(inp, n):
    nodes = {}
    maximum = len(inp)*(n+1)*100
    ond = (len(inp), len(inp[0]))
    end = (len(inp)*(n+1)-1, len(inp[0])*(n+1)-1)
# duplicate on x-axis
    for y in range(len(inp)):
        for x in range(len(inp[y])):
            nodes[(y,x)] = [int(inp[y][x]),maximum,False]
            temp = [( (y, x+(ond[1])*(i+1)) ,i+1) for i in range(n)]
            for t in temp:
                nodes[t[0]] = [(int(inp[y][x]) +t[1] -1) % 9 +1, maximum,False]
# duplicate on y-axis
    for y in range(len(inp)):
        for x in range(end[1]+1):
            temp = [( (y+(ond[0])*(i+1), x), i+1) for i in range(n)]
            for t in temp:
                nodes[t[0]] = [(nodes[(y,x)][0] +t[1] -1) % 9 +1, maximum,False]

    nodes[(0,0)] = [1,0,False]
    return nodes, end, maximum


# update all neighbours, add non visited to queue
def currentNode(cmap, nv, node, end):
    if node[1] == end:
        print(node[0])
    for i in [(1,0),(0,1),(-1,0),(0,-1)]:
        yx = (node[1][0]+i[0],node[1][1]+i[1])
        if yx in cmap:
            alt = node[0] + cmap[yx][0]
            if alt < cmap[yx][1]:
                cmap[yx][1] = alt
                if not cmap[yx][2]:
                    nv.put((alt,yx))
    cmap[node[1]][2] = True

inp = [i.rstrip() for i in input]
cmap, end, maximum = buildMap(inp, 4)
nv = PriorityQueue()
nv.put((0,(0,0)))
nv.put((maximum*2,end)) #fick skumma buggar n'r k'n blev tom f;rsta v'ndan, la till sp'ke

while not nv.empty():
    node = nv.get()
    currentNode(cmap, nv, node, end)
