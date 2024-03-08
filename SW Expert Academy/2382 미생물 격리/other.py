import sys
from collections import deque

sys.stdin = open("./SW Expert Academy/2382 미생물 격리/input.txt", "r")

T = int(input())

def change_direction(di):
    return {0: 1, 1: 0, 2: 3, 3: 2}[di]

def solution(cur_position):
    global M
    while M > 0:
        cur_position = set(cur_position)
        new_positions = set()

        for point in cur_position:
            row, col = point
            bug_num, bug_di = case_matrix[row][col].popleft()
            new_row, new_col = row + d_row[bug_di], col + d_col[bug_di]

            if 0 <= new_row < N and 0 <= new_col < N:
                new_positions.add((new_row, new_col))
                case_matrix[new_row][new_col].append([bug_num, bug_di])
            else:
                bug_num //= 2
                if bug_num > 0:
                    new_positions.add((new_row, new_col))
                    case_matrix[new_row][new_col].append([bug_num, change_direction(bug_di)])

        for point in new_positions:
            row, col = point
            if len(case_matrix[row][col]) > 1:
                max_bug = max(case_matrix[row][col], key=lambda x: x[0])
                case_matrix[row][col] = deque([max_bug])

        M -= 1

    return new_positions

d_row, d_col = [-1, 1, 0, 0], [0, 0, -1, 1]

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    cur_position = set()
    case_matrix = [[deque() for _ in range(N)] for _ in range(N)]

    for _ in range(K):
        row, col, num, di = map(int, input().split())
        cur_position.add((row, col))
        case_matrix[row][col].append([num, di - 1])

    point_list = solution(cur_position)

    result = 0
    for point in point_list:
        row, col = point
        result += case_matrix[row][col][0][0]

    print(f'#{tc} {result}')