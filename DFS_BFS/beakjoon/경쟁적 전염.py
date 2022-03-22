import sys
sys.stdin = open("input.txt", 'rt')
from collections import deque
# input = sys.stdin.readline()

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# if __name__ == "__main__":
#     n, k = map(int, sys.stdin.readline().split())
#     table = []
#     for _ in range(n):
#         table.append(list(map(int, sys.stdin.readline().split())))
#
#     s, xxx, yyy = map(int, sys.stdin.readline().split())
#
#     for _ in range(s):
#         dQ = deque()
#         for i in range(n):
#             for j in range(n):
#                 if table[i][j] != 0:
#                     dQ.append((i, j, table[i][j]))
#         new_dQ = sorted(dQ, key=lambda x:x[2])
#         new_dQ = deque(new_dQ)
#         while new_dQ:
#             x, y, v = new_dQ.popleft()
#
#             for k in range(4):
#                 xx = x + dx[k]
#                 yy = y + dy[k]
#                 if 0 <= xx < n and 0 <= yy < n and table[xx][yy] == 0:
#                     table[xx][yy] = v
#
#     print(table[xxx-1][yyy-1])

if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().split())
    table = []
    virus = []
    for i in range(n):
        table.append(list(map(int, sys.stdin.readline().split())))
        for j in range(n):
            if table[i][j] != 0:
                virus.append((table[i][j], i, j))

    s, xxx, yyy = map(int, sys.stdin.readline().split())

    virus.sort()
    dQ = deque(virus)
    cnt = 0
    while dQ:
        if cnt == s:
            break
        for _ in range(len(dQ)):
            v, x, y = dQ.popleft()

            for k in range(4):
                xx = x + dx[k]
                yy = y + dy[k]
                if 0 <= xx < n and 0 <= yy < n and table[xx][yy] == 0:
                    table[xx][yy] = v
                    dQ.append((v, xx, yy))
        else:
            cnt += 1
    print(table[xxx-1][yyy-1])



