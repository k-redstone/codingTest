import sys
input = sys.stdin.readline

delta =[
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
    (-1, -1),
    (-1, 1),
    (1, -1),
    (1, 1)
]

# def check(row, col):
#     for item in delta:
#         temp_row, temp_col = row, col
#         while True:
#             temp_row , temp_col = temp_row + item[0], temp_col + item[1]
#             if 0 <= temp_row < N and 0 <= temp_col < N:
#                 if matrix[temp_row][temp_col] == 1:
#                     return False
#             else:
#                 break
#     return True


def backtrack(row):
    global cnt
    if row == N:
        cnt += 1
        return
    for col in range(N): 
        if not col_visit[col] and not left_visit[row + col] and not right_visit[row - col + N -1]:
            col_visit[col] = left_visit[row + col] = right_visit[row - col + N -1] = 1
            backtrack(row + 1)
            col_visit[col] = left_visit[row + col] = right_visit[row - col + N -1] = 0
            

N = int(input())
cnt = 0
col_visit = [0] * N
left_visit  = [0] * (2 * N - 1)
right_visit  = [0] * (2 * N - 1) 
backtrack(0)
print(cnt)