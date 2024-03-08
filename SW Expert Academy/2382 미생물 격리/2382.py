import sys
from collections import deque
sys.stdin = open("./SW Expert Academy/2382 미생물 격리/input.txt", "r")

T = int(input())
def change_direction(di):
    if di == 0:
        return 1
    if di == 1:
        return 0
    if di == 2:
        return 3
    if di == 3:
        return 2
    
def solution(cur_position):
    global M
    while M > 0:
        cur_position = deque(list(set(cur_position)))
        for _ in range(len(cur_position)):
            row, col = cur_position.popleft()
            bug_num, bug_di = case_matrix[row][col].popleft()
            new_row, new_col = row+d_row[bug_di], col+d_col[bug_di]
            
            if new_row == 0 or new_col == 0 or new_row == N-1 or new_col == N-1:
                bug_num = bug_num // 2
                if bug_num == 0:
                    continue
                else:
                    case_matrix[new_row][new_col].append([bug_num, change_direction(bug_di)])
                    cur_position.append((new_row, new_col))
            else:
                cur_position.append((new_row, new_col))
                case_matrix[new_row][new_col].append([bug_num, bug_di])


        for point in cur_position:
            row, col = point
            if len(case_matrix[row][col]) > 1:
                arr = sorted(case_matrix[row][col], key=lambda item: item[0], reverse=True)
                sum_bug = 0
                for bug in arr:
                    sum_bug += bug[0]
                case_matrix[row][col] = deque([[sum_bug, arr[0][1]]])

        M -= 1
    cur_position = deque(list(set(cur_position)))
    return cur_position


d_row, d_col = [-1, 1, 0, 0], [0, 0, -1, 1]

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    cur_position = deque()
    case_matrix = [[deque() for _ in range(N)]  for _ in range(N)]
    for i in range(K):
        row, col, num, di = map(int, input().split())
        cur_position.append((row, col))
        case_matrix[row][col].append([num, di-1])

    point_list = solution(cur_position)
    
    result = 0
    for point in point_list:
        row, col = point
        result += case_matrix[row][col][0][0]
    print(f'#{tc} {result}')