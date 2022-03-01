import sys
sys.stdin = open("input.txt", 'rt')

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort()

    sum_ = 0
    all_sum = 0

    for i in arr:
        sum_ += i
        all_sum += sum_

    print(all_sum)
