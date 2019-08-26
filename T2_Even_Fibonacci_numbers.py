#!/bin/python3
import sys


nums = int(input().strip())
for _ in range(nums):
    limit = int(input().strip())
    sum_, f, f1, f2 = 0, 0, 0, 2
    while f < limit:
        sum_ += f2
        f = 4 * f2 + f1
        f1 = f2; f2 = f
    print(sum_)