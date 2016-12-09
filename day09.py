import re

def block_len(regex, s):
    if "(" not in s:
        return len(s)
    else:
        m = regex.search(s)
        reps = int(m.group(3))
        chars = int(m.group(2))
        return len(m.group(1)) + reps * block_len(regex, m.group(4)[:chars]) + block_len(regex, m.group(4)[chars:])

def block_len_simp(regex, s):
    if "(" not in s:
        return len(s)
    else:
        m = regex.search(s)
        chars = int(m.group(2))
        reps = int(m.group(3))
        return len(m.group(1)) + chars * reps + block_len_simp(regex, m.group(4)[chars:])

def test_1():
    test_input = [("ADVENT", "ADVENT"), ("A(1x5)BC", "ABBBBBC"), ("(3x3)XYZ", "XYZXYZXYZ"), ("A(2x2)BCD(2x2)EFG", "ABCBCDEFEFG"), ("(6x1)(1x3)A", "(1x3)A"), ("X(8x2)(3x3)ABCY", "X(3x3)ABC(3x3)ABCY")]

    for i in test_input:
        d = decompress(i[0])
        print ("{} {} {}\n".format(i[0], d, d == i[1]))

def test_2():
    test_input = [("(27x12)(20x12)(13x14)(7x10)(1x12)A", 241920), ("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN", 445)]
    for i in test_input:
        print(i[0], len(decompress_2(i[0])), i[1])

with open ("day09.txt", "r") as f:
    inp = f.readlines()[0]

regex = re.compile("(.*?)\((\d+)x(\d+)\)(.*)")
print (block_len(regex, inp))


