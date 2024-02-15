import sys
from collections import deque
sys.stdin = open("./input.txt", "r")


def solution(case):
    while True:
        for num in range(1, 6):
            left_pop = case.popleft()
            if left_pop - num <= 0:
                case.append(0)
                return case
            case.append(left_pop - num)

for tc in range(1, 11):
    _ = input()
    case_list = deque(list(map(int, input().split())))
    result = solution(case_list)
    print(f'#{tc}', *result)
