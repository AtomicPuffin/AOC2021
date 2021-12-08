import os
import sys
os.chdir("/Users/andreas/Documents/GitHub/AOC2021/")
#print(os.getcwd())

#print(open("input2.txt").readlines())

power = open("input3.txt").readlines()
#counter = 0
#counts = [0,0,0,0,0,0,0,0,0,0,0,0]

def max_binary(input, counter, counts):
    for i in input:
        for n in range(12):
            counts[n] = counts[n] + int(i[n])
        counter += 1
    max_bin = ""
    for i in counts:
        if i >= counter/2:
            max_bin = max_bin + "1"
        else:
            max_bin = max_bin + "0"
    return max_bin

def min_binary(input, counter, counts):
    for i in input:
        for n in range(12):
            counts[n] = counts[n] + int(i[n])
        counter += 1
    min_bin = ""
    for i in counts:
        if i >= counter/2:
            min_bin = min_bin + "0"
        else:
            min_bin = min_bin + "1"
    return min_bin

#gamma_bin, epsilon_bin = crt_binary(power, counter, counts)


def filt(input, minmax):
    temp = []
    for i in range(12):
        comp = minmax(input, 0, [0,0,0,0,0,0,0,0,0,0,0,0])
        for n in input:
            if comp[i] == n[i]:
                temp.append(n)
        if len(temp) == 1:
            return temp
        else:
            input = temp
            temp = []

oxygen = filt(power, max_binary)
co2 = filt(power, min_binary)

print(oxygen)
print(co2)

gamma = int(oxygen[0], 2)
epsilon = int(co2[0], 2)

print(gamma)
print(epsilon)


print(gamma*epsilon)






