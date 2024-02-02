import sys
sys.stdin = open("./baekjoon/IM 대비/2605 줄세우기/input.txt", "r")


N = int(sys.stdin.readline().rstrip())

pick_num = list(map(int, sys.stdin.readline().rstrip().split()))
line_list = list(range(1, N + 1))

for num in range(len(pick_num)):
    if pick_num[num] == 0:
        continue
    else:
        temp_num = num
        for _ in range(pick_num[num]):
            line_list[temp_num], line_list[temp_num-1] = line_list[temp_num-1], line_list[temp_num]
            temp_num -= 1

print(*line_list)