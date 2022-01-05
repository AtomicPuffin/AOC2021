import os
os.chdir("/Users/andreas/Documents/GitHub/AOC2021/")

measurements = open("input1.txt").readlines()
prev1 = 999999999
prev2 = 999999999
prev3 = 999999999
counter = 0
for i in measurements:
    if int(i)+prev1+prev2 > prev1+prev2+prev3:
        counter += 1
    prev3 = prev2
    prev2 = prev1
    prev1 = int(i)
print(counter)






