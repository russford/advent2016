import collections


def gen_maze_xy(x, y, num):
    a = x*x + 3*x + 2*x*y + y + y*y + num
    return bin(a).count("1") % 2 == 1


def gen_maze(w, h, num):
    return [[gen_maze_xy(x,y,num) for x in range(w)] for y in range(h)]


def print_maze(maze):
    print('\n'.join([''.join(["#" if m else "." for m in l]) for l in maze]))


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
    dirs = [d for d in dirs if maze[d[0]][d[1]] == 0 and d not in came_from.keys()]
    return dirs


def check_or_append (n, p, target, q, l, came_from):
    came_from[p] = (n,l+1)
    if p[0] == target[0] and p[1] == target[1]:
        return 1
    else:
        q.append((p, l+1))


def walk_maze (maze, target):
    q = collections.deque()
    came_from = {}
    q.append (((1,1),0))
    while q:
        n, l = q.popleft()
        poss = neighbors(n, maze, came_from)
        print ("at {}: poss = {}".format(n, poss))
        for p in poss:
            if not p in came_from.keys():
                if check_or_append(n, p, target, q, l, came_from):
                    # print (came_from)
                    return came_from
    return came_from

def check_length (target, paths):
    path_len = 0
    while target != (1,1):
        target = paths[target][0]
        path_len += 1
    return path_len

def solve (w, h, num, target):
    maze = gen_maze(w, h, num)
    paths = walk_maze(maze, target)
    print_maze(maze)
    return paths

paths = solve (100,100, 1358, (39,31))

print(paths[(39,31)][1])

for p in paths.items(): print (p[1][1])

print (sum(map(lambda p:p[1][1]<=50, paths.items())))


