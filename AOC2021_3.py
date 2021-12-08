import os
import sys
os.chdir("/Users/andreas/Documents/GitHub/AOC2021/")
#print(os.getcwd())

#print(open("input2.txt").readlines())

power = open("input3.txt").readlines()
counter = 0
counts = [0,0,0,0,0,0,0,0,0,0,0,0]

for i in power:
    for n in range(12):
        counts[n] = counts[n] + int(i[n])
    counter += 1

print(counts)
print(counter)

gamma_bin = ""
epsilon_bin = ""

for i in counts:
    if i > counter/2:
        gamma_bin = gamma_bin + "1"
        epsilon_bin = epsilon_bin + "0"
    else:
        gamma_bin = gamma_bin + "0"
        epsilon_bin = epsilon_bin + "1"

print(gamma_bin)
print(epsilon_bin)

gamma = int(gamma_bin,2)
epsilon = int(epsilon_bin, 2)

print(gamma)
print(epsilon)


print(gamma*epsilon)






