import os
import sys
import itertools
#import numpy as np
#import statistics
os.chdir("/Users/andreas/Documents/GitHub/AOC2021/")
input = open("input11.txt").readlines()
#input = open("input11 copy.txt").readlines()

octis = [[int(num) for num in word.rstrip()] for word in input ]

#print (octis)



def stepOne(oct):
    for y in oct:
        for x in range(len(y)):
            y[x] += 1

def flash(oct,tens):
#    print(tens)
    for n in tens:
#        print(n)
        for i in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]: # l's p[ att g;ra programmatiskt]
            
            y = n[0] + i[0]
            x = n[1] + i[1]
#            print(y,x)
            if 0 <= y <= 9 and 0 <= x  <= 9:
#                print(y,x)
                oct[y][x] += 1
 #               print(oct[y][x])
                if oct[y][x] == 10:
                    tens.append((y,x))
#            flash (oct,y+i[0],x+i[1])

def stepTwo(oct):
    tens = []
    for y in range(len(oct)):
        for x in range(len(oct[0])):
            if oct[y][x] == 10:
                tens.append((y,x))
#    tens = [(0,2)]
    if tens:
        flash(oct,tens)

def stepThree(oct, counter):
    fla = 0
    for y in oct:
        for x in range(len(y)):
            if y[x] > 9:
                y[x] = 0
                fla += 1
#    print (fla)
    counter+= 1
    if fla == 10*10:
        print(counter)
    return counter
#    return fla

flashes  = 0

counter = 0
for i in range(1000):
    stepOne(octis)
    stepTwo(octis)
#    flashes += stepThree(octis, counter)
    counter = stepThree(octis, counter)

#print(counter)
#print(flashes)
#print(octis)
