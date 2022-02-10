input = open("input7.txt").readlines()
#input = open("input7ex.txt").readlines()


def read_lines(lines):
    return [int(i) for i in lines[0].split(",")]

crabs = read_lines(input)
crabs.sort()
med = round(sum(crabs) / len(crabs))
med = med-1

result = 0
for i in crabs:
    temp = abs(i - med)
    for i in range(temp):
        result += i+1

print(result)


