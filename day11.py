# The first floor contains a promethium generator and a promethium-compatible microchip.
# The second floor contains a cobalt generator, a curium generator, a ruthenium generator, and a plutonium generator.
# The third floor contains a cobalt-compatible microchip, a curium-compatible microchip, a ruthenium-compatible microchip, and a plutonium-compatible microchip.
# The fourth floor contains nothing relevant.

# test:
# The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
# The second floor contains a hydrogen generator.
# The third floor contains a lithium generator.
# The fourth floor contains nothing relevant.

import itertools, heapq
from functools import reduce



def check_fried (state):
    checks = [(state[i], state[i+1]) for i in range(1, len(state), 2)]
    if checks:
        gens, chips = zip(*checks)
        for i in range(len(chips)):
            if gens[i] != chips[i] and chips[i] in gens: return 1
    return 0

def state_add (poss, minus, n):
    return [1 if i==0 or i in poss else 0 for i in range(n)]

def state_heuristic(state):
    return (reduce(lambda x,y: -x*y, state), state)

def check_or_append (current, poss, delta, came_from, q, cost):
    s = list(current)
    s[0] += delta
    for p in poss:
        s[p] = s[0]
    s = tuple(s)

    # print ("cost[{}] = {}".format(current, cost[current]))

    if not check_fried(s):
        if s not in came_from: # or cost[s] > new_cost:
            # if s in cost: old_cost = cost[s]
            # else: old_cost = "N/A"
            # print ("i: {}, i+1: {} | cost is {}, new cost {}".format(current, s, old_cost, new_cost))
            heapq.heappush(q, state_heuristic(s))
            came_from[s] = current
            cost[s] = new_cost

        if all([s == 4 for s in current]):
            print ("got a solution, cost = ", solve_cost)
            return 1


def fetch_states(state, came_from, q, cost):
    elev = []
    if state[0] < 4: elev += [1]
    if state[0] > 1: elev += [-1]

    floor_items = [i for i in range(1, len(state)) if state[i] == state[0]]

    poss = list(itertools.combinations(floor_items, 1)) + list(itertools.combinations(floor_items, 2))

    for e, p in itertools.product(elev, poss):
        if check_or_append(state, p, e, came_from, q, cost): return 1


def walk_elev (state, target, cost):
    came_from = {}
    cost[state] = 0
    q = []
    heapq.heappush(q, (-1, state))
    while q:
        pri, s = heapq.heappop(q)
        if fetch_states(s, came_from, q, cost):
            break

    return came_from








target = (4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4)
origin = (1, 1, 1, 2, 3, 2, 3, 2, 3, 2, 3, 1, 1, 1, 1)

# target = (4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4)
# origin = (1, 1, 1, 2, 3, 2, 3, 2, 3, 2, 3)

# target = (4, 4, 4, 4, 4)
# origin = (1, 2, 1, 3, 1)

cost = {}

came_from = walk_elev (origin, target, cost)

print ("!{}!".format(cost[target]))


