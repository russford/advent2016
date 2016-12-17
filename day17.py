import hashlib
import collections

dirs = { "U": (0,-1), "D": (0,1), "L": (-1,0), "R": (1,0) }

def poss(key, path, x, y):
    hash = hashlib.md5((key+path).encode("utf-8")).hexdigest()[:4]
    dirs = [["U", "D", "L", "R"][i] for i in range(4) if "b" <= hash[i] <= "f"]
    if x == 0 and "L" in dirs: dirs.remove("L")
    if x == 3 and "R" in dirs: dirs.remove("R")
    if y == 0 and "U" in dirs: dirs.remove("U")
    if y == 3 and "D" in dirs: dirs.remove("D")
    return dirs

def run_dfs(key, path, x, y, q):
    global dirs
    print("at {},{} path is {}".format(x,y,path))
    if x == 3 and y == 3:
        print("got it in {} steps: {}".format(len(path), path))
        return 1
    paths = poss (key, path, x, y)
    for p in paths:
        dir = dirs[p]
        if run(key, path+p, x+dir[0], y+dir[1]): return 1

def check_or_append (path, x, y, q):
    if x == 3 and y == 3:
        print("got it in {} steps: {}".format(len(path), path))
        return 1
    else:
        q.append((path, x, y))


def run_bfs_step (key, q, stop):
    global dirs
    path, x, y = q.popleft()
    paths = poss (key, path, x, y)
    for p in paths:
        dir = dirs[p]
        if check_or_append(path+p, x+dir[0], y+dir[1], q) and stop: return 1

def run_bfs (key, stop):
    q = collections.deque()
    q.append(("", 0, 0))
    while q:
        if run_bfs_step (key, q, stop) and stop:
            return 1


print (run_bfs("gdjjyniy", 0))