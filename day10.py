import re
from collections import defaultdict

test_input = ["value 5 goes to bot 2","bot 2 gives low to bot 1 and high to bot 0","value 3 goes to bot 1","bot 1 gives low to output 1 and high to bot 0", "bot 0 gives low to output 2 and high to output 0", "value 2 goes to bot 2"]

def give (bots, outputs, dest, chip):
    dest = dest.split()
    if dest[0] == "bot":
        bots[int(dest[1])] += [chip]
    else:
        outputs[int(dest[1])] +=  [chip]


def process(instr):
    bots = defaultdict(lambda: [])
    gives = {}
    outputs = defaultdict(lambda: [])
    for i in instr:
        if i.startswith ("value"):
            value, botnum = map(int, re.findall("(\d+)", i))
            bots[botnum] += [value]
        else:
            bot, low_dest, high_dest = re.findall("(bot \d+|output \d+)", i)
            bot = int(bot.split()[1])
            gives[bot] = (low_dest, high_dest)


    while gives:
        for bot, chips in bots.items():
            if len(chips) == 2:
                low, high = gives[bot]
                print ("bot {} giving {} to {} and {} to {}".format(bot, max(chips), high, min(chips), low))
                if max(chips) == 61 and min(chips) == 17: print ("answer: ", bot)
                give (bots, outputs, high, max(chips))
                give (bots, outputs, low, min(chips))
                bots[bot] = []
                break
        else:
            return bots, gives, outputs


with open("day10.txt", "r") as f:
    file_input = f.readlines()

bots, gives, outputs = process(file_input)

print (outputs)

print (outputs[0][0] * outputs[1][0] * outputs[2][0])
