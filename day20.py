with open ("day20.txt", "r") as f:
    ranges = sorted([tuple(map(int, l.split("-"))) for l in f.readlines()])
ranges.append((4294967295+1, 4294967295+2))

num = 1
ips = 0
for r in ranges:
    print (num+1, r)
    if num+1 < r[0]:
        print ("lowest is ", num+1)
        break
    num = r[1]

r2 = []
bot =

potentials = []
for i in range(len(ranges)-1):
    if ranges[i+1][0]-ranges[i][1]-1 > 0:
        potentials.append ((ranges[i][1]+1, ranges[i+1][0]-1))

print (potentials)

for i in range(len(potentials)):
    for r in ranges:
        if r[0] < potentials[i][0] < r[1]:
            print ("hit: p = {}, r = {}".format(potentials[i], r))
            potentials[i] = (r[1]+1, potentials[i][1])
            print ("updated p = ", potentials[i])
        elif r[0] < potentials[i][1] < r[1]:
            print("hit: p = {}, r = {}".format(potentials[i], r))
            potentials[i] = (potentials[i][0], r[0]-1)
            print("updated p = ", potentials[i])
        if potentials[i][0] > potentials[i][1]: potentials[i] = (0,0)


print (potentials)


print(sum([p[1]-p[0]+1 for p in potentials]))



print (sum([max(ranges[i+1][0]-ranges[i][1]-1, 0) for i in range(len(ranges)-1)]))
