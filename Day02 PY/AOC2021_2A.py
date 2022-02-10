plan = open("input2.txt").readlines()
distance = 0
depth = 0
aim = 0
for i in plan:
    t = i.split()[0]
    n = int(i.split()[1])
    if t == "forward":
        distance += n
    elif t == "down":
        depth += n
    elif t == "up":
        depth -= n

print(distance * depth)






