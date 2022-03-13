import sys
sys.stdin = open("input.txt", 'rt')
from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def BFS():

    while dQ:
        tx, ty = dQ.popleft()
        for k in range(4):
            xx = tx + dx[k]
            yy = ty + dy[k]
            # 주변의 토마토가 익지 않은 토마토 일때
            if 0 <= xx < m and 0 <= yy < n and table[xx][yy] == 0:
                # 토마토 익음
                table[xx][yy] = 1
                # 일수 늘리기
                ch[xx][yy] = ch[tx][ty] + 1
                dQ.append((xx, yy))


if __name__ == "__main__":
    n, m = map(int, input().split())

    table = [list(map(int, input().split())) for _ in range(m)]

    ch = [[0] * n for _ in range(m)]

    dQ = deque()
    # 익은 토마토 찾기
    for i in range(m):
        for j in range(n):
            if table[i][j] == 1:
                dQ.append((i, j))
                ch[i][j] = 1
    BFS()

    # 끝까지 익지 않은 토마토 확인 및
    # 최소 날짜 구하기
    largest = -2147000000
    not_real_tomato = False
    for ii in range(m):
        for jj in range(n):
            # 익지 않은 토마토 존재
            if table[ii][jj] == 0:
                print(-1)
                not_real_tomato = True
                break
            if ch[ii][jj] > largest:
                largest = ch[ii][jj]

        if not_real_tomato:
            break
    else:
        print(largest-1)

