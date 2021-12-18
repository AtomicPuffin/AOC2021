import os
import sys
import math
#from queue import PriorityQueue
#import itertools
#from itertools import starmap
#import numpy as np
#import statistics
os.chdir("/Users/andreas/Documents/GitHub/AOC2021/")
input = [x.rstrip() for x in open("input16.txt").readlines()]
input2 = [x.rstrip() for x in open("input16 copy.txt").readlines()]
#input2 = 'D2FE28'

#hex translation table
hexBin = {'0' : '0000',
        '1' : '0001',
        '2' : '0010',
        '3' : '0011',
        '4' : '0100',
        '5' : '0101',
        '6' : '0110',
        '7' : '0111',
        '8' : '1000',
        '9' : '1001',
        'A' : '1010',
        'B' : '1011',
        'C' : '1100',
        'D' : '1101',
        'E' : '1110',
        'F' : '1111'}
'''
class Package:
    def __init__(self,ver,tID,cbit=2,val=0,tail=[]):
        self.ver = ver
        self.tID = tID
        self.cbit = cbit
        self.val = val
        self.tail = tail

    def parse(pack):
'''


#translate hex file to bin file
def hexToBin(lines):
    temp = [hexBin[i] for i in lines[0]]
    temp = ''.join(temp)
    return temp

#parses one package into data and subpackets
def readPackage(pack):
    tID = int(pack[3:6],2)
    pack = pack[6:]

    if tID == 4: # extract numeral
        val = ''
        while pack[0] == '1':
            val += pack[1:5]
            pack = pack[5:]
        val += pack[1:5]
        pack = pack[5:]
        val = int(val,2)
        return val, pack
    else: # operator
        val = []
        if pack[0] == '0': # 15 bits tell number of bits
            pack = pack[1:]
            dataRange = int(pack[:15],2)
            pack = pack[15:]
            data = pack[:dataRange]
            pack = pack[dataRange:]
            while len(data) > 6:
                n,data = readPackage(data)
                val.append(n)
            val = operate(val,tID)
            return val, pack
        else: # 11 bits tell number of packages
            pack = pack[1:]
            dataRange = int(pack[:11],2)
            pack = pack[11:]
            data = pack
            for _ in range(dataRange):
                n,data = readPackage(data)
                val.append(n)
            val = operate(val,tID)
            return val, data

def operate(val,tID):
    if tID == 0: # sum
        return sum(val)
    elif tID == 1: # product, multi or just val if 1
        return math.prod(val)
    elif tID == 2: # min
        return min(val)
    elif tID == 3: # max
        return max(val)
    elif tID == 5: # first greater than second
        return val[0] > val[1]
    elif tID == 6: # first lesser than second
        return val[0] < val[1]
    elif tID == 7: # first equal to second
        return val[0] == val[1]


binIn = hexToBin(input)
print(binIn)
n,data = readPackage(binIn)
print(n)
#print(vs+v)




'''
#Part one solution
#parses one package into data and subpackets
def readPackage(pack):
    ver = int(pack[:3],2)
    tID = int(pack[3:6],2)
    pack = pack[6:]

    if tID == 4: # extract numeral
        val = ''
        while pack[0] == '1':
            val += pack[1:5]
            pack = pack[5:]
        val += pack[1:5]
        pack = pack[5:]
        return ver, tID, val, pack, 0
    else: # operator
        versum = 0
        val = []
        if pack[0] == '0': # 15 bits tell number of bits
            pack = pack[1:]
            dataRange = int(pack[:15],2)
            pack = pack[15:]
            data = pack[:dataRange]
            pack = pack[dataRange:]
            while len(data) > 6:
                v,t,n,data,vs = readPackage(data)
                versum += vs + v
                val.append([v,t,n,data])
            return ver, tID, val, pack, versum
        else: # 11 bits tell number of packages
            pack = pack[1:]
            dataRange = int(pack[:11],2)
            pack = pack[11:]
            data = pack
            for _ in range(dataRange):
                v,t,n,data,vs = readPackage(data)
                versum += vs + v
                val.append([v,t,n,data])
            return ver, tID, val, data, versum

'''