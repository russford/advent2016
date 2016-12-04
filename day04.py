import re
import collections

def decrypt (name, code):
    return " ".join([''.join([chr(97 + (ord(c)-97+code)%26) for c in w]) for w in name.split("-")])

def is_valid (match):

    name, code, checksum = match.groups()
    code = int(code)

    c = collections.Counter(name.replace("-",""))

    key_fn = lambda x: (-x[1],x[0])
    top5 = ''.join(x[0] for x in sorted(c.items(), key=key_fn)[:5])

    if top5 == checksum:
        room = decrypt(name, code)
        if "north" in room: print ("{}: {}".format(code, room))
        return code
    return 0

with open("day04.txt", "r") as f:
    input_set = f.readlines()

regex = re.compile ("^([a-z\-]+)-([0-9]+)\[([a-z]+)\]$")

print(sum([is_valid(regex.match(inp)) for inp in input_set]))