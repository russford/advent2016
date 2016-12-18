# The first floor contains a promethium generator and a promethium-compatible microchip.
# The second floor contains a cobalt generator, a curium generator, a ruthenium generator, and a plutonium generator.
# The third floor contains a cobalt-compatible microchip, a curium-compatible microchip, a ruthenium-compatible microchip, and a plutonium-compatible microchip.
# The fourth floor contains nothing relevant.

# test:
# The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
# The second floor contains a hydrogen generator.
# The third floor contains a lithium generator.
# The fourth floor contains nothing relevant.

import itertools, collections

def check_fried (state):
    checks = [(state[i], state[i+1]) for i in range(1, len(state), 2)]
    if checks:
        gens, chips = zip(*checks)
        for i in range(len(chips)):
            if gens[i] != chips[i] and chips[i] in gens: return 1
    return 0

def state_add (poss, minus, n):
    return [1 if i==0 or i in poss else 0 for i in range(n)]

def check_or_append (state, poss, delta, came_from, q):

    s = list(state)
    s[0] += delta
    for p in poss:
        s[p] = s[0]
    s = tuple(s)

    if s not in came_from and not check_fried(s):
        q.append(s)
        came_from[s] = state

        if all([s == 4 for s in state]):
            print ("\n\nall done\n\n")
            return 1


def fetch_states(state, came_from, q):
    elev = []
    if state[0] < 4: elev += [1]
    if state[0] > 1: elev += [-1]

    floor_items = [i for i in range(1, len(state)) if state[i] == state[0]]

    poss = list(itertools.combinations(floor_items, 1)) + list(itertools.combinations(floor_items, 2))

    for e, p in itertools.product(elev, poss):
        if check_or_append(state, p, e, came_from, q): return 1


def walk_elev (state, target):
    came_from = {}
    q = collections.deque()
    q.append(state)
    while q:
        s = q.popleft()
        if fetch_states(s, came_from, q):
            break

    return came_from

target = (4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4)
origin = (1, 1, 1, 2, 3, 2, 3, 2, 3, 2, 3, 1, 1, 1, 1)

came_from = walk_elev (origin, target)

t = target
i = 1
while t != origin:
    print (t, i)
    t = came_from [t]
    i+=1
print (origin)





