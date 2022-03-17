import sys
sys.stdin = open("input.txt", 'rt')


def DFS(L, tmp_list):
    global cnt

    if L == len(numbers):
        if sum(tmp_list) == t:
            cnt += 1
    else:
        DFS(L+1, tmp_list + [numbers[L]])
        DFS(L+1, tmp_list + [-numbers[L]])


if __name__ == "__main__":
    numbers = list(map(int, input().split()))
    t = int(input())
    tmp_list = []

    cnt = 0
    DFS(0, tmp_list)
    print(cnt)


# 완전탐색
def solution(numbers, target):
    answer = 0
    graph = [0]
    for num in numbers:
        num_lst = []
        for i in graph:
            num_lst.append(i + num)
            num_lst.append(i - num)
        print(num_lst)
        graph = num_lst

    for j in graph:
        if j == target:
            answer += 1
    return answer
