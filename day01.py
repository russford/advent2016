input = "R2, L1, R2, R1, R1, L3, R3, L5, L5, L2, L1, R4, R1, R3, L5, L5, R3, L4, L4, R5, R4, R3, L1, L2, R5, R4, L2, R1, R4, R4, L2, L1, L1, R190, R3, L4, R52, R5, R3, L5, R3, R2, R1, L5, L5, L4, R2, L3, R3, L1, L3, R5, L3, L4, R3, R77, R3, L2, R189, R4, R2, L2, R2, L1, R5, R4, R4, R2, L2, L2, L5, L1, R1, R2, L3, L4, L5, R1, L1, L2, L2, R2, L3, R3, L4, L1, L5, L4, L4, R3, R5, L2, R4, R5, R3, L2, L2, L4, L2, R2, L5, L4, R3, R1, L2, R2, R4, L1, L4, L4, L2, R2, L4, L1, L1, R4, L1, L3, L2, L2, L5, R5, R2, R5, L1, L5, R2, R4, R4, L2, R5, L5, R5, R5, L4, R2, R1, R1, R3, L3, L3, L4, L3, L2, L2, L2, R2, L1, L3, R2, R5, R5, L4, R3, L3, L4, R2, L5, R5"

dirs = [(0,1),(1,0),(0,-1),(-1,0)]

inp = input.split(", ")

def advance (dir, instr):
    if instr[0] == "R":
        dir += 1
    else:
        dir -= 1
    dir %= 4
    val = int(instr[1:])
    x = dirs[dir][0] * val
    y = dirs[dir][1] * val
    return (dir, x,y)


def part1():
    x = 0
    y = 0

    dir = 0

    for i in inp:
        (dir, dx, dy) = advance(dir, i)
        x += dx
        y += dy

    print x, y, abs(x)+abs(y)

def part2():
    x=0
    y=0
    dir = 0
    grid = [[0]*1000 for i in range(1000)]
    for i in inp:
        if i[0] == "R":
            dir += 1
        else:
            dir -= 1
        dir %= 4
        val = int(i[1:])
        dx,dy = dirs[dir]
        cont = 0

        for j in range(val):
            if grid[x+500][y+500] == 1:
                break
            else:
                grid[x+500][y+500] = 1
                x += dx
                y += dy
        else:
            cont = 1

        if cont == 0: break


    print x, y, abs(x)+abs(y)


if __name__ == "__main__":
    part1()
    part2()





