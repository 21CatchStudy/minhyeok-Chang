import sys
sys.stdin = open("input.txt", 'rt')

if __name__ == "__main__":
    h = int(input())

    cnt = 0

    for i in range(h+1):
        for j in range(60):
            for k in range(60):
                if '3' in str(i) + str(j) + str(k):
                    cnt += 1
    print(cnt)

