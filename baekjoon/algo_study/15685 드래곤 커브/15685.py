import sys
input = sys.stdin.readline

# 0: 왼쪽 (→)
# 1: 위 (↑)
# 2: 오른쪽 (←)
# 3: 아래 (↓)
# (idx+1)%4

def get_position(d, g):
    d_list = [d]
    for _ in range(g):
        for idx in range(len(d_list)-1, -1, -1):
            d_list.append((d_list[idx] + 1) % 4)
    return d_list

def count_square(arr):
    cnt = 0
    for item in arr:
        x, y = item
        temp = 0
        for idx in range(3):
            new_x, new_y = x+d_x[idx], y+d_y[idx]
            if (new_x, new_y) in arr:
                temp += 1
        if temp == 3:
            cnt += 1
    return cnt

d_x, d_y = [1, 1, 0], [0, 1, 1]
d_row, d_col = [0, -1, 0, 1], [1, 0, -1, 0]
N = int(input().rstrip())
case_list = [list(map(int, input().rstrip().split())) for _ in range(N)]
position_list = set()

for curve in case_list:
    col, row, d, g = curve
    position = get_position(d, g)
    position_list.add((col, row))
    for p in position:
        col, row = col+d_col[p], row+d_row[p]
        position_list.add((col, row))

print(count_square(position_list))