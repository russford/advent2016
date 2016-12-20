def solve(n):
    elves = [1]*n
    while sum(map(lambda x: x>0, elves)) > 1:
        i = 0
        while i < n:
            while i<n and elves[i] == 0: i+=1
            if i < n:
                j = (i+1)%n
                while elves[j] == 0 and i != j: j = (j+1)%n

                if j != i:
                    elves[i] += elves[j]
                    elves[j] = 0
                    i = j+1
    return elves.index(max(elves))+1

def solve2(n):
    elves = [i+1 for i in range(n)]
    i = 0
    a = len(elves)
    while a > 1:
        j = (a//2+i)%a
        del elves[j]
        if i == a-1:
            i = 0
        else:
            i = i+1
        a = len(elves)
    return elves


key = 3014603


e = solve2(key)

print (e)


