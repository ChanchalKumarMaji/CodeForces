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


def solve(n):
    p = 1
    for k in range(1, 30):
        p += 1 << k
        if n % p == 0:
            return n // p


if __name__ == '__main__':
    t = iint()
    for _ in range(t):
        n = iint()
        print(solve(n))
