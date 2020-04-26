# python3


def solve(a, b):
    n = len(a)
    s = set()
    res = True
    for i in range(1, n):
        s.add(a[i-1])
        offset = b[i] - a[i]
        res &= (offset == 0) | (offset > 0 and (1 in s)) | (offset < 0 and (-1 in s))
    if res and a[0] == b[0]:
        return "YES"
    return "NO"


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = [int(i) for i in input().split()]
        b = [int(i) for i in input().split()]
        print(solve(a, b))
