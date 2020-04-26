# python3


def solve(a):
    n = len(a)
    prefix = [0] * (n+1)
    for i in range(n):
        prefix[i+1] = prefix[i] + a[i]
    begin, end = 0, 0
    res = 0
    s = set([0])
    while begin < n:
        while (end < n) and (prefix[end+1] not in s):
            end += 1
            s.add(prefix[end])
        res += end - begin
        s.remove(prefix[begin])
        begin += 1
    return res


if __name__ == '__main__':
    n = int(input())
    a = [int(i) for i in input().split()]
    print(solve(a))
