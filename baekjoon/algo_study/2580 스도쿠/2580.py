import sys
sys.stdin = open("./baekjoon/algo_study/2580 스도쿠/input.txt", "r")
# input = sys.stdin.readline

# 체크하는것도 for문 돌리니까 시간초과가 나는건가? 하...
def check_row(row, num):
    return num not in case_matrix[row]

def check_col(col, num):
    return num not in (case_matrix[row][col] for row in range(9))


def check_square(row, col, num):
    row = row//3*3
    col = col//3*3
    return num not in (case_matrix[row+row_2][col+col_2] for row_2 in range(3) for col_2 in range(3))

# 이게 pop때문에 시간초과라고?? ㅠㅠㅠ
# 어캐 고치냐
def solution(idx):
    if idx == len(blank_list):
        for num in range(9):
            print(*case_matrix[num])
        exit()
    row = blank_list[idx][0]
    col = blank_list[idx][1]
    for num in range(1, 10):
        if check_row(row, num) and check_col(col, num) and check_square(row, col, num):
            case_matrix[row][col] = num
            solution(idx+1)
            case_matrix[row][col] = 0


case_matrix = [list(map(int, input().split())) for _ in range(9)]

blank_list = []
for row in range(9):
    for col in range(9):
        if case_matrix[row][col] == 0:
            blank_list.append((row, col))
solution(0)
