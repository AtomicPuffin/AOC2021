import os
import sys
import itertools
#import numpy as np
#import statistics
os.chdir("/Users/andreas/Documents/GitHub/AOC2021/")
input = open("input9.txt").readlines()
#input = open("input9 copy.txt").readlines()

zero = [0,1,2,4,5,6]
one = [2,5]
two = [0,2,3,4,6]
three = [0,2,3,5,6]
four = [1,2,3,5]
five = [0,1,3,5,6]
six = [0,1,3,4,5,6]
seven = [0,2,5]
eight = [0,1,2,3,4,5,6]
nine = [0,1,2,3,5,6]

numbers = [zero, one,two,three,four,five,six,seven,eight,nine]
full_set = ['a','b','c','d','e','f','g']

possibilities = [['a','b','c','d','e','f','g'] for x in range(7)]

def read_lines(lines):
    return [i.split() for i in lines]

def update(word, pos, ls):
    for i in ls:
        pos[i] = [value for value in word if value in pos[i]]
    return pos

def find_key(line, p):
    line = sorted(line[:10], key=len)
    pos = p.copy()
    fivec = ''
    sixc = ''

    for y in line:
        if len(y) == 2:
            pos = update(y,pos, [2,5])
        elif len(y) == 3:
            pos = update(y,pos, [0,2,5])
        elif len(y) == 4:
            pos = update(y,pos, [1,2,3,5])
        elif len(y) == 5:
            fivec += y
        elif len(y) == 6:
            sixc += y

    five1 = ''
    five2 = ''
    five3 = ''
    six2 = ''
    six3 = ''
    for i in pos[6]:
        if fivec.count(i) == 1:
            five1 += i
        elif fivec.count(i) == 2:
            five2 += i
        elif fivec.count(i) == 3:
            five3 += i
        else:
            print('beeeep')
            
        if sixc.count(i) == 2:
            six2 += i
        elif sixc.count(i) == 3:
            six3 += i
        else:
            print('boooop')

    pos = update(five1,pos, [1,4])
    pos = update(five2,pos, [2,5])
    pos = update(five3,pos, [0,3,6])
    pos = update(six2,pos, [2,3,4])
    pos = update(six3,pos, [0,1,5,6])

    
    for i in range(len(pos)):
        if len(pos[i]) != 1:
            for y in pos[i]:
                if [y] in pos:
                    pos[i].remove(y)
                    exit


    return pos

def decode(line,key):
    num = []
    for i in line[11:15]:
        temp = [key.index([y]) for y in i]
        x = numbers.index(sorted(temp))
        num.append(x)
    return int(''.join((map(str,num))))

total = 0
for i in read_lines(input):
    k = find_key(i, possibilities)
    total += decode(i,k)

print(total)
