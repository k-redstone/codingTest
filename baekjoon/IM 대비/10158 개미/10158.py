import sys
sys.stdin = open("./baekjoon/IM 대비/10158 개미/input.txt", "r")

M, N = map(int, sys.stdin.readline().split())
col, row = map(int, sys.stdin.readline().split())
count = int(input())


col_list = []
row_list = []

for i in range(M):
    col_list.append(i)
for j in range(M, 0, -1):
    col_list.append(j)

for i in range(N):
    row_list.append(i)
for j in range(N, 0, -1):
    row_list.append(j)

col_count = col_list[(col+count) % (2*M)]
row_count = row_list[(row+count) % (2*N)]

print(col_count, row_count)