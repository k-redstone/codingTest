import sys
# from math import inf
sys.stdin = open("./input.txt", "r")

T = int(input())

def back(idx, sum_num):
    global small
    if sum_num == B:
        small = 0
        return
    if sum_num - B > small:
        return
    if idx >= N:
        if sum_num >= B:
            small = sum_num - B
        return
    for num in range(2):
        sub_set[idx] = num
        if num == 0:
            back(idx + 1, sum_num)
        else:
            back(idx+1, sum_num + h_list[idx])
        sub_set[idx] = 0


for tc in range(1, T+1):
    N, B = map(int, input().split())
    h_list = list(map(int, input().split()))
    sub_set = [0]*N
    small = 10000*N
    back(0, 0)
    print(f'#{tc} {small}')
