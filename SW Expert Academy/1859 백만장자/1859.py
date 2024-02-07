import sys
sys.stdin = open("./input.txt", "r")

T = int(input())


def solution(case_num, case_list):
    sum_num = 0
    max_price = case_list[-1]
    for num in range(-1, -case_num, -1):
        if max_price > case_list[num-1]:
            sum_num += max_price - case_list[num-1]
        else:
            max_price = case_list[num-1]
    return sum_num

for tc in range(1, T+1):
    case_num = int(input())
    case_list = list(map(int, input().split()))
    print(f'#{tc} {solution(case_num, case_list)}')
