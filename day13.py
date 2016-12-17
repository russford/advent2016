import collections

def gen_maze_xy(x, y, num):
    a = x*x + 3*x + 2*x*y + y + y*y + num
    return bin(a).count("1") % 2 == 1

def gen_maze(w, h, num):
    return [[gen_maze_xy(x,y,num) for x in range(w)] for y in range(h)]

def print_maze(maze):
    print('\n'.join([''.join(["#" if m else "." for m in l]) for l in maze]))

def neighbors (p, maze):
    dirs = []
    if p[0] > 0: dirs.append((-1, 0))
    if p[0] < len(maze[0])-1: dirs.append((1, 0))
    if p[1] > 0: dirs.append((0, -1))
    if p[1] < len(maze)-1: dirs.append((0, 1))
    print(dirs, p)
    dirs = [(d[0]+p[0], d[1]+p[1]) for d in dirs if maze[p[0]+d[0]][p[1]+d[1]] == 0]
    return dirs

def check_or_append (n, p, target, q, came_from):
    came_from [p] = n
    if p[0] == target[0] and p[1] == target[1]:
        return 1
    else:
        q.append(p)


def walk_maze (maze, target):
    q = collections.deque()
    came_from = {}
    q.append ((0,0))
    while q:
        n = q.popleft()
        poss = neighbors(n, maze)
        for p in poss:
            if not p in came_from.keys():
                if check_or_append (n, p, target, q, came_from):
                    return came_from

maze = gen_maze(10, 6, 10)

came_from = walk_maze(maze, (7,4))

t = (7,4)
while t != (0,0):
    print (t)
    t = came_from[t]
