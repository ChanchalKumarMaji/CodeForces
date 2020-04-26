# python3


def solve(p, c):
    n = len(p)
    if p[0] < c[0]:
        return "NO"
    for i in range(1, n):
        if (p[i-1] > p[i]) or (c[i-1] > c[i]) or (p[i] < c[i]) or (p[i]-p[i-1] < c[i]-c[i-1]):
            return "NO"
    return "YES"


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        p = []
        c = []
        for _ in range(n):
            x, y = map(int, input().split())
            p.append(x)
            c.append(y)
        print(solve(p, c))
