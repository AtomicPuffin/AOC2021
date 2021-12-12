import os
import sys
import itertools
#import numpy as np
#import statistics
os.chdir("/Users/andreas/Documents/GitHub/AOC2021/")
input = open("input12.txt").readlines()
#input = open("input12 copy.txt").readlines()

        # if a, b in paths, append value
        # else append key value
def buildMap(lines):
    cmap = {}
    for i in lines:
        a = i.split('-')[0].rstrip()
        b = i.split('-')[1].rstrip()
        if a in cmap:
            cmap[a].append(b)
        else:
            cmap[a] = [b]
        if b in cmap:
            cmap[b].append(a)
        else:
            cmap[b] = [a]
    return cmap

# om node lower och redan i tree g;r inget
# 

'''
def buildTree(cmap, forest, path, node):
    p2 = path.copy()
    p2.append(node)
    if node == 'end':
        forest.append(p2)
    else:
        for i in cmap[node]:
            if not i.islower() or i not in path:
                buildTree(cmap,forest,p2,i)

'''

#buid tree structure recursively
#add magic for single time burn to tree
def buildTree(cmap, forest, path, node, magic):
    p2 = path.copy()
    p2.append(node)
    if node == 'end':
        forest.append(p2)
    else:
        for i in cmap[node]:
            if not i.islower():
                buildTree(cmap,forest,p2,i, magic)
            elif i not in path:
                buildTree(cmap,forest,p2,i, magic)                
            elif magic == '' and i != 'start':
                buildTree(cmap,forest,p2,i,'####')



forest = []

m = buildMap(input)

#print(m)

buildTree(m,forest,[],'start','')

#print(forest)

print(len(forest))