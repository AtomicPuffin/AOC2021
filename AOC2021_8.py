import itertools

input = open("input8.txt").readlines()
#input = open("input8 copy.txt").readlines()


zero = [0,1,2,4,5,6]
one = [2,5]
two = [0,2,3,4,6]
three = [0,2,3,5,6]
four = [1,2,3,5]
five = [0,1,3,5,6]
six = [0,1,3,4,5,6]
seven = [0,2,5]
eight = [0,1,2,3,4,5,6]
nine = [0,1,2,3,5,6]

numbers = [zero, one,two,three,four,five,six,seven,eight,nine]

possibilities = list(itertools.permutations(['a','b','c','d','e','f','g']))

def read_lines(lines):
    return [i.split() for i in lines]

''' Part 1
def count(line):
    temp = 0
    for y in line[11:15]:
        if len(y) in uniques:
            temp += 1
    return temp'''

def find_key(line, pos):
    for y in line:
        temp = []
        if len(y) == 2:
            for i in range(len(pos)):
                if sorted(y) == sorted([pos[i][2],pos[i][5]]):
                    temp.append(pos[i])
        elif len(y) == 3:
            for i in range(len(pos)):
                if sorted(y) == sorted([pos[i][0],pos[i][2],pos[i][5]]):
                    temp.append(pos[i])
        elif len(y) == 4:
            for i in range(len(pos)):
                if sorted(y) == sorted([pos[i][1],pos[i][2],pos[i][3],pos[i][5]]):
                    temp.append(pos[i])
        elif len(y) == 5:
            for i in range(len(pos)):
                if sorted(y) in [
                    sorted(
                        [pos[i][0], pos[i][2], pos[i][3], pos[i][4], pos[i][6]]
                    ),
                    sorted(
                        [pos[i][0], pos[i][2], pos[i][3], pos[i][5], pos[i][6]]
                    ),
                    sorted(
                        [pos[i][0], pos[i][1], pos[i][3], pos[i][5], pos[i][6]]
                    ),
                ]:
                    temp.append(pos[i])
        elif len(y) == 6:
            for i in range(len(pos)):
                if sorted(y) in [
                    sorted(
                        [pos[i][0], pos[i][1], pos[i][2], pos[i][4], pos[i][5], pos[i][6]]
                    ),
                    sorted(
                        [pos[i][0], pos[i][1], pos[i][3], pos[i][4], pos[i][5], pos[i][6]]
                    ),
                    sorted(
                        [pos[i][0], pos[i][1], pos[i][2], pos[i][3], pos[i][5], pos[i][6]]
                    ),
                ]:
                    temp.append(pos[i])
        else:
            temp = pos
        pos = temp
    return pos

def decode(line,key):
    num = []
    for i in line[11:15]:
        temp = [key[0].index(y) for y in i]
        x = numbers.index(sorted(temp))
        num.append(x)

    return int(''.join((map(str,num))))

total = 0
for i in read_lines(input):
    k = find_key(i, possibilities)
    total += decode(i,k)

print(total)
