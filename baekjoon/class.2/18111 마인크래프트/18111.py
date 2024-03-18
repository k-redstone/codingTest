import sys
# input = sys.stdin.readline
sys.stdin = open("./baekjoon/class.2/18111 마인크래프트/input.txt", "r")


# 제거
def method_1(matrix, maxi, inv):
    cnt = 0
    temp = matrix

    for idx in range(len(temp)):
        if temp[idx] == maxi:
            temp[idx] -= 1
            inv += 1
            cnt += 1
    return temp, inv, cnt*2

# 설치
def method_2(matrix, mini, inv):
    cnt = 0
    temp = matrix
    
    for idx in range(len(temp)):
        if temp[idx] == mini:
            temp[idx] += 1
            inv -= 1
            cnt += 1
    return temp, inv, cnt


N, M, B = map(int, input().rstrip().split())
matrix = []
for _ in range(N):
    matrix.extend(list(map(int, input().rstrip().split())))


max_default = 256
min_default = 0
time = 0


while True:
    max_height = max(matrix)
    min_height = min(matrix)

    if sum(matrix) == max_height*len(matrix):
        print(time, max_height)
        break

    check_1 = matrix.count(max_height)*2
    if matrix.count(min_height) <= B:
        check_2 = matrix.count(min_height)
        if check_1 >= check_2:
            matrix, B, time_temp = method_2(matrix, min_height, B)
        else:
            matrix, B, time_temp = method_1(matrix, max_height, B)
    else:
        matrix, B, time_temp = method_1(matrix, max_height, B)
    time += time_temp
