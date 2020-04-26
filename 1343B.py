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
    k = n // 2
    if k % 2 == 0:
        print("YES")
        res = [2*i for i in range(1, k+1)] + [2*i-1 for i in range(1, k+1)]
        res[-1] += k
        print(" ".join([str(e) for e in res]))
    else:
        print("NO")


if __name__ == '__main__':
    t = iint()
    for _ in range(t):
        n = iint()
        solve(n)
