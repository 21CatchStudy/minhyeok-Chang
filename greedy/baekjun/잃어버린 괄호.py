
if __name__ == "__main__":
    v = input()

    s = v.split('-')

    sum = 0
    # 시작 부분에는 괄호가 들어가지 않는다.
    # 그래서 0 인덱스의 값은 더해준다.
    for i in s[0].split('+'):
        sum += int(i)

    # 다음부턴 - 부호 이후의 값들이기 때문에
    # 전부 빼준다. 
    for j in s[1:]:
        for k in j.split('+'):
            sum -= int(k)

    print(sum)
