import sys
sys.stdin = open("input.txt", 'rt')

if __name__ == "__main__":
    t = int(input())
    cases = []
    for _ in range(t):
        cases.append(int(input()))

    money = [25, 10, 5, 1]
    res = []

    for case in cases:
        for i in money:
            if case >= i:
                tmp = case // i
                case = case % i
                print(tmp, end=' ')
            else:
                print(0, end=' ')
        print()








