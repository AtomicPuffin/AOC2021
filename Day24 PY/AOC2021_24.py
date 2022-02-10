import math

input = [x.rstrip() for x in open("input24.txt").readlines()]
#input2 = [x.rstrip() for x in open("input24 copy.txt").readlines()]

'''
Input instructions are assembler type and can be translated to higher level code
It is an identical sequence repeating 14 times, with different constants injected
Only register Z carries over between repetitions, the others are overwritten as first action
The sequence is: Zout = w + c + 26 * Zin/a if (Zin % 26 +b) != w else Zin/a
Where w is the input and a, b and c are hardcoded in the input sequence
'''

def zforw(a,b,c,w,zin):
    n = zin/a
    n = math.floor(n) if n >= 0 else math.ceil(n)
    return w + c + 26 * n if (zin % 26 +b) != w else n

def loop(a,b,c,zin,num, maxz):
    zw = []
    for i in range(1,10):
        z = zforw(a,b,c,i,zin)
        if z < maxz:
            zw.append((num+str(i),z))
    return zw


def forwloop():
    a = [1, 1, 1, 26,1, 1, 1, 26, 26,1, 26,26,26,26]
    b = [13,11,14,-5,14,10,12,-14,-8,13,0, -5,-9,-1]
    c = [0, 3, 8, 5, 13,9, 6, 1,  1, 2, 7, 5, 8, 15]
    zout = [('',0)]
    for pos in range(14): 
        print(pos)
        maxz = 1
        for i in range(-1,-14+pos,-1): # limits solutions to those that can reach z = 0 at the end
            maxz *= a[i]
        print(maxz)
        znext = []
        for i in zout:
            znext += loop(a[pos], b[pos], c[pos],i[1],i[0], maxz)
        zout = znext
    return zout

#########################


forw = forwloop()
print(len(forw))

res = [int(i[0]) for i in forw if i[1] == 0]
print(max(res)) # part 1
print(min(res)) # part 2



''' Used for testing, coded the ALU
class ALU:
    def __init__(self):
        self.mem = {'w':0,'x':0,'y':0,'z':0}
        self.x = 0
        self.y = 0
        self.z = 0
        self.map = {'inp':self.inp, 'add':self.add, 'mul':self.mul, 
                    'div':self.div, 'mod':self.mod,'eql':self.eql}

    def add(self,a,b):
        if b in 'wxyz':
            self.mem[a] += self.mem[b]
        else:
            self.mem[a] += int(b)

    def mul(self,a,b):
        if b in 'wxyz':
            self.mem[a] = self.mem[a] * self.mem[b]
        else:
            self.mem[a] = self.mem[a] * int(b)

    def div(self,a,b):
        if b in 'wxyz':
            self.mem[a] = self.mem[a] / self.mem[b] 
        else:
            self.mem[a] = self.mem[a] / int(b)
        if self.mem[a] < 0:
            self.mem[a] = math.ceil(self.mem[a])
        else:
            self.mem[a] = math.floor(self.mem[a])

    def mod(self,a,b):
        if b in 'wxyz':
            self.mem[a] = self.mem[a] % self.mem[b]  
        else:
            self.mem[a] = self.mem[a] % int(b)  

    def eql(self,a,b):
        if b in 'wxyz':
            self.mem[a] = 1 if self.mem[a] == self.mem[b] else 0
        else:
            self.mem[a] = 1 if self.mem[a] == int(b) else 0
    
    def parse(self, instr,serial):
        serial = str(serial)
        self.mem['w'] = 0
        self.mem['x'] = 0
        self.mem['y'] = 0
        self.mem['z'] = 0
        for r in instr:
            print('before',self.mem['w'],self.mem['x'],self.mem['y'],self.mem['z'])
            r = r.split()
            print(r)
            if r[0] == 'inp':
                self.mem['w'] = int(serial[0])
                serial = serial[1:]
                print(self.mem['z'])
            else:
                self.map[r[0]](r[1],r[2])
        return self.mem['z']


    

def cut(input): # split by inputs
    instr = []
    while input:
        instr.append(input[:18])
        input = input[18:]
    return instr

'''
