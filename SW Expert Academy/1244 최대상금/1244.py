import sys

sys.stdin = open("./input.txt", "r")

T = int(input())

def solution(cnt):
    if cnt == 0:
        can_number.append(''.join(map(str, case_list)))
        return
    for start in range(len(case_list)):
        for idx in range(start+1, len(case_list)):
            case_list[start], case_list[idx] = case_list[idx], case_list[start]
            num = ''.join(map(str, case_list))+str(cnt)
            if number_dict.get(num) is None:
                number_dict[num] = True
                solution(cnt-1)
            case_list[start], case_list[idx] = case_list[idx], case_list[start]

for tc in range(1, T+1):
    number, cnt = map(int, input().split())
    case_list = list(map(int, str(number)))
    number_dict = {}
    can_number = []
    solution(cnt)
    can_number = list(sorted(can_number, reverse=True))
    print(f'#{tc} {can_number[0]}')