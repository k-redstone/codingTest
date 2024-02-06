import sys
sys.stdin = open("./baekjoon/IM 대비/2563 색종이/input.txt", "r")


T = int(sys.stdin.readline())
matrix = [[0]*100 for _ in range(100)]
cnt = 0
for _ in range(T):
    col, row = map(int, sys.stdin.readline().split())
    for i in range(row, row+10):
        for j in range(col, col+10):
            if matrix[i][j] == 0:
                 matrix[i][j] = 1
                 cnt += 1

print(cnt)