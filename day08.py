import unittest


class Grid (object):
    def __init__(self, sx, sy):
        self.grid = [[0]*sx for i in range(sy)]

    def rotate(self, col, num, move):
        if col:
            sz = len(self.grid)
            col_list = [self.grid[(i-move) % sz][num] for i in range(sz)]
            for i in range(sz):
                self.grid[i][num] = col_list[i]
        else:
            self.grid[num] = self.grid[num][-move:] + self.grid[num][:-move]

    def rect(self, row, col):
        for r in self.grid[:row]:
            r[:col] = [1]*col

    def lights_on(self):
        return sum(map(sum, self.grid))

    def print_grid(self):
        print('\n'.join([''.join(["#" if c else "." for c in r]) for r in self.grid]))

    def process(self, instr):
        instr = instr.split()
        if instr[0] == "rect":
            col, row = map(int, instr[1].split("x"))
            self.rect(row, col)
        else:
            self.rotate(instr[1] == "column", int(instr[2][2:]), int(instr[4]))


class Day08Test(unittest.TestCase):
    def test_lightson(self):
        test_input = ["rect 3x2", "rotate column x=1 by 1", "rotate row y=0 by 4", "rotate column x=1 by 1"]

        g = Grid(7, 3)
        for instr in test_input:
            g.process(instr)

        g.print_grid()

        self.assertEqual(g.lights_on(), 6)


#unittest.main()

with open("day08.txt", "r") as f:
    file_input = f.readlines()

g = Grid(50, 6)

for instr in file_input:
    g.process(instr)

g.print_grid()

print(g.lights_on())
