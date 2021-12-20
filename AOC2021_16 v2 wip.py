import os
#import sys
import math
#from typing import TypeAlias
#from queue import PriorityQueue
#import itertools
#from itertools import starmap
#import numpy as np
#import statistics
os.chdir("/Users/andreas/Documents/GitHub/AOC2021/")
input = [x.rstrip() for x in open("input16.txt").readlines()]
#input2 = [x.rstrip() for x in open("input16 copy.txt").readlines()]
#input2 = 'C200B40A82'
#input2 = '04005AC33890'
#input2 = '880086C3E88112'
#input2 = 'CE00C43D881120'
#input2 = 'D8005AC2A8F0'
#input2 = 'F600BC2D8F'
#input2 = '9C005AC2F8F0'
input2 = ['9C0141080250320F1802104A08']


class Package:
    def __init__(self,data):
        self.data = data[6:]
        self.ver = int(data[:3],2)
        self.id = int(data[3:6],2)
        self.content = self.getVal() if self.id == 4 else self.unpack()
        self.end = self.content[-1]

    def unpack(self):
        content = []
        print (self.data)
        print('unpack')
        if self.data[0] == '0': # 15 bits tell number of bits
            print('is0')
            end  = (int(self.data[1:16],2)+16)
            print(int(self.data[1:16],2))
            toRead = self.data[16:end]
            print(toRead)
            while len(toRead) > 6:
                p = Package(toRead)
                content.append(p)
                toRead = toRead[p.end:]  
        else: # 11 bits tell number of packages
            print('is1')
            toRead = self.data[12:]

            noOfPackages = int(self.data[1:12],2)
            print(noOfPackages)
            
            for _ in range(noOfPackages):
                print('#')
                print(toRead)
                p = Package(toRead)
                content.append(p)
                end = p.end
                print('end')
                print (end)
                toRead = toRead[end:]
                #print(toRead)
        content.append(end)            
        return content

    def getVal(self):
        val = ''
        print('val')
        tail = self.data
        print(tail)
        end = 6
        while True:
            val += tail[1:5]
            bit = tail[0]
            tail = tail[5:]
            end += 5
            if bit == '0':
                break
        val = int(val,2)
        return [val, end]

    @property
    def operate(self):
        if self.id == 0: # sum
            return sum(package.operate for package in self.content)
        elif self.id == 1: # product, multi or just val if 1
            return math.prod(package.operate for package in self.content)
        elif self.id == 2: # min
            return min(package.operate for package in self.content)
        elif self.id == 3: # max
            return max(package.operate for package in self.content) 
        elif self.id == 4: # value
            return self.content[0]       
        elif self.id == 5: # first greater than second
            return self.content[0].operate > self.content[1].operate
        elif self.id == 6: # first lesser than second
             return self.content[0].operate < self.content[1].operate
        elif self.id == 7: # first equal to second
            return self.content[0].operate == self.content[1].operate


#translate hex file to bin file
def hexToBin(lines):
    return (''.join(f"{int(f'0x{i}',16):04b}" for i in lines[0]))

binIn = hexToBin(input2)

#  unpacking somehow resets, reinserts old binaries with error   
# #                                          001010000001100100000111100011000000000100001000001001010000010                                              
# 100 111 0 000000001010000 01000010000000001001010000001100100000111100011000000000100001000001001010000010 00 #
#         0 000000001010000 01000010000000001001010000001100100000111100011000000000100001000001001010000010 00 #
#                           010 000 1 00000000010 01010000001100100000111100011000000000100001000001001010000010 #
#                                   1 00000000010 01010000001100100000111100011000000000100001000001001010000010 #
#                                                 010 100 00001 100100000111100011000000000100001000001001010000010
#                                                               100 100 00011 1100011000000000100001000001001010000010
#                                                               100 100 00011 1100011000000000100001000001001010000010
#                                                                              100011000000000100001000001001010000010
#                                                                                    000000000100001000001001010000010
#                                                                                                    00001001010000010
#                                                                                                          01010000010
#                                              
#print(binIn)
pck = Package(binIn)
#print(Package(binIn).operate)
