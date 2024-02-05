import sys
sys.stdin = open("./baekjoon/IM 대비/2635 수 이어나가기/input.txt", "r")


N = int(sys.stdin.readline())

result = 0
for num in range(N//2, N):
    temp_list = [N]
    temp = num
    if N == 1:
        temp = 1
    while temp >= 0:
        temp_list.append(temp)
        temp = temp_list[-2] - temp
    if len(temp_list) > result:
        result = len(temp_list)
        result_list = temp_list

print(result)
print(*result_list)