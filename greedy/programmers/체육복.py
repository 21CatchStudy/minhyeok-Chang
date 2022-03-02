import sys
sys.stdin = open("input.txt", 'rt')

if __name__ == "__main__":
    n = int(input())
    lost = list(map(int, input().split()))
    reserve = list(map(int, input().split()))

    # arr = [x+1 for x in range(n)]
    #
    # reserve2 = set()
    #
    # for i in reserve:
    #     if i == 1:
    #         reserve2.add(1)
    #         reserve2.add(2)
    #     elif i == n:
    #         reserve2.add(n)
    #         reserve2.add(n-1)
    #     else:
    #         reserve2.add(i)
    #         reserve2.add(i-1)
    #         reserve2.add(i+1)
    #
    # final_lost = set(lost) - reserve2
    # arr = set(arr) - final_lost
    #
    # print(len(arr))

    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)

    arr = [x+1 for x in range(n)]

    for i in reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)

    print(len(arr) - len(set_lost))






