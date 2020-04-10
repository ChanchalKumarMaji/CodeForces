# python3


def solve(a):
    c = [0] * len(a)
    m = []
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]:
        for j in range(len(a)):
            if (a[j] % p == 0) and (c[j] == 0):
                if p not in m:
                    m.append(p)
                c[j] = len(m)
    print(len(m))
    print(" ".join([str(e) for e in c]))


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = [int(i) for i in input().split()]
        solve(a)
