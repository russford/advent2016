with open ("day20.txt", "r") as f:
    ranges = sorted([tuple(map(int, l.split("-"))) for l in f.readlines()])


low = ranges[0]
new_ranges = []
for r in ranges:
    if r[0] <= low[1]+1:
        low = (low[0], max(low[1],r[1]))
    else:
        new_ranges.append(low)
        low = r
if low != new_ranges[-1]: new_ranges.append(low)

print(4294967295+1 - sum([r[1]-r[0]+1 for r in new_ranges]))
