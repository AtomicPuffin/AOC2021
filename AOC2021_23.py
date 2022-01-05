import os
import copy
from queue import PriorityQueue

os.chdir("/Users/andreas/Documents/GitHub/AOC2021/")
input = [x.rstrip() for x in open("input23.txt").readlines()]
input2 = [x.rstrip() for x in open("input23 copy.txt").readlines()]
input3 = [x.rstrip() for x in open("input23 copy 2.txt").readlines()]
input4 = [x.rstrip() for x in open("input23 copy 3.txt").readlines()]

class Room:
    def __init__(self, name, next, type='h', size=1, canleave='inout'):
        self.name = name #'h0'
        self.next = next # [(name, cost)]
        self.type = type # hABCD
        self.size = size # how many fits inside
        self.content = []
        self.canleave = canleave #inout, out, in, complete

    def canPut(self,type):
        if self.type == 'h':
            return not self.content
        return self.canleave == 'in' and self.type == type

    def canTake(self):
        if self.type == 'h':
            return self.content
        return self.canleave == 'out' and len(self.content) > 0     

    def take(self):
        cost = self.size - len(self.content)
        amph = self.content.pop(0)
        if self.canleave == 'out' and all(i == self.type for i in self.content):
            self.canleave = 'in'
        return amph, cost

    def put(self, type):
        cost  = self.size - len(self.content) - 1
        self.content.append(type)
        if self.canleave == 'in' and len(self.content) == self.size:
            self.canleave = 'complete'
        return cost

class Burrow:
    def __init__(self, depth):

        self.rooms = {'h0': Room('h0', [('h1',1)]),
                      'h1': Room('h1', [('h0',1),('h3',2),('A',2)]),
                      'h3': Room('h3', [('h1',2),('h5',2),('A',2),('B',2)]),                
                      'h5': Room('h5', [('h3',2),('B',2),('C',2),('h7',2)]),                  
                      'h7': Room('h7', [('h5',2),('C',2),('D',2),('h9',2)]),                 
                      'h9': Room('h9', [('h7',2),('h10',1),('D',2)]),      
                      'h10': Room('h10', [('h9',1)]),             
                      
                      'A': Room('A', [('h1',2),('h3',2)], 'A', depth, 'out'),                
                      'B': Room('B', [('h3',2),('h5',2)], 'B', depth, 'out'),                
                      'C': Room('C', [('h5',2),('h7',2)], 'C', depth, 'out'),                   
                      'D': Room('D', [('h7',2),('h9',2)], 'D', depth, 'out'),           
        }
        self.cost = 0 # total cost to get here
        self.energy = {'A':1, 'B':10,'C':100,'D':1000}
        self.last = ''

    def __str__(self):
        return (str(self.rooms['h0'].content)+str(self.rooms['h1'].content)+str(self.rooms['h3'].content)+
              str(self.rooms['h5'].content)+str(self.rooms['h7'].content)+str(self.rooms['h9'].content)+
              str(self.rooms['h10'].content)+''.join(self.rooms['A'].content)+'-'+''.join(self.rooms['B'].content)+'-'+
              ''.join(self.rooms['C'].content)+'-'+''.join(self.rooms['D'].content))

    def __eq__(self, other):
        return self.cost == other.cost

    def __lt__(self, other):
        return self.cost < other.cost

    def readLines(self, lines):
        rooms = {3:'A', 5:'B',7:'C',9:'D'}
        for i in range(len(lines[1])): # check hallway, might inject non starter board
            if lines[1][i] in 'ABCD':
                self.rooms['h'+str(i+1)].put(lines[1][i])
        for y in range(self.rooms['A'].size): # check rooms
            for i in range(len(lines[1])-2):
                if lines[-(y+2)][i] in 'ABCD': # since queu, start from behind
                    self.rooms[rooms[i]].put(lines[(y+2)][i])

    def legalPath(self, last, start, orig): # [(key,cost)], (key,cost), (key,cost), [(key)]
        mvs = []
        todo = []
        l = [start[0]]
        for p in self.rooms[start[0]].next: # check all neighbours, p = (key, cost)
            # never backtrack
            l.append(p[0])
            if p[0] not in last and self.rooms[p[0]].canPut(self.rooms[orig].content[0]):
                todo += [(p[0], start[1]+p[1])]# add in todo for now
        if todo != []:
            last = l
            for p in todo:
                if self.rooms[orig].type != self.rooms[p[0]].type: # never move from h to h
                    mvs.append(p)
                mvs += (self.legalPath(last, p, orig))
        return mvs            

    def legalMoves(self):
        moves = []
        for i in self.rooms: # for all rooms
            if self.rooms[i].canTake():
                m1 = (i, self.rooms[i].content[0])
                m2 = self.legalPath([], (i,0), i)    
                if m2:
                    moves.append((m1,m2))
        ret = []
        for s in moves: # optimize to always make only a finishing move if available
            for d in s[1]:
                if s[0][1] == d[0]:
                    ret += [(s[0], [(d)])]
        if ret != []:
            return ret
        return moves #list of legal moves with cost

    def move(self, start, dest): #start = key, dest = (key, cost)
        cost = dest[1]
        amph, c1 = self.rooms[start].take()
        c2 = self.rooms[dest[0]].put(amph)
        self.cost += (cost +c1 +c2) * self.energy[amph]

    def complete(self): # count completed rooms
        return sum(self.rooms[t].canleave == 'complete' for t in ['A','B','C','D'])


def step(branches, history):
    while True:
        b = branches.get()[1]
        print(b.cost)
        if b.complete() == 4: # found a solution
            print('winner', b)
            return history,b
        moves = b.legalMoves()
        for start in moves:
            for dest in start[1]:
                branch = copy.deepcopy(b)
                branch.move(start[0][0], dest)
                branch.last = dest[0]
                if (
                    str(branch) in history
                    and history[str(branch)][0] <= branch.cost
                ):
                    continue
                branches.put((branch.cost, branch))
                history[str(branch)] = (branch.cost, str(b))
        if branches.empty():
            print('failed',b)
            return history,b

burr = Burrow(4)
amphs = burr.readLines(input)

print(burr,'\n')
history = {str(burr):(0,'')}
djikstra = PriorityQueue()

djikstra.put((0, burr))
history, solution = step(djikstra, history)

print(solution)

while history[str(solution)][1] != '':
    print(history[str(solution)][1])
    solution = history[str(solution)][1]
