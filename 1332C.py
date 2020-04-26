# python3

def solve(s, k):
    n = len(s)
    r = n//k
    res = 0
    for j in range(k//2):
        d = [0] * 26
        for i in range(r):
            d[ord(s[i*k+j]) - 97] += 1
            d[ord(s[i*k+k-1-j]) - 97] += 1
        res += 2*r - max(d)
    if k%2 == 1:
        d = [0] * 26
        for i in range(r):
            d[ord(s[i*k+k//2]) - 97] += 1
        res += r - max(d)
    return res


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        s = input()
        print(solve(s, k))
