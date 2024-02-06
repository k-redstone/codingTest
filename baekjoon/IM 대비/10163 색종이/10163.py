import sys
sys.stdin = open("./baekjoon/IM 대비/10163 색종이/input.txt", "r")

paper_num = int(sys.stdin.readline())
case_list = [list(map(int, input().split())) for _ in range(paper_num)]
max_list = []

for item in case_list:
    max_list.append(item[0] + item[2])
    max_list.append(item[1] + item[3])

width = max(max_list)
matrix = [[0]*(width+1) for _ in range(width)]

for idx, item in enumerate(case_list):
    for row in range(item[1], item[1] + item[3]):
        for col in range(item[0], item[0] + item[2]):
            matrix[row][col] = idx + 1

for num in range(1, paper_num+1):
    cnt = 0
    for row in matrix:
        cnt += row.count(num)
    print(cnt)