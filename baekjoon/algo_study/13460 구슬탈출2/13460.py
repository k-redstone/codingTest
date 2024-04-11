import sys
input = sys.stdin.readline

d_row = [1, -1, 0, 0]
d_col = [0, 0, -1, 1]


def move(row, col, delta):
    back = -1

    for cnt in range(1, 10):
        n_row, n_col = row+(d_row[delta]*cnt), col+(d_col[delta]*cnt)
        if matrix[n_row][n_col] == '#':
            return cnt + back
        if matrix[n_row][n_col] == 'O':
            return cnt
        if matrix[n_row][n_col] == 'R' or matrix[n_row][n_col] == 'B':
            back -= 1


def back(cnt, r_row,r_col, b_row, b_col):
    global result
    if (cnt, r_row,r_col, b_row, b_col) in visited:
        return
    visited.add((cnt, r_row,r_col, b_row, b_col))

    if cnt >= 11:
        return

    for idx in range(4):
        r_cnt = move(r_row, r_col, idx)
        b_cnt = move(b_row, b_col, idx)
        if r_cnt==0 and b_cnt==0:
            continue
        
        nr_row, nr_col = r_row+(d_row[idx]*r_cnt), r_col+(d_col[idx]*r_cnt)
        nb_row, nb_col = b_row+(d_row[idx]*b_cnt), b_col+(d_col[idx]*b_cnt)

        if matrix[nb_row][nb_col] == 'O':
            continue
        elif matrix[nr_row][nr_col] == 'O':
            result = min(cnt, result)
            return
        matrix[r_row][r_col], matrix[b_row][b_col]  = ".", "."
        matrix[nr_row][nr_col], matrix[nb_row][nb_col] = "R", "B"
        back(cnt+1, nr_row, nr_col, nb_row, nb_col)

        # 되돌리기
        matrix[nr_row][nr_col], matrix[nb_row][nb_col] = ".", "."
        matrix[r_row][r_col], matrix[b_row][b_col]  = "R", "B"


N, M = map(int, input().rstrip().split())
matrix = [list(input().rstrip()) for _ in range(N)]

result = 11
visited = set()

for row in range(N):
    for col in range(M):
        if matrix[row][col] == 'R':
            r_row, r_col = row, col
        if matrix[row][col] == 'B':
            b_row, b_col = row, col

back(1, r_row, r_col, b_row, b_col)

if result == 11:
    result = -1
print(result)