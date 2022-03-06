import sys
sys.stdin = open("input.txt", 'rt')

if __name__ == "__main__":
    place = input()

    alphabet = [0, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    steps = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]

    x = alphabet.index(place[0])
    y = int(place[1])

    cnt = 0
    for step in steps:
        xx = x + step[0]
        yy = y + step[1]

        if 1 <= xx <= 8 and 1 <= yy <= 8:
           cnt += 1

    print(cnt)
