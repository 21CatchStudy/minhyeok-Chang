import sys
sys.stdin = open("input.txt", 'rt')

if __name__ == "__main__":
    n = int(input())

    ways = list(input().split())

    now_x = 1
    now_y = 1

    for way in ways:

        if way == "L":
            now_y -= 1
            if now_y < 1:
                now_y += 1
        elif way == "R":
            now_y += 1
        elif way == "U":
            now_x -= 1
            if now_x < 1:
                now_x += 1
        else:
            now_x += 1

    print(now_x, now_y)
