# Its left and center tiles are traps, but its right tile is not.
# Its center and right tiles are traps, but its left tile is not.
# Only its left tile is a trap.
# Only its right tile is a trap.

traps = ["^^.", ".^^", "^..", "..^"]

def next_line (line):
    check_line = "." + line + "."
    return ''.join(['^' if check_line[i:i+3] in traps else "." for i in range(len(line))])

def count_traps (line, n):
    count = 0
    for i in range(n):
        count += line.count(".")
        line = next_line(line)
    return count

puzzle_input = "^..^^.^^^..^^.^...^^^^^....^.^..^^^.^.^.^^...^.^.^.^.^^.....^.^^.^.^.^.^.^.^^..^^^^^...^.....^....^."

print (count_traps(puzzle_input, 400000))
