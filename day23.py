test_code = """cpy 2 a
tgl a
tgl a
tgl a
cpy 1 a
dec a
dec a"""


# cpy x y copies x (either an integer or the value of a register) into register y.
# inc x increases the value of register x by one.
# dec x decreases the value of register x by one.
# jnz x y jumps to an instruction y away (positive means forward; negative means backward), but only if x is not zero.


# For one-argument instructions, inc becomes dec, and all other one-argument instructions become inc.
# For two-argument instructions, jnz becomes cpy, and all other two-instructions become jnz.
# The arguments of a toggled instruction are not affected.
# If an attempt is made to toggle an instruction outside the program, nothing happens.
# If toggling produces an invalid instruction (like cpy 1 2) and an attempt is later made to execute that instruction, skip it instead.
# If tgl toggles itself (for example, if a is 0, tgl a would target itself and become inc a), the resulting instruction is not executed until the next time it is reached.

def toggle (instr):
    instr = instr.split()
    if len(instr) == 2:
        if instr[0] == "inc":
            return "dec " + instr[1]
        else: return "inc " + instr[1]
    if len(instr) == 3:
        if instr[0] == "jnz":
            return "cpy {} {}".format(instr[1], instr[2])
        else:
            return "jnz {} {}".format(instr[1], instr[2])

def val(v, registers):
    if "a" <= v[0] <= "d":
        return registers[v]
    else:
        return int(v)


def exec (code, code_ptr, registers):
    if code_ptr == 2:
        registers["a"] = registers["a"] * registers["b"]
        registers["b"] -= 1
        registers["c"] = 2 * registers["b"]
        registers["d"] = 0
        return 14

    if code_ptr == 20:
        registers["a"] += 95*96
        return 6

    instr = code[code_ptr].split()
    if instr[0] == "cpy":
        if instr[2] in registers:
            registers[instr[2]] = val(instr[1], registers)
    if instr[0] == "inc":
        if instr[1] in registers:
            registers[instr[1]] += 1
    if instr[0] == "dec":
        if instr[1] in registers:
            registers[instr[1]] -= 1
    if instr[0] == "jnz":
        cmp = val(instr[1], registers)
        if cmp != 0:
            return val(instr[2], registers)
    if instr[0] == "tgl":
        jmp = val(instr[1], registers)
        if code_ptr+jmp < len(code):
            new_ins = toggle(code[code_ptr+jmp])
            print ("toggled {}:{} to {}".format(code_ptr+jmp, code[code_ptr+jmp], new_ins))
            code[code_ptr+jmp] = new_ins
            if code_ptr+jmp == 18:
                print ('\n'.join(code[16:]))
    return 0

def run_code(code):
    registers = {"a": 12, "b": 0, "c": 0, "d": 0}
    code_ptr = 0
    print(code)
    i=0
    while code_ptr < len(code):
        jmp = exec(code, code_ptr, registers)
        if code_ptr < 2 or 21 > code_ptr > 15 or code_ptr == 10 or code_ptr > 23:
            print("{:>3}: {:<8} | {}".format(code_ptr, code[code_ptr], '   '.join(["{}:{:>5}".format(k,v) for k,v in sorted(registers.items())])))
        if jmp == 0: jmp = 1
        code_ptr += jmp
        i += 1
    print (sorted(registers.items()))

with open("day23.txt", "r") as f:
    file_code = [l.strip('\n') for l in f.readlines()]

run_code(file_code)
