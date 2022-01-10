input = open("input14.txt").readlines()
input2 = open("input14 copy.txt").readlines()

def readLines(lines):
    start = {}
    temp1 = lines.pop(0).rstrip()
    edges = ''.join([temp1[0],temp1[-1]])
    temp2 = [temp1[i:i+2] for i in range(len(temp1[1:]))]
    for i in temp2:
        start[i] = start.get((i),0) + 1
    lines.pop(0)
    pins = {i[:2]: i.rstrip()[-1] for i in lines}
    return start, pins, edges
        
def insert(start, pins):
    end = {}
    for i in start:
        if i in pins:
            i2 = ''.join([i[0],pins[i]])
            i3 = ''.join([pins[i],i[1]])
            end[i2] = end.get((i2),0) + start[i]
            end[i3] = end.get((i3),0) + start[i]
        else:
            end[i] = end.get((i),0) + start[i]
    return end

def spin(start, pins, spins):
    for _ in range(spins):
        start = insert(start, pins)
    return start

def calc1(end, edges):
    result = {}
    for i in end:
        result[i[0]] = result.get((i[0]),0) + end[i]/2
        result[i[1]] = result.get((i[1]),0) + end[i]/2
    result[edges[0]] = result.get((edges[0]),0) + 0.5
    result[edges[1]] = result.get((edges[1]),0) + 0.5
    most = max(result, key=result.get)
    least = min(result, key=result.get)

    return result[most] - result[least]


s, p, e = readLines(input)

#test file
#s2, p2, e2 = readLines(input2)
#end2 = spin(s2, p2, 40) 
#print(calc1(end2, e2))

part1 = spin(s, p, 10)
part2 = spin(s, p, 40)

print(calc1(part1, e))
print(calc1(part2, e))