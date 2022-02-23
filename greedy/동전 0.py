import sys
sys.stdin = open("input.txt")
if __name__ == "__main__":
    n, k = map(int, input().split())
    coins = []
    for _ in range(n):
        coins.append(int(input()))
    coins.sort(reverse=True)
    res = 0
    for coin in coins:
        if coin <= k:

            res += k//coin
            k = k % coin

        if k == 0:
            break

    print(res)
