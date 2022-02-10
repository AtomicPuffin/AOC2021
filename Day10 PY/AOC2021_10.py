input = open("input10.txt").readlines()
#input = open("input10 copy.txt").readlines()

calc = {'(':1, ')':1, '[':2,']':2,'{':3,'}':3,'<':4,'>':4}
lr = {'(':'l', ')':'r', '[':'l',']':'r','{':'l','}':'r','<':'l','>':'r'}
cost = {'(':3,'[':57,'{':1197,'<':25137,')':3,']':57,'}':1197,'>':25137}

def read_line(line):
    temp = list(line)
    while len(temp) > 1:
        for i in range(len(temp)):
            if i+1 == len(temp):
                return temp
            if lr[temp[i]] == 'l' and lr[temp[i+1]] == 'r':
                if cost[temp[i]] != cost[temp[i + 1]]:
                    return []
                del temp[i+1]
                del temp[i]
                break            

def sum_line(line):
    s = 0
    for i in range(len(line)):
        s *= 5
        s += calc[line[-i-1]]
    return s

print(sum(read_line(i.rstrip()) for i in input))

incomplete = [read_line(i.rstrip()) for i in input]
incomplete = list(filter(None, incomplete))

scores = [sum_line(i) for i in incomplete]

m = len(scores)//2

scores = sorted(scores)

print(scores[m])

