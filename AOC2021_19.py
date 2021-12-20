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

# scanner x,y,z real position, range 1000 only sees beacons, dont know itself
# beacon position relative to scanner
# 12 common beacons = positioning of scanners relatively to eachother
# scanners unaware of rotation or where they face, integer multiple of 90 on all axises, 
#   24 different orientations
trans = [['x','y','-z'],['x','-z','-y'],['x','-y','z'],['x','z','y'],
        ['-x','y','z'],['-x','z','-y'],['-x','-y','-z'],['-x','-z','y'],
        ['y','z','-x'],['y','-x','-z'],['y','-z','x'],['y','x','z'],
        ['-y','z','x'],['-y','x','-z'],['-y','-z','-x'],['-y','-x','z'],
        ['z','y','x'],['z','x','-y'],['z','-y','-x'],['z','-x','y'],
        ['-z','y','-x'],['-z','-x','-y'],['-z','-y','x'],['-z','x','y']]
'''
perms = [[x,y,-z],[x,-z,-y],[x,-y,z],[x,z,y],[-x,y,z],[-x,z,-y],[-x,-y,-z],[-x,-z,y],
                        [y,z,-x],[y,-x,-z],[y,-z,x],[y,x,z],[-y,z,x],[-y,x,-z],[-y,-z,-x],[-y,-x,z],
                        [z,y,x],[z,x,-y],[z,-y,-x],[z,-x,y],[-z,y,-x],[-z,-x,-y],[-z,-y,x],[-z,x,y]]
'''
class Scanner:
    def __init__(self, id, beacons, coord=(0,0,0), key=[], found=False):
        self.id = id
        self.beacons = beacons
        self.xs = [i[0] for i in beacons]
        self.ys = [i[1] for i in beacons]
        self.zs = [i[2] for i in beacons]
        self.coord = coord
        self.key = key
        self.found = found

def parse(lines): # find scanner number, list of beacons, repeats
    scanners = []
    no = 0
    beacons = []
    for i in lines:
        if i == '':
            scanners.append(Scanner(no,beacons))
            beacons = []
        elif i[:3] == '---':
            res = re.findall(r'\d', i)
            no = int(''.join(res))
        else:
            b = [int(n) for n in i.split(',')]
            beacons.append(b)
    scanners.append(Scanner(no,beacons))
    return scanners

def transp(perm, beac):
    res = []
    for i in range(3):
        if perm[i] == 'x':
            res.append(beac[0])
        elif perm[i] == '-x':
            res.append(-beac[0])
        elif perm[i] == 'y':
            res.append(beac[1])
        elif perm[i] == '-y':
            res.append(-beac[1])
        elif perm[i] == 'z':
            res.append(beac[2])
        elif perm[i] == '-z':
            res.append(-beac[2])
    return res

def overlap(deltas): 
    cs = {}
    for i in deltas:
        if i in cs:
            cs[i] += 1
        else:
            cs[i] = 1
    a = max(cs, key=lambda key: cs[key])
    return a, cs[a]

def delta(s1,s2):
    if s2.found:
        return [], []
    for i in trans:
        deltas = []
        for a in s1.beacons:
            for b in s2.beacons:
                c = transp(i,b)
                d = np.add(c,a)
                deltas.append(tuple(d))
        t1,t2 = overlap(deltas)
        
        if t2 >= 12:
            return i, t1
    return [], []

def alignToZero(scan, key, pos):
    scan.coord = pos
    scan.found = True
    scan.key = key
    for i in range(len(scan.beacons)):
        scan.beacons[i] = transp(key,scan.beacons[i])
        scan.beacons[i] = np.add(scan.beacons[i],[-pos[0],-pos[1],-pos[2]]).tolist()
        scan.beacons[i] = [-scan.beacons[i][0],-scan.beacons[i][1],-scan.beacons[i][2]]

def manhattan(a, b):
    return sum(a[i]-b[i] for i in range(3))

def mapping(scanners):
    manlist = []
    done = False
    while not done:
        done = True
        for i in scanners:
            done = done and i.found
            if not i.found:
                for y in scanners:
                    if i.id != y.id and y.found:
                        tr, delt = delta(y, i)
                        if tr != []:
                            print(y.id)
                            print(i.id)
                            print(delt)
                            manlist.append(delt)
                            alignToZero(i, tr, delt)
    return manlist

def one(scanners):
    bacon = {}
    for i in scanners:
        for y in i.beacons:
            bacon[tuple(y)] = 1
    print(len(bacon))

def two(mlst):
    max = 0
    for i in trans:
        mlst2 = [transp(i,a) for a in mlst]
        for x in mlst2:
            for y in mlst2:
                m = manhattan(x,y)
                if m > max:
                    max = m
    print(max)




scanners = parse(input)
scanners[0].found = True


mlst = mapping(scanners) # long execution, for quick 2 use list below

#mlst = [(1223, 70, 51), (121, 59, 1161), (2424, 63, -84), (1196, 136, 1154), (1237, 35, 2494), (3636, -14, 32), (2358, 1199, 109), (2447, 102, 1272), (2421, 2441, -58), (2466, -1122, 1248), (2506, 3761, -69), (2429, 2425, 1139), (2398, 1198, -1121), (2443, 2573, -1107), (2334, 3615, -1133), (2347, 3685, -2300), (1145, 3692, -20), (3538, 3759, -1179), (2345, 1201, -2314), (1140, 4845, -40), (3576, 4810, -1126), (3554, 2522, -1257), (2338, 4825, -1102), (2421, 149, -2436), (2422, 3589, -3627), (3673, 4909, 82), (3721, 6179, -1182), (4813, 4920, -1162), (4917, 2507, -1229), (1323, 172, -2380)]

mlst.append((0,0,0))

one(scanners)
two(mlst)
