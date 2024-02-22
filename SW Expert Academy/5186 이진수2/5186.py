import sys
sys.stdin = open("./input.txt", "r")
T = int(input())

for tc in range(1, T+1):
    N = float(input())
    bin_num = ''
    for i in range(1, 13):
        if N >= 2 ** -i:
            bin_num += '1'
            N -= 2 ** -i
        else:
            bin_num += '0'
        if N == 0:
            break
    else:
        bin_num = 'overflow'
    print(f'#{tc} {bin_num}')