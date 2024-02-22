import sys
from collections import deque
sys.stdin = open("./input.txt", "r")

def solution(case):
    point_dict = {i: 0 for i in range(101)}
    Q = deque()
    for idx, item in enumerate(case):
        if item == 0:
            continue
        Q.append(idx)
        point_dict[idx] = (idx, item)
    temp = case
    while Q:
        point = Q.popleft()
        if point_dict[point][1] == 1:
            if point >= 99:
                temp[99] = 0
                continue
            if point_dict[point + 1] == 0:
                point_dict[point], point_dict[point + 1] = point_dict[point + 1], point_dict[point]
                temp[point], temp[point+1] = temp[point+1], temp[point]
                Q.append(point + 1)
                continue
        elif point_dict[point][1] == 2:
            if point <= 0:
                temp[0] = 0
                continue
            if point_dict[point - 1] == 0:
                point_dict[point], point_dict[point - 1] = point_dict[point - 1], point_dict[point]
                temp[point], temp[point-1] = temp[point-1], temp[point]
                Q.append(point - 1)
                continue
    return temp


for tc in range(1, 11):
    _ = input()
    case_matrix = [list(map(int, input().split())) for _ in range(100)]

    trans_matrix = [[] for _ in range(100)]
    for idx in range(100):
        trans_matrix[idx] = [case_matrix[row][idx] for row in range(100)]
    cnt = 0
    for case in trans_matrix:
        result = ''.join(map(str, solution(case)))
        cnt += result.count('12')
    print(f'#{tc} {cnt}')