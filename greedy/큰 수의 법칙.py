import sys
sys.stdin = open("input.txt", 'rt')

if __name__ == "__main__":
    n, m, k = map(int, input().split())

    arr = list(map(int, input().split()))
   
    cnt = 0
    arr.sort()
    first = arr[-1]
    second = arr[-2]
    # 처음 풀이
    # while cnt < m:
    #     for _ in range(k):
    #         res += first
    #         cnt += 1
    #     res += second
    #     cnt += 1
    
    # 보다 효율적인 
    pattern = first*k + second

    a = m // (k+1)
    b = m % (k+1)

    res = pattern * a + first * b

    print(res)

