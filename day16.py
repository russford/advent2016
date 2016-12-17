def fill_alg(a):
    return a + "0" + ''.join(["1" if c == "0" else "0" for c in reversed(a)])


def checksum (s):
    while len(s) % 2 == 0:
        s = ''.join(["1" if a[0] == a[1] else "0" for a in [s[i:i+2] for i in range(0, len(s), 2)]])
    return s


def gen_data_checksum (s, n):
    while len(s) < n:
        s = fill_alg(s)
    return checksum(s[:n])

s = "00101000101111010"

print(gen_data_checksum(s, 35651584))



