import sys
sys.stdin = open("./baekjoon/IM 대비/2669 면적구하기/input.txt", "r")

case_matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(4)]
max_num = 0
cnt = 0
for item in case_matrix:
    max_num = max(max(item), max_num)
draw_matrix = [[0] * max_num  for _ in range(max_num)]

for item in case_matrix:
    for row in range(item[1], item[3]):
        for col in range(item[0], item[2]):
            if draw_matrix[row][col] == 0:
                draw_matrix[row][col] = 1
                cnt += 1

print(cnt)