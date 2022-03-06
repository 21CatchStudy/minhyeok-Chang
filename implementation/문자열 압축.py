import sys
sys.stdin = open("input.txt", 'rt')

if __name__ == "__main__":

    s = input()
    # 이전 틀린 코드
    # for i in range(2, len(s) // 2 + 1):
    #
    #     all_string = ''
    #     now_string = ''
    #     same_cnt = 1
    #
    #     # 0부터 시작한것이
    #     for j in range(0, len(s), i):
    #         if j+i >= len(s):
    #             all_string += s[j: len(s)]
    #
    #         if j == 0:
    #             now_string = s[j:j+i]
    #
    #         elif now_string == s[j:j+i]:
    #             same_cnt += 1
    #
    #         elif now_string != s[j:j+i]:
    #             if same_cnt != 1:
    #                 all_string = all_string + str(same_cnt) + now_string
    #
    #             # 이 부분을 놓쳤다
    #             else:
    #                 all_string = all_string + now_string
    #             same_cnt = 1
    #             now_string = s[j:j+i]
    #
    #     if small > len(all_string):
    #         wow = all_string
    #         print(wow)
    #         small = len(all_string)
    #
    #
    # print(small)

    res = []
    # if len(s) == 1:
    #     return 1
    # 자르는 단위 1부터 시작해야하는데 2부터 시작함
    # 그래서 틀렸음
    for i in range(1, len(s) // 2 + 1):

        all_string = ''
        now_string = s[:i]
        same_cnt = 1

        # 0부터 시작한것이 문제
        for j in range(i, len(s), i):
            # i를 더했을때 범위를 넘어 갔을 경우
            # 잘못 설계 
            # if j+i >= len(s):
            #     all_string += s[j: len(s)]

            if now_string == s[j:j+i]:
                same_cnt += 1

            else:
                if same_cnt != 1:
                    all_string = all_string + str(same_cnt) + now_string
                # 이 부분을 놓쳤다
                else:
                    all_string = all_string + now_string
                same_cnt = 1
                now_string = s[j:j+i]
        # for문이 끝나고 남은 알파벳들 더하는 부분
        if same_cnt != 1:
            all_string = all_string + str(same_cnt) + now_string
        else:
            all_string = all_string + now_string

        res.append(len(all_string))


    print(min(res))
