#!/bin/python3

total = []
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    ints = (3, 5, 15)
    divs = [(n - 1) // i for i in ints]
    sums = []
    for i, d in zip(ints, divs):
        sums.append(i * d * (d + 1) // 2)
    total.append(sums[0]+sums[1]-sums[2])

print('\n'.join(map(str, total)))
