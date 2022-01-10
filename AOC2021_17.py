#input = [x.rstrip() for x in open("input17.txt").readlines()]
#input2 = [x.rstrip() for x in open("input17 copy.txt").readlines()]

target = ((235,259),(-62,-118))
target2 = ((20,30),(-5,-10))

def update(x,y,dx,dy):
    x += dx
    if dx > 0:
        dx += -1
    elif dx < 0:
        dx += 1
    y += dy
    dy += -1
    return x,y,dx,dy   

def findPeak(target,dx,dy):
    peak = -1
    y = 0
    x = 0
    prev = (0,0)
    while x <= target[0][1] and y >= target[1][1]:
        prev = (x,y)
        x,y,dx,dy = update(x,y,dx,dy)
        if y > peak:
            peak = y
    if (
        prev[0] >= target[0][0]
        and prev[0] <= target[0][1]
        and prev[1] <= target[1][0]
        and prev[1] >= target[1][1]
    ):
        return peak
    return -1  

def findHit(target,dx,dy):
    y = 0
    x = 0
    odx = dx
    ody = dy
    prev = (0,0)
    while x <= target[0][1] and y >= target[1][1]:
        prev = (x,y)
        x,y,dx,dy = update(x,y,dx,dy)
    if (
        prev[0] >= target[0][0]
        and prev[0] <= target[0][1]
        and prev[1] <= target[1][0]
        and prev[1] >= target[1][1]
    ):
        return (odx,ody)
    return (0,0)

def iter(target, perm):
    peak = 0
    for i in perm:
        temp = findPeak(target,i[0],i[1])
        if temp > peak:
            peak = temp
    return peak    

def iter2(target, perm):
    result = []
    for i in perm:
        temp = findHit(target,i[0],i[1])
        if temp != (0,0):
            result.append(temp)
    return result

t = target

listX = list(range(t[0][1]+1))
listY = list(range(abs(t[1][1]),t[1][1]-1,-1))

perm = []
for x in listX:
    for y in listY:
        perm.append((x,y))

# part 1
print(iter(t, perm))

# part 2
print(len(iter2(t, perm)))

