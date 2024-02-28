import sys
sys.stdin = open("./input.txt", "r")


T = int(input())

def solution(start, cnt, prev_num):
    if cnt == 0:
        can_number.append(prev_num)
        return
    if start >= len(case_list):
        can_number.append(prev_num)
        return
    switch_idx = -1
    temp = 0
    for idx in range(start+1, len(case_list)):
        if case_list[start] <= case_list[idx]:
            if temp <= case_list[idx]:
                temp = case_list[idx]
                switch_idx = idx
    if switch_idx == -1:
        if start == len(case_list)-1:
            case_list[start], case_list[start-1] = case_list[start-1], case_list[start]
            num = ''.join(map(str, case_list))
            if cnt % 2 == 1:
                if number_dict.get(num) is not None:
                    can_number.append(num)
                    return
            solution(start + 1, cnt, num)
        else:
            if cnt % 2 == 1:
                if number_dict.get(prev_num) is not None:
                    can_number.append(prev_num)
                    return
            solution(start + 1, cnt, prev_num)

    else:
        case_list[start], case_list[switch_idx] = case_list[switch_idx], case_list[start]
        num = ''.join(map(str, case_list))
        solution(start + 1, cnt-1, num)

for tc in range(1, T+1):
    number, cnt = map(int, input().split())
    case_list = list(map(int, str(number)))
    number_dict = {}
    can_number = []
    start_num = ''.join(map(str, case_list))
    number_dict[start_num] = True
    solution(0, cnt, start_num)
    print(f'#{tc} {can_number[0]}')
