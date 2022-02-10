input = open("input13.txt").readlines()
#input = open("input13 copy.txt").readlines()
#input = open("input13 big.txt").readlines()

def readLines(lines):
    coord = []
    while lines[0][0].isnumeric():
        l = lines.pop(0)
        coord.append((int(l.split(',')[0]), int(l.split(',')[1])))
    l = lines.pop(0)
    folds = [(i.split()[2].rstrip()[0],int(i.split()[2].rstrip()[2:])) for i in lines]
    return coord, folds
        

def boardSize(dts):
    mY = 0
    mX = 0
    for i in dts:
        mY = max(mY,i[1])
        mX = max(mX,i[0])
    return mY,mX


def fold(dts, line):
    if line[0] == 'y':
        for i in range(len(dts)):
            if dts[i][1] > line[1]:
                dts[i] = (dts[i][0], 2*line[1]-dts[i][1])
    elif line[0] == 'x':
        for i in range(len(dts)):
            if dts[i][0] > line[1]:
                dts[i] = (2*line[1]-dts[i][0], dts[i][1])
    dts = list(dict.fromkeys(dts))
    return dts


def visualize(dots,x,y):
    outLines = []
    for ay in range(y):
        outLine = []
        for ax in range (x):
            if (ax,ay) in dots:
                outLine.append('#')
            else:
                outLine.append(' ')
        outLines.append(''.join(outLine))
    return outLines


dots, folds = readLines(input)
maxY, maxX = boardSize(dots)


for i in folds:
    dots = fold(dots,i)
    if i[0] == 'x':
        maxX = i[1]
    else:
        maxY = i[1]

temp = visualize(dots,maxX, maxY)
for i in temp:
    print(i)
