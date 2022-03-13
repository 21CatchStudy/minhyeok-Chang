import sys
sys.stdin = open("input.txt", 'rt')
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def BFS(x, y):

    dQ = deque()
    dQ.append((x, y))
    while dQ:
        tx, ty = dQ.popleft()
        town_list[-1] += 1
        for k in range(4):
            xx = tx + dx[k]
            yy = ty + dy[k]
            if 0 <= xx < n and 0 <= yy < n and table[xx][yy] == '1':
                table[xx][yy] = '0'
                dQ.append((xx, yy))


if __name__ == "__main__":
    n = int(input())

    table = []

    for _ in range(n):
        table.append(list(input()))
    town_list = []

    for i in range(n):
        for j in range(n):
            if table[i][j] == '1':
                town_list.append(0)
                # 한 마을의 첫 집을 방문 했을때
                # 체크를 하지 않아 틀렸다.
                table[i][j] = '0'
                BFS(i, j)

    print(len(town_list))
    # 정렬 안해서 틀렸던 문제...
    # 문제의 조건을 잘보자
    town_list.sort()
    for town in town_list:
        print(town)

