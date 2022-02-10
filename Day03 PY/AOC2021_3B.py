power = open("input3.txt").readlines()

def max_binary(input, counter, counts):
    for i in input:
        for n in range(12):
            counts[n] = counts[n] + int(i[n])
        counter += 1
    return "".join("1" if i >= counter/2 else "0" for i in counts)

def min_binary(input, counter, counts):
    for i in input:
        for n in range(12):
            counts[n] = counts[n] + int(i[n])
        counter += 1
    return "".join("0" if i >= counter/2 else "1" for i in counts)

def filt(input, minmax):
    temp = []
    for i in range(12):
        comp = minmax(input, 0, [0,0,0,0,0,0,0,0,0,0,0,0])
        for n in input:
            if comp[i] == n[i]:
                temp.append(n)
        if len(temp) == 1:
            return temp
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






