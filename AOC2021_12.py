input = open("input12.txt").readlines()
#input = open("input12 copy.txt").readlines()

def buildMap(lines):
    cmap = {}
    for i in lines:
        a = i.split('-')[0].rstrip()
        b = i.split('-')[1].rstrip()
        if a in cmap:
            cmap[a].append(b)
        else:
            cmap[a] = [b]
        if b in cmap:
            cmap[b].append(a)
        else:
            cmap[b] = [a]
    return cmap

def buildTree(cmap, path, node, double):
    p2 = path.copy()
    p2.append(node)
    if node == 'end':
        return [p2]
    paths = []
    for i in cmap[node]:
        if not i.islower() or i.islower() and i not in path:
            addNotEmpty(paths, (buildTree(cmap,p2,i,double)))
        elif i.islower() and i in path and double and i != 'start':
            addNotEmpty(paths, (buildTree(cmap,p2,i,False)))       
    return paths

def addNotEmpty(paths, t):
    if t:
        for x in range(len(t)):
            paths.append(t[x])


m = buildMap(input)

allPaths = buildTree(m,[],'start',True)

print(len(allPaths))