import sys
from collections import deque

sys.stdin = open("./input.txt", "r")

def merge(l, r):
    global cnt
    result = []
    l_idx = r_idx = 0
    if l[-1] > r[-1]:
        cnt += 1
    while len(l) > l_idx or len(r) > r_idx:
        if len(l) > l_idx and len(r) > r_idx:
            if l[l_idx] <= r[r_idx]:
                result.append(l[l_idx])
                l_idx += 1
            else:
                result.append(r[r_idx])
                r_idx += 1
        elif len(l) > l_idx:
            result.append(l[l_idx])
            l_idx += 1
        elif len(r) > r_idx:
            result.append(r[r_idx])
            r_idx += 1
    return result

def divide(n, case):
    if n == 1:
        return case
    mid = n//2
    left = divide(mid, case[:mid])
    right = divide(n-mid, case[mid:])
    return merge(left, right)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    case_list = list(map(int, input().split()))
    cnt = 0
    arr = divide(N, case_list)

    print(f'#{tc} {arr[N//2]} {cnt}')