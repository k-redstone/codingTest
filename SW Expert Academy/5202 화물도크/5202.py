import sys
sys.stdin = open("./input.txt", "r")

T = int(input())

def solution():
    cnt = cur_end = 0
    while time_table:
        start_time, end_time = time_table.pop()
        if cur_end <= start_time:
            cnt += 1
            cur_end = end_time
    return cnt

for tc in range(1, T+1):
    N = int(input())
    time_table = list(sorted([list(map(int, input().split())) for _ in range(N)], key=lambda item: item[1], reverse=True))
    # print(time_table)
    print(f'#{tc} {solution()}')
