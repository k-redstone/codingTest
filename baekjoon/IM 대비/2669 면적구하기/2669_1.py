import sys
sys.stdin = open("./baekjoon/IM 대비/2669 면적구하기/input.txt", "r")

draw_set = set()

for _ in range(4):
    col_1, row_1, col_2, row_2 = map(int, sys.stdin.readline().split())
    for row in range(row_1, row_2):
        for col in range(col_1, col_2):
            draw_set.add((row, col))

print(len(draw_set))