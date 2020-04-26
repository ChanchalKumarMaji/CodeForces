# python3


def solve(n, m):
    for i in range(n):
        if i == 0:
            print('W' + 'B'*(m-1))
        else:
            print('B'*m)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        solve(n, m)
