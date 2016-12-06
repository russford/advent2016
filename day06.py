def most_common(lst):
    return max(set(lst), key=lst.count)

def least_common(lst):
    return min(set(lst), key=lst.count)

def decode_1 (msg):
    return ''.join([most_common(m) for m in zip(*msg)])

def decode_2 (msg):
    return ''.join([least_common(m) for m in zip(*msg)])


test_input = ["eedadn",
              "drvtee",
              "eandsr",
              "raavrd",
              "atevrs",
              "tsrnev",
              "sdttsa",
              "rasrtv",
              "nssdts",
              "ntnada",
              "svetve",
              "tesnvt",
              "vntsnd",
              "vrdear",
              "dvrsen",
              "enarar"]

with open ("day06.txt", "r") as f:
    run_input = f.readlines()

print (decode_1(run_input))
print (decode_2(run_input))