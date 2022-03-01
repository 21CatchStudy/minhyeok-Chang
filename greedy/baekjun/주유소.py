import sys
sys.stdin = open("input.txt", 'rt')

# if __name__ == "__main__":
#     n = int(input())
#     dis = list(map(int, input().split()))
#     price = list(map(int, input().split()))
    # ch = [0] * n
    #
    # res = 0
    # idx = 0
    # while idx < n:
    #     res += dis[idx] * price[idx]
    #     ch[idx] = 1
    #     for j in range(idx+1, n):
    #         if ch[j] == 0 and ch[j] > price[idx]:
    #             ch[j] = 1
    #             print(dis[j], price[idx])
    #             res += dis[j] * price[idx]
    #         elif ch[j] == 0 and ch[j] < price[idx]:
    #             idx = j
    #             break
    #     else:
    #         break


# 정답 코드
if __name__ == "__main__":
    n = int(input())
    roads = list(map(int, input().split()))
    costs = list(map(int, input().split()))

    # 정답 코드

    res = roads[0] * costs[0]
    m = costs[0]  # 지금까지 가장 가격이 낮은 값
    dist = 0  # 지금까지 달려온 거리

    for i in range(1, n - 1):
        if costs[i] < m:
            res += m * dist
            dist = roads[i]
            m = costs[i]
        else:
            dist += roads[i]

        if i == n - 2:
            res += m * dist
    print(res)




