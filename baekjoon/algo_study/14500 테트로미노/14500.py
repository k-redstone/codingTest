import sys
input = sys.stdin.readline

def backtrack(row, col, sum_num, block_cnt):
    global max_num
    if block_cnt == 4:
        max_num = max(max_num, sum_num)
        return
    if max_num > sum_num + maxx * (4-block_cnt):
        return
    for idx in range(4):
        new_row = row + d_row[idx]
        new_col = col + d_col[idx]
        if 0 <= new_row < N and 0 <= new_col < M:
            if visited[new_row][new_col] == 0:
                visited[new_row][new_col] = 1
                backtrack(new_row, new_col, sum_num + case_matrix[new_row][new_col], block_cnt + 1)
                visited[new_row][new_col] = 0

def special_sum(row, col):
    global max_special
    for num in range(4):
        sum_num = 0
        for new_row, new_col in special[num]:
            special_row = row + new_row
            special_col = col + new_col
            if 0 <= special_row < N and 0 <= special_col < M:
                sum_num += case_matrix[special_row][special_col]
            else:
                break
        else:
            if sum_num > max_special:
                max_special = sum_num



d_row, d_col = [0, -1, 1, 0], [1, 0, 0, -1]
special =[
    [(0, 0), (0, 1), (0, 2), (-1, 1)],
    [(0, 0), (0, 1), (0, 2), (1, 1)],
    [(0, 0), (1, 0), (2, 0), (1, -1)],
    [(0, 0), (1, 0), (2, 0), (1, 1)],
]

N, M = map(int, input().split())
case_matrix = [list(map(int, input().split())) for _ in range(N)]
max_num = 0
max_special = 0
visited = [[0]*M for _ in range(N)]
maxx = max([max(i) for i in case_matrix])

for row in range(N):
    for col in range(M):
        visited[row][col] = 1
        backtrack(row, col, case_matrix[row][col] ,1)
        special_sum(row, col)
        visited[row][col] = 0

print(max(max_num, max_special))
