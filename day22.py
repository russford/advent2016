#Filesystem              Size  Used  Avail  Use%
#/dev/grid/node-x35-y7    89T   72T    17T   80%

import re, itertools, heapq


def get_neighbors(data, n):
    neighbors = []

class Node (object):
    def __init__ (self, data):
        self.x, self.y = data[:2]
        self.name = "node_x{}_y{}".format(self.x, self.y)
        self.size, self.used, self.avail, self.use_pct = data[2:]
        self.neighbors = []
        self.payload = False
        self.blocked = False

    def can_move(self, b):
        return self.used != 0 and self.used < b.avail and (abs(self.x - b.x) + abs(self.y - b.y) <= 1)

    def string(self):
        return "{:03d}/{:03d}".format(self.used, self.size)

    def count_neighbors(self, data):
        deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        self.neighbors = [data[(self.x + d[0], self.y + d[1])] for d in deltas if (self.x + d[0], self.y + d[1]) in data]
        if self.size > 300:
            self.blocked = True
        return self.neighbors

    def __repr__(self):
        return "{0.name} ({0.x},{0.y}): {0.used}/{0.size}".format(self)

    def char(self):
        if self.used == 0:
            return "_"
        if self.blocked:
            return "#"
        else: return "."

def get_poss (data):
    return [(a,b) for a,b in itertools.permutations(data.values(), 2) if a.is_viable(b)]


def walk (data, node, dest):
    heap = []
    poss = get_poss(data)
    while heap:
        pass



def move(data, a, b):
    if not is_viable(a,b):
        raise Exception ("move is not viable")
    else:
        pass


data = {}
with open("day22.txt", "r") as f:
    for l in f.readlines():
        matches = list(map(int, re.findall("(\d+)", l)))
        if matches:
            n = Node(matches)
            data[(n.x,n.y)] = n

max_x = max([n.x for k,n in data.items()])
max_y = max([n.y for k,n in data.items()])

print (max_x, max_y)

target = (max_x, 0)
data[target].payload = True

for x, d in data.items():
    d.count_neighbors(data)

print ('\n'.join([''.join([data[(i, j)].char() for i in range(max_x+1)])for j in range(max_y+1)]))

for k,v in data.items():
    if v.used == 0:
        print (k, v, v.char())

with open ("day22out.txt", "w") as f:
    f.write('\n'.join([' --- '.join([data[(i,j)].string() for i in range(max_x+1)]) for j in range(max_y+1)]))
