import functools
from adventutils import search_astar

def gen_maze_xy(state, num):
    x, y = state
    a = x*x + 3*x + 2*x*y + y + y*y + num
    return bin(a).count("1") % 2 == 0

def maze_poss (state, num):
    poss = [(d[0]+state[0], d[1]+state[1]) for d in {(1,0), (-1,0), (0,1), (0,-1)}]
    poss = filter(functools.partial(gen_maze_xy, num=num), poss)
    return poss

def distance (state, target):
    return abs(state[0]-target[0])+abs(state[1]-target[1])

path = search_astar((1,1), functools.partial(distance, target=(31,39)), functools.partial(maze_poss, num=1358))

print (len(path))