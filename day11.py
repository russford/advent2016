# The first floor contains a promethium generator and a promethium-compatible microchip.
# The second floor contains a cobalt generator, a curium generator, a ruthenium generator, and a plutonium generator.
# The third floor contains a cobalt-compatible microchip, a curium-compatible microchip, a ruthenium-compatible microchip, and a plutonium-compatible microchip.
# The fourth floor contains nothing relevant.

# test:
# The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
# The second floor contains a hydrogen generator.
# The third floor contains a lithium generator.
# The fourth floor contains nothing relevant.

import itertools, copy, collections


class State(object):
    def __init__(self):
        self.items = {"HM": 1, "LM": 1, "HG": 2, "LG": 3 }
        print (sorted(self.items.items()))
        self.elevator = 1
        self.chem_set = set([a[0] for a in self.items.keys()])

    def tuple_state(self):
        return [self.elevator] + [v for k,v in sorted(self.items.items())]

    def print_items(self):
        for i in range(4,0,-1):
            str = " ".join([ k if v==i else ". " for k,v in self.items.items()])
            e_str = "E " if self.elevator == i else "  "
            print ("L{} {} {}".format(i, e_str, str))

    def check_fry_set (self, floor_items):
        if not "G" in [g[1] for g in floor_items]:
            return 0
        if not "M" in [g[1] for g in floor_items]:
            return 0

        chips = set([a[0] for a in floor_items if a[1] == "M"])
        gens = set([a[0] for a in floor_items if a[1] == "G"])

        return any([c not in gens for c in chips]) and any([g not in chips for g in gens])


    def check_fry(self):
        for i in range(4,0,-1):
            if (self.check_fry_set ([k for k,v in self.items.items() if v == i])):
                return 1

    def check_complete (self):
        return all([v == 4 for k,v in self.items.items()])

    def fetch_states (self):
        elevators = []
        if self.elevator < 4:
            elevators += [1]
        if self.elevator > 1:
            elevators += [-1]

        floor_items = [k for k,v in self.items.items() if v == self.elevator]

        poss = list(itertools.combinations(floor_items, 1)) + list(itertools.combinations(floor_items, 2))
        poss = list(itertools.product(elevators, poss))
        return poss

    def act(self, action):
        self.elevator += action[0]
        for i in action[1]:
            self.items[i] = self.elevator


seen_states = collections.deque()

min_depth = 5

def run_states(state, depth):
    print ("at depth {}: {} | {}".format(depth, state.tuple_state(), seen_states))
    global min_depth, seen_states

    if depth>min_depth:
        return 0
    if state.check_fry():
        return 0
    if state.check_complete():
        print ("complete! {}: {}".format(depth, seen_states))
        if min_depth > depth: min_depth = depth

    poss = state.fetch_states()

    #print ("proceeding; {} poss".format(len(poss)))
    for move in poss:
        s = copy.deepcopy(state)
        s.act (move)

        if not s.tuple_state() in seen_states:
            seen_states.append(state.tuple_state())
            run_states(s, depth+1)
            seen_states.pop()

s = State()
print(run_states(s,1))

print(seen_states)