import sys
sys.stdin = open("input.txt", 'rt')

if __name__ == "__main__":
    n, m = map(int, input().split())

    arrs = [list(map(int, input().split())) for _ in range(n)]

    res = 0
    for arr in arrs:
        min_ = min(arr)
        if res < min_:
            res = min_

    print(res)
