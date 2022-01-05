import os

os.chdir("/Users/andreas/Documents/GitHub/AOC2021/")
input = open("input5.txt").readlines()
#input = open("input5ex.txt").readlines()


def create_sea():
    temp = []
    for i in range(1000):
        temp.append([])
        for _ in range(1000):
            temp[i].append(0)
    return temp

def read_lines(lines):
    return [
        [
            int(i.split()[0].split(",")[0]),
            int(i.split()[0].split(",")[1]),
            int(i.split()[-1].split(",")[0]),
            int(i.split()[-1].split(",")[1]),
        ]
        for i in lines
    ]

def filter_lines_v(lines):
    return [i for i in lines if i[0] == i[2] or i[1] == i[3]]

def filter_lines_d(lines):
    output = []
    for i in lines:
        dx = abs(i[0]-i[2])
        dy = abs(i[1]-i[3])
        if dx == dy:
            output.append(i)
    return output

def update_v(lines, seamap):
    for i in lines:
        x1 = i[0]
        x2 = i[2]
        y1 = i[1]
        y2 = i[3]

        if x1 == x2 and y1 == y2:
            seamap[x1][y1] += 1

        elif x1 == x2:
            y = min(y1,y2)
            d = abs(y2 - y1) +1

            for t in range(d):
                seamap[x1][y+t] += 1
        else:
            x = min(x1,x2)
            d = abs(x2 - x1) +1

            for t in range(d):
                seamap[x+t][y1] += 1
        
def update_d(lines, seamap):
    for i in lines:
        dx = abs(i[0]-i[2])+1
        if i[0]-i[1] == i[2]-i[3]:
            x = max(i[0],i[2])
            y = max(i[1],i[3])
            for t in range(dx):
                seamap[x-t][y-t] += 1   
        else:
            x = min(i[0],i[2])
            y = max(i[1],i[3])
            for t in range(dx):
                seamap[x+t][y-t] += 1  

def count(seamap):
    counter = 0
    for x in seamap:
        for y in x:
            if y > 1:
                counter += 1
    return counter


ventlines = read_lines(input)
seamap = create_sea()
ventlinesV = filter_lines_v(ventlines)
ventlinesD = filter_lines_d(ventlines)
update_v(ventlinesV,seamap)
update_d(ventlinesD,seamap)

print(count(seamap))

