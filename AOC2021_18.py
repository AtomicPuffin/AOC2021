import os
import math
import ast

os.chdir("/Users/andreas/Documents/GitHub/AOC2021/")
input = [x.rstrip() for x in open("input18.txt").readlines()]
input2 = [x.rstrip() for x in open("input18 copy.txt").readlines()]

class Snailnum:
    def __init__(self, num, parent=0):
        self.parent = parent
        if isinstance(num[0], (int, Snailnum)):
            self.left = num[0]
        else:
            self.left = Snailnum([num[0][0],num[0][1]], self)
        if isinstance(num[1], (int, Snailnum)):
            self.right = num[1]
        else:
            self.right = Snailnum([num[1][0],num[1][1]], self)

    def __add__(self,self2):
        result = Snailnum([self, self2])
        self.parent = result
        self2.parent  = result
        finished = False
        while not finished:
            a = False
            while not a:
                a = result.explode()
            b = result.split()
            finished  = a and b            
        return result

    def __repr__(self):
        if isinstance(self.left, int) and isinstance(self.right, int):
            return '({0}, {1})'.format(self.left, self.right)
        elif isinstance(self.left, int):
            return '({0}, {1})'.format(self.left, repr(self.right))
        elif isinstance(self.right, int):
            return '({0}, {1})'.format(repr(self.left), self.right)
        else:
            return '({0}, {1})'.format(repr(self.left), repr(self.right))

    def explode(self, n=0):
        finished = True
        if n == 4:
            finished = False
            self.bubbleL(self.left)
            self.bubbleR(self.right)
            if self.parent.left == self:
                self.parent.left = 0
            elif self.parent.right == self:
                self.parent.right = 0
            else:
                print('Error expl')
        else:
            if finished and not isinstance(self.left, int):
                finished = self.left.explode(n+1) and finished
            if finished and not isinstance(self.right, int):
                finished = self.right.explode(n+1) and finished
        return finished

    def bubbleR(self, y):
        if self.parent != 0: # has parent, if 0 do nothing, reached end of number with no match
            if isinstance(self.parent.right,int): # found an int, add and end
                self.parent.right += y
            elif self.parent.right == self: # keep climbing
                self.parent.bubbleR(y)
            else: # full Snailnum to the right
                self.parent.right.drillR(y)

    def drillR(self,y):
        if isinstance(self.left,int):
            self.left += y
        else:
            self.left.drillR(y)

    def bubbleL(self, x):
        if self.parent != 0: # has parent, if 0 do nothing, reached end of number with no match
            if isinstance(self.parent.left,int): # found an int, add and end
                self.parent.left += x
            elif self.parent.left == self: # keep climbing
                self.parent.bubbleL(x)
            else: # full Snailnum to the right
                self.parent.left.drillL(x)

    def drillL(self,x):
        if isinstance(self.right,int):
            self.right += x
        else:
            self.right.drillL(x)


    def split(self):
        finished = True
        if isinstance(self.left, int):
            if self.left >= 10:
                finished = False
                x = math.floor(self.left / 2)
                y = math.ceil(self.left / 2)
                self.left = Snailnum([x,y],self)
        else:
            finished = self.left.split() and finished
        if isinstance(self.right, int) and finished:
            if self.right >= 10:
                finished = False
                x = math.floor(self.right / 2)
                y = math.ceil(self.right / 2)
                self.right = Snailnum([x,y],self)
        elif finished:
            finished = self.right.split() and finished
        return finished        


    def magnitude(self):
        a = self.left if isinstance(self.left, int) else self.left.magnitude()
        b = self.right if isinstance(self.right, int) else self.right.magnitude()
        return a*3 + b*2

inp = [ast.literal_eval(x) for x in input]


# Part 2
max = 0
for i in range(len(inp)):
    inpcopy = inp.copy()
    x = inpcopy.pop(i)
    for i in inpcopy:
        a = (Snailnum(x)+Snailnum(i)).magnitude()
        if a > max:
            max = a
print(max)

# Part 1

res = Snailnum(inp.pop(0))
for i in inp:
    res = res + Snailnum(i)
print(res.magnitude())

