from itertools import combinations
import sys
sys.stdin = open('./input.txt', 'r')

T = int(input())
case_list = [i for i in range(1, 13)]

for _ in range(T):
    N, K = list(map(int, input().split()))
    com_list = list(combinations(case_list, N))
    cnt = 0
    for item in com_list:
        if sum(item) == K:
            cnt += 1

    print(f'#{_ + 1} {cnt}')


