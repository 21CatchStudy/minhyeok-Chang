from collections import deque
import sys
sys.stdin = open("input.txt", 'rt')

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def BFS(x, y):
    global cnt
    dQ = deque()
    dQ.append((x, y))

    while dQ:
        nx, ny = dQ.popleft()

        for i in range(4):
            xx = nx + dx[i]
            yy = ny + dy[i]

            if 0 <= xx < n and 0 <= yy < m and table[xx][yy] == '1':
                table[xx][yy] = '0'
                ch[xx][yy] = ch[nx][ny] + 1
                dQ.append((xx, yy))


if __name__ == "__main__":
    n, m = map(int, input().split())

    table = [list(input()) for _ in range(n)]
    ch = [[0] * (m) for _ in range(n)]

    ch[0][0] = 1
    table[0][0] = '0'

    BFS(0, 0)
    print(ch[n-1][m-1])







