import sys
sys.stdin = open("./input.txt", "r")

T = int(input())

def solution(row, col, idx):
    if idx >= 6:
        result.add(''.join(temp))
        return
    for num in range(4):
        new_row, new_col = row+d_row[num], col+d_col[num]
        if 0 <= new_row < 4 and 0 <= new_col < 4:
            temp[idx+1] = case_matrix[new_row][new_col]
            solution(new_row, new_col, idx+1)
            temp[idx+1] = 0



d_row, d_col = [-1, 1, 0, 0], [0, 0, -1, 1]
for tc in range(1, T+1):
    case_matrix = [list(input().split()) for _ in range(4)]
    result = set()
    for row in range(4):
        for col in range(4):
            temp = [0]*7
            temp[0] = case_matrix[row][col]
            solution(row, col, 0)
    print(f'#{tc} {len(result)}')