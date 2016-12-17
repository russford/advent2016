test_code = """cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a"""


# cpy x y copies x (either an integer or the value of a register) into register y.
# inc x increases the value of register x by one.
# dec x decreases the value of register x by one.
# jnz x y jumps to an instruction y away (positive means forward; negative means backward), but only if x is not zero.

def val(v, registers):
    if "a" <= v[0] <= "d":
        return registers[v]
    else:
        return int(v)


def exec (instr, registers):
    instr = instr.split()
    if instr[0] == "cpy":
        registers[instr[2]] = val(instr[1], registers)
    if instr[0] == "inc":
        registers[instr[1]] += 1
    if instr[0] == "dec":
        registers[instr[1]] -= 1
    if instr[0] == "jnz":
        cmp = val(instr[1], registers)
        if cmp != 0:
            return int(instr[2])
    return 0

def run_code(code):
    registers = {"a": 0, "b": 0, "c": 0, "d": 0}
    code_ptr = 0
    print(code)
    i=0
    while code_ptr < len(code):
        # print("{}: {} | {}".format(code_ptr, code[code_ptr], sorted(registers.items())))
        jmp = exec(code[code_ptr], registers)
        if jmp == 0: jmp = 1
        code_ptr += jmp
    print (sorted(registers.items()))

with open("day12.txt", "r") as f:
    file_code = f.readlines()

run_code(file_code)
