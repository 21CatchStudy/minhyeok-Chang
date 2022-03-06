import sys
sys.stdin = open("input.txt", 'rt')

if __name__ == "__main__":
    s = input()

    a = []
    n = []
    for i in s:
        if i.isalpha():
            a.append(i)
        else:
            n.append(int(i))

    a.sort()
    sum_ = sum(n)
    res = a + [str(sum_)]
    print(''.join(res))
