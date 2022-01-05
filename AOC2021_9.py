import os

os.chdir("/Users/andreas/Documents/GitHub/AOC2021/")
input = open("input9.txt").readlines()
#input = open("input9 copy.txt").readlines()

def testinmap(cavefloor, y, x):
    if x < 0 or y < 0 or x >= len(cavefloor[0]) or y >= len(cavefloor):
        return 9
    else:
        return cavefloor[y][x]

def findlow(cavefloor):
    output = []
    for y in range(len(cavefloor)):
        for x in range(len(cavefloor[y])):
            neighbours = [testinmap(cavefloor,y-1,x),testinmap(cavefloor,y+1,x),testinmap(cavefloor,y,x-1),testinmap(cavefloor,y,x+1)]
            if cavefloor[y][x] < min(neighbours):
                output.append([(y,x)])
    return output

def digits(cavefloor):
    return [[int(a) for a in i.rstrip()] for i in cavefloor]


def expandb(cf,bas, y,x):
    for i in [(-1,0),(1,0),(0,-1),(0,1)]:
        iter(cf, bas, y+i[0], x+i[1])

def iter(cf, bas, y,x):
    if testinmap(cf,y,x) == 9:
        pass
    elif (y, x) not in bas:
        bas.append((y,x))
        expandb(cf,bas,y,x)


m = digits(input)

lows = findlow(m)

# One star
'''temp = []
for i in findlow(m):
    temp.append(m[i[0][0]][i[0][1]])'''

# Two stars
basins = [[] for i in range(len(lows))]

for i in range(len(lows)):
    basins[i].append(lows[i][0])
    expandb(m,basins[i], lows[i][0][0], lows[i][0][1])

print (basins)


s = sorted(basins, key=len)
print(s)
print(len(s[-1])*len(s[-2])*len(s[-3]))

