plan = open("input2.txt").readlines()
distance = 0
depth = 0
aim = 0
for i in plan:
    t = i.split()[0]
    n = int(i.split()[1])
    if t == "forward":
        distance += n
        depth += aim * n
    elif t == "down":
        aim += n
    elif t == "up":
        aim -= n

print(distance * depth)






