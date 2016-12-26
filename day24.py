test_input = """###########
#0.1.....2#
#.#######.#
#4.......3#
###########""".split()

import collections
import heapq
import itertools

def gen_maze (inp):
    maze = [list(i) for i in inp]
    pts = {}
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if "0" <= maze[i][j] <= "9":
                pts[maze[i][j]] = (i,j)
    return maze, pts

def neighbors (p, maze, came_from):
    dirs = []
    r, c = p
    if r > 0:
        dirs.append((r-1, c))
    if r < len(maze)-1:
        dirs.append((r+1, c))
    if c > 0:
        dirs.append((r, c-1))
    if c < len(maze[0])-1:
        dirs.append((r, c+1))
    dirs = [d for d in dirs if maze[d[0]][d[1]] != '#' and d not in came_from.keys()]
    return dirs


def check_or_append(n, p, target, q, l, came_from):
    came_from[p] = (n, l+1)
    if p[0] == target[0] and p[1] == target[1]:
        return 1
    else:
        q.append((p, l+1))

def walk_maze(maze, start, target):
    q = collections.deque()
    came_from = {}
    q.append((start, 0))
    while q:
        n, l = q.popleft()
        poss = neighbors(n, maze, came_from)
        # print("at {}: poss = {}".format(n, poss))
        for p in poss:
            if check_or_append(n, p, target, q, l, came_from):
                # print (came_from)
                return came_from
    return came_from

with open ("day24.txt", "r") as f:
    file_input = [l.strip('\n') for l in f.readlines()]

maze, pts = gen_maze (file_input)

costs = {}
for p1, p2 in itertools.combinations(pts.keys(), 2):
    paths = walk_maze(maze, pts[p1], pts[p2])
    costs[(min(p1,p2), max(p1,p2))] = paths[pts[p2]][1]

lowest = 100000
low_path = None

for path in itertools.permutations(sorted(pts.keys())[1:]):
    p = ["0"] + list(path) + ["0"]
    length = sum([costs[(min(p[i], p[i+1]), max(p[i], p[i+1]))] for i in range(len(p)-1)])
    if length < lowest:
        lowest, low_path = length, p

print (low_path, lowest)
