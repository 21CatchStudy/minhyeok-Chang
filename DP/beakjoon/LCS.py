import sys
sys.stdin = open("input.txt", 'rt')

if __name__ == "__main__":
    first = input()
    second = input()

    flen = len(first)
    slen = len(second)

    table = [[0] * (slen + 1) for _ in range(flen + 1)]

    for i in range(1, flen+1):
        for j in range(1, slen+1):
            if first[i-1] == second[j-1]:
                table[i][j] = table[i-1][j-1] + 1
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])

    print(table[-1][-1])

    # https://myjamong.tistory.com/317
    # 1차원 테이블을 이용하는 더 효율적인 방법
    # import sys
    #
    # read = sys.stdin.readline
    #
    # word1, word2 = read().strip(), read().strip()
    # l1, l2 = len(word1), len(word2)
    # cache = [0] * l2
    #
    # for i in range(l1):
    #     cnt = 0
    #     for j in range(l2):
    #         if cnt < cache[j]:
    #             cnt = cache[j]
    #         elif word1[i] == word2[j]:
    #             cache[j] = cnt + 1
    # print(max(cache))


    # print(first, second)
    # arr = []
    # for i in range(len(first)):
    #     for j in range(len(second)):
    #         if first[i] == second[j]:
    #             arr.append(j)
    #
    # print(arr)
    # dy = [1] * len(arr)
    # for ii in range(len(arr)):
    #     for jj in range(ii):
    #         if arr[ii] > arr[jj]:
    #             dy[ii] = max(dy[ii], dy[jj]+1)
    # print(dy)
    # print(max(dy))


