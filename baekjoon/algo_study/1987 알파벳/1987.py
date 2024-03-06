import sys
input = sys.stdin.readline

d_row, d_col = [-1, 1, 0, 0], [0, 0, -1, 1]

def backtrack(row, col, dist):
    global answer
    if case_matrix[row][col] in stack:
        answer = max(answer, dist)
        return
    
    stack.append(case_matrix[row][col])
    for idx in range(4):
        new_row, new_col = row+d_row[idx], col+d_col[idx]
        if 0 <= new_row < R and 0 <= new_col < C:
            backtrack(new_row, new_col, dist+1)
    stack.pop()

R, C = map(int, input().rstrip().split())
case_matrix = [list(input().rstrip()) for _ in range(R)]

stack = []
answer = 1
backtrack(0, 0, 0)
print(answer)