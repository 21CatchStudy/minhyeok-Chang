import sys
sys.stdin = open("input.txt", 'rt')

if __name__ == "__main__":
    n = int(input())
    array = []
    for _ in range(n):
        array.append(list(map(int, sys.stdin.readline().split())))

    array.sort()

    dy = [1] * n
    for i in range(n):
        for j in range(i):
            if array[i][1] > array[j][1]:
                dy[i] = max(dy[i], dy[j]+1)

    print(len(array) - max(dy))


