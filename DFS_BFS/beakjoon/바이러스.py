import sys
sys.stdin = open("input.txt", 'rt')


def DFS(x):
    global cnt
    for i in range(2, n+1):
        if table[x][i] == 1 and ch[i] == 0:
            ch[i] = 1
            cnt += 1
            DFS(i)


if __name__ == "__main__":
    n = int(input())
    a = int(input())

    # 좌표가 1부터 주어지기 때문에 n+1까지 
    table = [[0] * (n+1) for _ in range(n+1)]
    for _ in range(a):
        x, y = map(int, input().split())
        # 가중치가 오고 가는것 상관없이 같다는 것을
        # 생각 못하고 x, y에만 1을 넣어서 틀렸었다.
        table[x][y] = 1
        table[y][x] = 1

    ch = [0] * (n+1)

    cnt = 0
    ch[1] = 1
    DFS(1)

    print(cnt)


