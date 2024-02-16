import sys
sys.stdin = open("./input.txt", "r")

def backtrack(row, col, flag):
    for num in range(4):
        new_row, new_col = row + d_row[num], col + d_col[num]
        if 0 <= new_row < 16 and 0 <= new_col < 16:
            if case_matrix[new_row][new_col] == '2':
                return True
            if case_matrix[new_row][new_col] == '0':
                case_matrix[row][col] = '1'
                flag = backtrack(new_row, new_col, flag)
                if case_matrix[new_row][new_col] == '2':
                    return True
                case_matrix[row][col] = '0'

    return flag


d_row, d_col = [0, 0, -1, 1], [1, -1, 0, 0]
for tc in range(1, 11):
    _ = input()
    case_matrix = [list(input()) for _ in range(16)]
    for row in range(16):
        for col in range(16):
            if case_matrix[row][col] == '3':
                start_row, start_col = row, col
                break
    print(f'#{tc} {int(backtrack(start_row, start_col, False))}')

