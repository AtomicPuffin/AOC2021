import os

os.chdir("/Users/andreas/Documents/GitHub/AOC2021/")
input = [x.rstrip() for x in open("input25.txt").readlines()]
input2 = [x.rstrip() for x in open("input25 copy.txt").readlines()]

def prep(input):
    seabed = [list(i) for i in input]
    ly = len(seabed)
    lx = len(seabed[0])
    return seabed, ly, lx

def east(seabed, ly, lx):
    moves = []
    for y in range(ly):
        for x in range(lx):
            if seabed[y][x] == '>' and seabed[y][(x + 1) % lx] == '.':
                moves.append((y,x))
    changeE = bool(moves)
    for i in moves:
        seabed[i[0]][i[1]] = '.'
        seabed[i[0]][(i[1] + 1) % lx] = '>'
    return seabed, changeE

def south(seabed,ly,lx):
    moves = []
    for y in range(ly):
        for x in range(lx):
            if seabed[y][x] == 'v' and seabed[(y + 1) % ly][x] == '.':
                moves.append((y,x))
    changeS = bool(moves)
    for i in moves:
        seabed[i[0]] [i[1]] = '.'
        seabed[(i[0]+1) % ly] [i[1]] = 'v'
    return seabed, changeS

seabed, ly,lx = prep(input)

counter = 0
change = True
while change:
    seabed, che = east(seabed,ly,lx)
    seabed, chs = south(seabed,ly,lx)
    change  = che or chs
    counter += 1

print(counter)
