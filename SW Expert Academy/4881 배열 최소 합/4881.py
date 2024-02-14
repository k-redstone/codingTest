import sys
sys.stdin = open("./input.txt", "r")

T = int(input())

# def backtrack2(idx):
#     if idx == N:
#         sum_num = 0
#         for row, col in enumerate(arr):
#             sum_num += case_matrix[row][col-1]
#         sum_list.append(sum_num)
#         return
#     else:
#         for j in range(idx, N):
#             arr[idx], arr[j] = arr[j], arr[idx]
#             backtrack2(idx+1)
#             arr[idx], arr[j] = arr[j], arr[idx]


def backtrack(idx, num):
    global min_num
    if idx == N:
        if min_num > num:
            min_num = num
            return
    if num >= min_num:
        return
    for item in range(1, N+1):
        if item not in arr:
            arr[idx] = item
            backtrack(idx+1, num + case_matrix[idx][arr[idx]-1])
            arr[idx] = 0

for tc in range(1, T+1):
    N = int(input())
    case_matrix = [list(map(int, input().split())) for _ in range(N)]
    min_num = 100
    arr = [0]*N
    backtrack(0, 0)
    print(f'#{tc} {min_num}')