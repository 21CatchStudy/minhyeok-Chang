import sys
sys.stdin = open("input.txt", 'rt')

if __name__ == "__main__":
    x = int(input())

    case = list(map(int, input().split()))
    reverse_case = case[::-1]

    increase = [1 for i in range(x)]  # 가장 긴 증가하는 부분 수열
    decrease = [1 for i in range(x)]  # 가장 긴 감소하는 부분 수열(reversed)

    for i in range(x):
        for j in range(i):
            if case[i] > case[j]:
                increase[i] = max(increase[i], increase[j] + 1)
            if reverse_case[i] > reverse_case[j]:
                decrease[i] = max(decrease[i], decrease[j] + 1)

    result = [0 for i in range(x)]
    for i in range(x):
        result[i] = increase[i] + decrease[x - i - 1] - 1

    print(max(result))

#     dy = [1] * n
#     asd = list()
#     asd.append([arr[0]])
#
#     for i in range(n):
#         largest = 0
#         large_v = 0
#         for j in range(i):
#             if arr[i] > arr[j]:
#                 if dy[j] > largest:
#                     largest = dy[j]
#                     large_v = j
#                     print(large_v)
#                 dy[i] = max(dy[i], dy[j]+1)
#         asd.append((asd[large_v] + [i]))
#
#     print(asd)
#
#
#
#
#
