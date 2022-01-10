input = [x.rstrip() for x in open("input22.txt").readlines()]
input2 = [x.rstrip() for x in open("input22 copy.txt").readlines()]
input3 = [x.rstrip() for x in open("input22 copy 2.txt").readlines()]
input4 = [x.rstrip() for x in open("input22 copy 3.txt").readlines()]

def readLines(lines):
    instructions = []
    for i in lines:
        coor = i.split()[1]
        onf = 1 if i.split()[0] == 'on' else 0
        coor = coor.split(',')
        x = coor[0][2:]
        y = coor[1][2:]
        z = coor[2][2:]
        x1,x2 = x.split('..')
        y1,y2 = y.split('..')
        z1,z2 = z.split('..')
        instructions.append((onf, (int(x1), int(x2)), (int(y1), int(y2)), (int(z1), int(z2)),onf))
    return instructions

# for each step, check all cubes for overlap
# if overlap, calculate intersection, add intersection as negative cube
# if ON add step to cubes
# note that overlap will be calculated for intersections as well, 
# and they will alternate between positive and negative, 
# avoiding the need to keep track of multiple overlaps


def overlapping(a,b): # returns True if there is overlap
    return (
        b[1][0] <= a[1][1]
        and b[1][1] >= a[1][0]
        and b[2][0] <= a[2][1]
        and b[2][1] >= a[2][0]
        and b[3][0] <= a[3][1]
        and b[3][1] >= a[3][0]
    )

def intersection(a,b): # returns the intersection of a and b, last element reversed from i
    x1 = max(a[1][0], b[1][0])
    x2 = min(a[1][1], b[1][1])
    y1 = max(a[2][0], b[2][0])
    y2 = min(a[2][1], b[2][1])
    z1 = max(a[3][0], b[3][0])
    z2 = min(a[3][1], b[3][1])
    return (0,(x1,x2),(y1,y2),(z1,z2),-1*a[-1])

def count(cubes): # counts volume of all cubes, adds or subtracts depending on last flag
    return sum(
        (i[1][1] - i[1][0] + 1)
        * (i[2][1] - i[2][0] + 1)
        * (i[3][1] - i[3][0] + 1)
        * i[-1]
        for i in cubes
    )

#steps = readLines(input[:20]) # part 1
steps = readLines(input) # part 2

cubes = [steps.pop(0)]

while steps:
    step = steps.pop(0)
    res = [intersection(cube,step) for cube in cubes if overlapping(cube,step)]
    if step[0] == 1:
        res.append(step)
    cubes += res
print(count(cubes))



