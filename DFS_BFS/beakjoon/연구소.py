from itertools import combinations
from collections import deque

import sys
import copy
sys.stdin = open("input.txt", 'rt')

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# indexError
def BFS():

    dQ = deque()
    for kx, ky in twos:
        dQ.append((kx, ky))

    while dQ:
        nx, ny = dQ.popleft()

        for ii in range(4):
            xx = nx + dx[ii]
            yy = ny + dy[ii]

            if 0 <= xx < m and 0 <= yy < n and tmp_table[xx][yy] == 0:
                tmp_table[xx][yy] = 2
                dQ.append((xx, yy))


if __name__ == "__main__":
    n, m = map(int, input().split())

    table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    zeros = []
    twos = []
    # 0좌표 구하기, 2좌표 구하기
    for i in range(n):
        for j in range(m):
            if table[i][j] == 0:
                zeros.append((i, j))
            if table[i][j] == 2:
                twos.append((i, j))

    c_zeros = combinations(zeros, 3)
    res = []

    # 콤비네이션 돌기
    for c in c_zeros:
        tmp_table = copy.deepcopy(table)
        for x, y in c:
            tmp_table[x][y] = 1

        BFS()

        tmp = 0
        # BFS 다 돌고 0 개수 구하기
        for iii in range(n):
            for jjj in range(m):
               if tmp_table[iii][jjj] == 0:
                   tmp += 1
        res.append(tmp)


    print(max(res))



