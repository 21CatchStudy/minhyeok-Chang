import sys
sys.stdin = open("input.txt", 'rt')
from collections import deque

# stack 형식으로 풀기
def DFS(x):

    for i in range(1, n+1):
        # 아직 방문하지 않았고, 간선으로 연결된 정점이면 실행
        if ch[i] == 0 and table[x][i] == 1:
            ch[i] = 1
            res.append(i)
            DFS(i)  # 재귀

# queue 형식으로 풀기
def BFS(x):

    dQ = deque()
    # 큐 전처리 및 체크리스트 체크
    dQ.append(x)
    ch[x] = 1
    res.append(x)
    while dQ:
        now = dQ.popleft()
        for j in range(1, n+1):
            # 위 DFS와 동일
            if ch[j] == 0 and table[now][j] == 1:
                ch[j] = 1
                res.append(j)
                dQ.append(j)


if __name__ == "__main__":
    n, m, v = map(int, input().split())

    table = [[0] * (n+1) for _ in range(n+1)]
    ch = [0] * (n+1)    # 체크리스트

    # 이어진 간선 테이블에 입력
    for i in range(m):
        x, y = map(int, input().split())
        table[x][y] = 1
        table[y][x] = 1

    res = []
    res.append(v)
    ch[v] = 1
    DFS(v)
    for i in res:
        print(i, end=' ')
    print()

    ch = [0] * (n + 1)
    res = []
    BFS(v)
    for j in res:
        print(j, end=' ')




