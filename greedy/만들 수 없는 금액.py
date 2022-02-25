import sys
sys.stdin = open("input.txt", 'rt')
from itertools import combinations

if __name__ == "__main__":
    n=int(input())
    arr=list(map(int, input().split()))

    coin_sum=1
    arr.sort()

    combi_sums = set()
    for i in range(n):
        tmp = combinations(arr, i+1)
        for j in tmp:
            combi_sums.add(sum(j))

    now_number = 1
    while True:
        if now_number in combi_sums:
            now_number += 1
        else:
            break

    print(now_number)
