import os
import sys
#import numpy as np
os.chdir("/Users/andreas/Documents/GitHub/AOC2021/")
input = open("input5.txt").readlines()
#input = open("input5ex.txt").readlines()


def create_sea():
    temp = []
    for i in range(1000):
        temp.append([])
        for y in range(1000):
            temp[i].append(0)
    return temp

def read_lines(lines):
    output = []
    for i in lines:
        output.append( [int(i.split()[0].split(",")[0]),int(i.split()[0].split(",")[1]),int(i.split()[-1].split(",")[0]),int(i.split()[-1].split(",")[1])])
    return output

def filter_lines_v(lines):
    output = []
    for i in lines:
        if i[0] == i[2] or i[1] == i[3]:
            output.append(i)
    return output

def filter_lines_d(lines):
    output = []
    for i in lines:
        dx = abs(i[0]-i[2])
        dy = abs(i[1]-i[3])
        if dx == dy:
            output.append(i)
    return output

def update_v(lines, seamap):
    for i in lines:
        x1 = i[0]
        x2 = i[2]
        y1 = i[1]
        y2 = i[3]

        if x1 == x2 and y1 == y2:
            seamap[x1][y1] += 1

        elif x1 == x2:
            if y1 < y2:
                d = y2 - y1 +1
                for t in range(d):
                    seamap[x1][(y1+t)] += 1
            else:
                d = y1 - y2 +1
                for t in range(d):
                    seamap[x1][(y2+t)] += 1
        elif x1 < x2:
            d = x2 - x1 +1
            for t in range(d):
                seamap[(x1+t)][y1] += 1
        else:
            d = x1 - x2 +1
            for t in range(d):
                seamap[(x2+t)][y2] += 1
        
def update_d(lines, seamap):
    for i in lines:
        x1 = i[0]
        x2 = i[2]
        y1 = i[1]
        y2 = i[3]
        dx = abs(x1-x2)+1
        if x1 < x2:
            if y1 < y2:
                for t in range(dx):
                    seamap[x1+t][y1+t] += 1
            else:
                for t in range(dx):
                    seamap[x1+t][y1-t] += 1
        else:
            if y1 < y2:
                for t in range(dx):
                    seamap[x1-t][y1+t] += 1
            else:
                for t in range(dx):
                    seamap[x1-t][y1-t] += 1

def count(seamap):
    counter = 0
    for x in seamap:
        for y in x:
            if y > 1:
                counter += 1
    return counter


ventlines = read_lines(input)
#print(ventlines)
seamap = create_sea()
ventlinesV = filter_lines_v(ventlines)
ventlinesD = filter_lines_d(ventlines)
update_v(ventlinesV,seamap)
update_d(ventlinesD,seamap)



#print(ventlinesV)
#print(ventlinesD)
#print(seamap)
print(count(seamap))

