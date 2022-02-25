import sys
sys.stdin = open("input.txt", 'rt')

if __name__ == "__main__":
    arr=input()
    zcount=0
    ocount=0
    before=arr[0]
    if before == '0':
        zcount+=1
    else:
        ocount+=1

    for idx, i in enumerate(arr):
        if idx==0:
            pass
        else:
            if i!= before and i=='1':
                ocount+=1
                before='1'
            elif i != before and i== '0':
                zcount+=1
                before='0'

    print(min(zcount, ocount))
