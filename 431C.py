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


# Return the number of ways to get n using 1, 2, ..., k.
def solve(n, k):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n+1):
        for j in range(1, k+1):
            if i-j >= 0:
                dp[i] += dp[i-j]
    return dp[n]


if __name__ == '__main__':
    n, k, d = ilist()
    print((solve(n, k) - solve(n, d-1)) % 1000_000_007)
