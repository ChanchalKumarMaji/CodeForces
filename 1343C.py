# python3

##=====================================================
from sys import stdin, stdout
from collections import defaultdict, Counter
from functools import lru_cache
from math import gcd, floor, ceil
 
def ilist():
    return [int(x) for x in stdin.readline().strip().split(" ")]
def iint():
    return int(stdin.readline().strip())
def istr():
    return stdin.readline().strip()
##=====================================================


def solve(a):
    n = len(a)
    res = 0
    prev = 0
    for i in range(1, n):
        if a[i-1] * a[i] < 0:
            res += max(a[prev:i])
            prev = i
    res += max(a[prev:])
    return res


if __name__ == '__main__':
    t = iint()
    for _ in range(t):
        n = iint()
        a = ilist()
        print(solve(a))
