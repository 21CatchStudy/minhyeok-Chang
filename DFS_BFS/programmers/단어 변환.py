import sys
sys.stdin = open("input.txt", 'rt')
from collections import deque


def check_words(w1, w2):

    cnt = 0
    for i in range(len(w1)):
        if w1[i] == w2[i]:
            cnt += 1
    if cnt == len(w1) - 1:
        return True
    else:
        return False


def BFS(begin):
    global target
    dQ = deque()
    cnt = 0
    if target not in words:
        return 0

    for j in words:
        if check_words(begin, j):
            words.remove(j)
            dQ.append(j)

    while dQ:
        cnt += 1
        for k in range(len(dQ)):
            tmp = dQ.popleft()
            if tmp == target:
                return cnt
            else:
                for ii in words:
                    if check_words(tmp, ii):
                        words.remove(ii)
                        dQ.append(ii)
    else:
        return 0


if __name__ == "__main__":

    begin = input()
    begin = list(begin)

    target = input()

    words = ["hot", "dot", "dog", "lot", "log", "cog"]

    cnt = BFS(begin)

    print(cnt)
