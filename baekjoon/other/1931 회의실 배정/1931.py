import sys
input = sys.stdin.readline
def solution():
    cur_start = cnt = 0
    while case_list:
        start, end = case_list.pop()

        if cur_start <= start:
            cnt += 1
            cur_start = end
    return cnt

N = int(input())
case_list = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: [x[1], x[0]], reverse=True)
print(solution())