

class Grid (object):
    grid = [[0]*50 for i in range(6)]

    def rotate_row(self, row, move):
        self.grid[row] = self.grid[-move:] + self.grid[:-move]
        pass

    def rotate_col(self, col, move):
        self.grid = zip(*self.grid)
        rotate_row(self, col, move)
        self.grid = zip(*self.grid)
        pass

    def rect(self, row, col):
        for g in self.grid[:row]:
            g[:col] = [1]*col

    def lights_on(self):
        return sum(map(sum, self.grid))

    def print_grid(self):
        print ('\n'.join([''.join(["#" if c else " " for c in g]) for g in self.grid]))

    def process(self, instr):
        instr = instr.split()
        if instr[0] == "rect":
            row,col = map(int, instr[1].split("x"))
            self.rect(row,col)
        else:




test_input = ["rect 3x2", "rotate column x=1 by 1", "rotate row y=0 by 4", "rotate column x=1 by 1"]

g = Grid()

for instr in test_input:
    g.process(instr)
    print (g.lights_on())

print(g.lights_on())

g.print_grid()
