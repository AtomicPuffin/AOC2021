measurements = open("input1.txt").readlines()
prev = 999999
counter = 0
for i in measurements:
    if int(i) > prev:
        counter += 1
    prev = int(i)
print(counter)






