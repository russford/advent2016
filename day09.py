import re, unittest

def block_len_1(regex, s):
    if "(" not in s:
        return len(s)
    else:
        m = regex.search(s)
        reps, chars = int(m.group(3)), int(m.group(2))
        return len(m.group(1)) + chars * reps + block_len_1(regex, m.group(4)[chars:])


def block_len_2(regex, s):
    if "(" not in s:
        return len(s)
    else:
        m = regex.search(s)
        reps, chars = int(m.group(3)), int(m.group(2))
        return len(m.group(1)) + reps * block_len_2(regex, m.group(4)[:chars]) + block_len_2(regex, m.group(4)[chars:])


class Day09Test(unittest.TestCase):

    regex = re.compile("(.*?)\((\d+)x(\d+)\)(.*)")

    def test_part1(self):
        test_input = [("ADVENT", "ADVENT"), ("A(1x5)BC", "ABBBBBC"), ("(3x3)XYZ", "XYZXYZXYZ"), ("A(2x2)BCD(2x2)EFG", "ABCBCDEFEFG"), ("(6x1)(1x3)A", "(1x3)A"), ("X(8x2)(3x3)ABCY", "X(3x3)ABC(3x3)ABCY")]
        for i in test_input:
            self.assertEqual(block_len_1(self.regex, i[0]), len(i[1]))

    def test_part2(self):
        test_input = [("(27x12)(20x12)(13x14)(7x10)(1x12)A", 241920), ("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN", 445)]
        for i in test_input:
            self.assertEqual(block_len_2(self.regex, i[0]), i[1])

#unittest.main()

with open ("day09.txt", "r") as f:
    inp = f.readlines()[0]

regex = re.compile("(.*?)\((\d+)x(\d+)\)(.*)")
print (block_len_1(regex, inp))
print (block_len_2(regex, inp))


