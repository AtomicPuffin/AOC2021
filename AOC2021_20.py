import os

os.chdir("/Users/andreas/Documents/GitHub/AOC2021/")
input = [x.rstrip() for x in open("input20.txt").readlines()]
input2 = [x.rstrip() for x in open("input20 copy.txt").readlines()]

inp = input
alg = inp[0]
img = list(inp[2:])
canvas = '.'

def grow(img,g):
    img2 = []
    rw = ''.join(g for _ in range(len(img[0])+4))
    img2.append(rw)
    img2.append(rw)
    for i in img:
        img2.append(g+g+i+g+g)
    img2.append(rw)
    img2.append(rw)
    return img2

def conv(str):
    bin = ''.join('0' if i == '.' else '1' for i in str)
    return int(bin,2)

def improve(img,alg,canvas):
    img = grow(img,canvas)
    nimg = []
    for y in range(len(img)-2):
        nrow = []
        for x in range(len(img[y])-2):
            tmp = (img[y][x] +img[y][x+1] +img[y][x+2] +img[y+1][x] +img[y+1][x+1] 
                  +img[y+1][x+2] +img[y+2][x] +img[y+2][x+1]+img[y+2][x+2])
            n = conv(tmp)
            nrow += alg[n]
        nimg.append(''.join(nrow))
    
    canvas = alg[conv(canvas*9)]
    return nimg, canvas

def count(img):
    counter = 0
    for y in img:
        for x in y:
            if x == '#':
                counter += 1
    return counter

# Part 1
for _ in range(2):      
    img,canvas = improve(img,alg,canvas)    

print(count(img))

# Part 2
for _ in range(48):      
    img,canvas = improve(img,alg,canvas)    

print(count(img))


