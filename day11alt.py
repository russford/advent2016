import functools
import itertools
import heapq

def search_astar(start, h_func, poss_func):
    q = [(h_func(start), start)]
    visited = {start: None}
    cost = {start: 0}
    while q:
        h, state = heapq.heappop (q)
        if h_func(state) == 0:
            path = []
            while state != start:
                path.append (state)
                state = visited[state]
            return path
        poss = poss_func (state)
        for p in poss:
            new_cost = cost[state]+1
            check_state = p[:1] + tuple(sorted([p[i:i + 2] for i in range(1, len(p), 2)]))
            if check_state not in cost or new_cost < cost[check_state]:
                heapq.heappush(q, (new_cost + h_func(p), p))
                cost[state] = new_cost
                visited[p] = state
    return 0

def check_fried (state):
    checks = [(state[i], state[i+1]) for i in range(1, len(state), 2)]
    if checks:
        gens, chips = zip(*checks)
        for i in range(len(chips)):
            if gens[i] != chips[i] and chips[i] in gens: return 1
    return 0


def floor_poss(state):
    elev = []
    if state[0] < 4:
        elev += [1]
    if state[0] > 1:
        elev += [-1]
    floor_items = [i for i in range(1, len(state)) if state[i] == state[0]]
    poss = list(itertools.combinations(floor_items, 1)) + list(itertools.combinations(floor_items, 2))
    for e, p in itertools.product(elev, poss):
        new_floor = state[0] + e
        new_pairs = [new_floor if i in p else state[i] for i in range(1, len(state))]
        new_pairs = sorted([new_pairs[i:i+2] for i in range(0, len(new_pairs),2)])
        t = tuple([new_floor] + [i for l in new_pairs for i in l])
        if not check_fried(t):
            yield t


def distance(state, target):
    return sum([target[i]-state[i] for i in range(len(state))])


target = (4, 4, 4, 4, 4)
origin = (1, 2, 1, 3, 1)

path = search_astar(origin, functools.partial(distance, target=target), floor_poss)
print('\n'.join(map(str, path)))
assert len(path) == 11

target = (4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4)
origin = (1, 1, 1, 2, 3, 2, 3, 2, 3, 2, 3)

path = search_astar(origin, functools.partial(distance, target=target), floor_poss)

assert len(path) == 33

target = (4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4)
origin = (1, 1, 1, 2, 3, 2, 3, 2, 3, 2, 3, 1, 1, 1, 1)

path = search_astar(origin, functools.partial(distance, target=target), floor_poss)

print(len(path))