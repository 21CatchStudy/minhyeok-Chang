import sys
sys.stdin = open("input.txt", 'rt')

if __name__ == "__main__":
    n = int(input())
    array = list(map(int, input().split()))

    dy = [1 for i in range(n)]

    for i in range(n):
        for j in range(i):
            if array[i] > array[j]:
                dy[i] = max(dy[i], dy[j]+1)

    # dy[-1]값을 출력해서 틀렸었음
    # max값을 출력해야 최대 수열이 출력됨
    print(max(dy))
