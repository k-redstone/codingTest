import sys
sys.stdin = open("./input.txt", "r")
# abs 막힘
def solution(case):
    if len(case) == 1:
        return case
    mid_num = (len(case)+1) // 2
    left_item = solution(case[:mid_num])
    right_item = solution(case[mid_num:])
    if left_item[0][1] == right_item[0][1]:
        return left_item
    elif left_item[0][1] - right_item[0][1] == 1:
        return left_item
    elif left_item[0][1] - right_item[0][1] == -1:
        return right_item
    elif left_item[0][1] - right_item[0][1] == 2:
        return right_item
    elif left_item[0][1] - right_item[0][1] == -2:
        return left_item

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    case_list = list(map(int, input().split()))
    index_list = [[idx, item] for idx, item in enumerate(case_list)]
    result = solution(index_list)
    print(f'#{tc} {result[0][0]+1}')