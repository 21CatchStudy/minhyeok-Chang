from collections import deque
import sys
sys.stdin = open("input.txt", 'rt')

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def BFS(v):
    dQ = deque()
    dQ.append((table[v], v))

    while dQ:
        list_, idx = dQ.popleft()
        for j in list_:
            if ch[j] == -1:
                ch[j] = ch[idx] + 1
                dQ.append((table[j], j))


if __name__ == "__main__":
    # input().split()으로 하니깐 시간초과 발생 
    n, m, k, x = map(int, sys.stdin.readline().rstrip().split())

    # k => 거리정보, x => 출발 도시 번호

    table = [[] for _ in range(n+1)]
    ch = [-1] * (n + 1)
    for i in range(m):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        table[a].append(b)

    ch[x] = 0
    BFS(x)

    res = []
    for idx, ii in enumerate(ch):
        if ii == k:
            res.append(idx)

    if len(res) == 0:
        print(-1)
    else:
        res.sort()
        for jj in res:
            print(jj)



# 2차원 테이블 형식으로 풀려 했는데 잘 풀리지 않아 링크드 리스트 방식으로 풀어봄
# def BFS(v):
#     dQ = deque()
#     dQ.append((v, v))
#
#     while dQ:
#         nx, ny = dQ.popleft()
#         for c in range(4):
#             xx = nx + dx[c]
#             yy = ny + dy[c]
#             if 0 <= xx < n and 0 <= yy < n and table[xx][yy] == 1:
#
#
#
# if __name__ == "__main__":
#     n, m, k, x = map(int, input().split())
#
#     # k => 거리정보, x => 출발 도시 번호
#
#     table = [[0] * n for _ in range(n)]
#
#     for i in range(m):
#         a, b = map(int, input().split())
#         table[a][b] = 1
#
#     ch = [[0] * n for _ in range(n)]
#
#     res = []
#     BFS(x-1)
#     res.sort(reverse=True)
#
#     if len(res) == 0:
#         print(-1)
#     else:
#         for j in res:
#             print(j)

