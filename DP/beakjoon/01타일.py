import sys
sys.stdin = open("input.txt", 'rt')

if __name__ == "__main__":
    n = int(sys.stdin.readline())

    dy = [0] * n

    if n == 1:
        print(1)
    else:
        dy[0] = 1
        dy[1] = 2

        for i in range(2, n):
            dy[i] = (dy[i-2] + dy[i-1]) % 15746

        print(dy[n-1] % 15746)
