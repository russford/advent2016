

def part1 (inp):
    print sum (sum(i) > max(i)*2 for i in inp)

def part2 (inp):

    threes = [iter(inp)]*3

    print sum (
            sum(
                sum(l) > max(l)*2
                for l in zip(*list(c))
                )
            for c in zip(*threes)
            )

if __name__ == "__main__":
    with open("day03.txt", "r") as f:
        inp = [map(int, l.split()) for l in f.readlines()]
    part1(inp)
    part2(inp)

