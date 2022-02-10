input = open("input11.txt").readlines()
#input = open("input11 copy.txt").readlines()

octis = [[int(num) for num in word.rstrip()] for word in input ]

def stepOne(oct):
    for y in oct:
        for x in range(len(y)):
            y[x] += 1

def flash(oct,tens):
    for n in tens:
        for i in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]: 
            y = n[0] + i[0]
            x = n[1] + i[1]
            if 0 <= y <= 9 and 0 <= x  <= 9:
                oct[y][x] += 1
                if oct[y][x] == 10:
                    tens.append((y,x))

def stepTwo(oct):
    tens = []
    for y in range(len(oct)):
        for x in range(len(oct[0])):
            if oct[y][x] == 10:
                tens.append((y,x))
    if tens:
        flash(oct,tens)

def stepThree(oct, counter):
    fla = 0
    for y in oct:
        for x in range(len(y)):
            if y[x] > 9:
                y[x] = 0
                fla += 1
    counter+= 1
    return counter, fla

flashes  = 0
counter = 0
for _ in range(1000):
    stepOne(octis)
    stepTwo(octis)
    counter, fla = stepThree(octis, counter)
    flashes += fla
    if fla == 10 ** 2: # part 2 if range larger than answer
        print(counter)
        break

#print(flashes) # part 1 if range set to 100 above

