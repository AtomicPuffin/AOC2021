input = open("input6.txt").readlines()
#input = open("input6ex.txt").readlines()


def read_lines(lines):
    temp = lines[0].split(",")
    return [int(i) for i in temp]

def initial_state(fishes, counter):
    for x in range(len(fishes)):
        counter[fishes[x]] += 1
    return counter

""" Part 1
def update(fishes, days):
    for i in range(days):
        for x in range(len(fishes)):
            if fishes[x] == 0:
                fishes[x] = 6
                fishes.append(8)
            else:
               fishes[x] -= 1
"""
def update(counter):
    temp = counter[1]

    counter[1] = counter[2]
    counter[2] = counter[3]
    counter[3] = counter[4]
    counter[4] = counter[5]
    counter[5] = counter[6]
    counter[6] = counter[7]+counter[0]
    counter[7] = counter[8]
    counter[8] = counter[0]

    counter[0] = temp


counters = [0,0,0,0,0,0,0,0,0]

school = read_lines(input)
counters = initial_state(school, counters)

for _ in range (256):
    update(counters)

print(sum(counters))

