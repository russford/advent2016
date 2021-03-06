# swap position X with position Y means that the letters at indexes X and Y (counting from 0) should be swapped.

# swap letter X with letter Y means that the letters X and Y should be swapped (regardless of where they appear in the string).

# rotate left/right X steps means that the whole string should be rotated; for example, one right rotation would turn abcd into dabc.

# rotate based on position of letter X means that the whole string should be rotated to the right based on the index of letter X
# (counting from 0) as determined before this instruction does any rotations. Once the index is determined, rotate the string to the
# right one time, plus a number of times equal to that index, plus one additional time if the index was at least 4.

# reverse positions X through Y means that the span of letters at indexes X through Y (including the letters at X and Y) should be reversed in order.

# move position X to position Y means that the letter which is at index X should be removed from the string, then inserted such that it ends up at index Y.

import re, itertools, functools

def instr_swap_position (data, s):
    a = int(min(data))
    b = int(max(data))
    return s[:a]+s[b]+s[a+1:b]+s[a]+s[b+1:]

def instr_swap_letter (data, s):
    a = s.index(data[0])
    b = s.index(data[1])
    return instr_swap_position((a,b), s)

def instr_rotate_num(data, s):
    rot = int(data[1])
    if data[0] == "left":
        return s[rot:]+s[:rot]
    else:
        return s[-rot:]+s[:-rot]

def instr_rotate_pos(data, s):
    i = s.index(data[0])
    if i >= 4: i += 1
    return instr_rotate_num (("right", (i+1)%len(s)), s)

def instr_reverse (data, s):
    return s[:int(data[0])]+s[int(data[0]):int(data[1])+1][::-1]+s[int(data[1])+1:]

def instr_move_pos (data, s):
    c = s[int(data[0])]
    s = s[:int(data[0])]+s[int(data[0])+1:]
    return s[:int(data[1])]+c+s[int(data[1]):]

def build_func_list(instr):
    instr_set = { "swap position (\w+) with position (\w+)": instr_swap_position,
                  "swap letter (\w+) with letter (\w+)": instr_swap_letter,
                  "rotate (\w+) (\w+) step": instr_rotate_num,
                  "rotate based on position of letter (\w+)": instr_rotate_pos,
                  "reverse positions (\w+) through (\w+)": instr_reverse,
                  "move position (\w+) to position (\w+)": instr_move_pos }
    func_list = [(re.compile(string), function) for string, function in instr_set.items()]
    funcs = []
    for i in instr:
        for regex, func in func_list:
            m = regex.match(i)
            if m:
                funcs.append (functools.partial(func, m.groups()))
    return funcs


def process_instr (s, instr, func_list):
    for regex, func in func_list:
        m = regex.match (instr)
        if m:
            return func(s, m.groups())
    else:
        raise Exception ("no match on instruction {}".format(instr))


# swap position 4 with position 0 swaps the first and last letters, producing the input for the next step, ebcda.
# swap letter d with letter b swaps the positions of d and b: edcba.
# reverse positions 0 through 4 causes the entire string to be reversed, producing abcde.
# rotate left 1 step shifts all letters left one position, causing the first letter to wrap to the end of the string: bcdea.
# move position 1 to position 4 removes the letter at position 1 (c), then inserts it at position 4 (the end of the string): bdeac.
# move position 3 to position 0 removes the letter at position 3 (a), then inserts it at position 0 (the front of the string): abdec.
# rotate based on position of letter b finds the index of letter b (1), then rotates the string right once plus a number of times equal to that index (2): ecabd.
# rotate based on position of letter d finds the index of letter d (4), then rotates the string right once, plus a number of times equal to that index,
# plus an additional time because the index was at least 4, for a total of 6 right rotations: decab.


def process_deck (s, deck):
    for d in deck:
        s = d(s)
    return s

test_input = ["swap position 4 with position 0", "swap letter d with letter b",
              "reverse positions 0 through 4", "rotate left 1 step",
              "move position 1 to position 4", "move position 3 to position 0",
              "rotate based on position of letter b", "rotate based on position of letter d"]

with open("day21.txt", "r") as f:
    file_input = f.readlines()

deck = build_func_list(file_input)

s = "abcdefgh"
print(process_deck(s, deck))

s = "fbgdceah"

for p in itertools.permutations(s):
    if process_deck(''.join(p), deck) == s:
        print (''.join(p))
