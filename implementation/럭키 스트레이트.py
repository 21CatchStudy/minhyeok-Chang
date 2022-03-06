import sys
sys.stdin = open("input.txt", 'rt')

if __name__ == "__main__":
    score = input()

    ls = 0
    rs = 0

    for i in range(len(score) // 2):
        ls += int(score[i])
        rs += int(score[-(i+1)])

    if ls == rs:
        print("LUCKY")

    else:
        print("READY")



