import os
import sys
#import numpy as np
os.chdir("/Users/andreas/Documents/GitHub/AOC2021/")
input = open("input4.txt").readlines()

def read_draws(row):
    return [int(i) for i in row.split(",")]

def read_row (row):
    temp = []
    for i in row:
        temp.append([int(i),False])
    return temp

def read_bricks (raw_input):
    temp = []
    counter = 0
    for i in raw_input[2:]:
        if counter < 5:
            temp.append(read_row(i.split()))
            counter += 1
        else:
            counter = 0
        if counter == 5:
            bricks.append(temp)
            temp = []

def update(brick, num):
    for i in brick:
        for y in i:
            if y[0] == num:
                y[1] = True
    return brick

def check_row(row):
    return bool(row[0][1] and row[1][1] and row[2][1] and row[3][1] and row[4][1])

def check(brick):
    for i in range(5):
        if check_row(brick[i]) or check_row([brick[0][i],brick[1][i],brick[2][i],brick[3][i],brick[4][i]]):
            return True
    return False

def final_calc(brick, numb):
    temp = 0
    for i in brick:
        for y in i:
            if not y[1]:
                temp += y[0]
    return temp * numb


def bingo(dra, brick):
    for i in dra:
        temp = []   
        for y in brick:
            update(y,i)
        for y in brick:
            if not check(y):
                temp.append(y)

        if len(temp) == 0:
#            print(brick[0])
#            print(i)
            return(final_calc(brick[0],i))
        brick = temp

bricks = []                
draws = read_draws(input[0])
read_bricks(input)                             

print(bingo(draws,bricks))





