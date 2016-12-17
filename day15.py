import re


def solve(offsets):
    for i in range(10000000000):
        if all([(i+k[1]) % k[0] == 0 for k in offsets]):
            print (i)
            return


file_input = """Disc #1 has 13 positions; at time=0, it is at position 10.
Disc #2 has 17 positions; at time=0, it is at position 15.
Disc #3 has 19 positions; at time=0, it is at position 17.
Disc #4 has 7 positions; at time=0, it is at position 1.
Disc #5 has 5 positions; at time=0, it is at position 0.
Disc #6 has 3 positions; at time=0, it is at position 1.
Disc #7 has 11 positions; at time=0, it is at position 0."""

# file_input = """Disc #1 has 5 positions; at time=0, it is at position 4.
# Disc #2 has 2 positions; at time=0, it is at position 1."""

offsets = []

for i in file_input.split('\n'):
    print(i)
    nums = list(map(int,re.findall ("(\d+)", i)))
    offsets.append((nums[1], (nums[3]+nums[0])%nums[1]))

print (offsets)
solve(offsets)
