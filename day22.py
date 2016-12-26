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

    def can_move(self, b):
        return self.used != 0 and self.used < b.avail and (abs(self.x - b.x) + abs(self.y - b.y) <= 1)

    def string(self):
        return "{:03d}/{:03d}".format(self.used, self.size)

    def count_neighbors(self, data):
        deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        self.neighbors = [data[(self.x + d[0], self.y + d[1])] for d in deltas if (self.x + d[0], self.y + d[1]) in data]
        self.neighbors = list(filter(lambda n: self.can_move(n), neighbors))
        return self.neighbors

    def __repr__(self):
        return "{0.name} ({0.x},{0.y}): {0.used}/{0.size}".format(self)

    def char (self):
        if self.used == 0:
            return "_"
        if len(self.neighbors) == 0:
            return "#"
        else: return "."

def get_poss (data):
    return [(a,b) for a,b in itertools.permutations(data.values(), 2) if a.is_viable(b)]


def walk (data, node, dest):
    heap = []
    poss = get_poss(data)
    while



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

target = (max_x, 0)
data[target].payload = True

for x, d in data.items():
    d.count_neighbors(data)


