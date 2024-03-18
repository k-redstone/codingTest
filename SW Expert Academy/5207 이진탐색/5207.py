import sys
sys.stdin = open("./input.txt", "r")

T = int(input())

def binary(item, arr):
    l = 0
    r = len(arr)-1
    # 왼쪽 1 오른쪽 2
    di = -1
    while l <= r:
        mid = (l+r) // 2
        if arr[mid] == item:
            return 1
        elif arr[mid] > item:
            if di == 2 or di == -1:
                di = 1
                r = mid - 1
            else:
                return 0
        elif arr[mid] < item:
            if di == 1 or di == -1:
                di = 2
                l = mid + 1
            else:
                return 0
    return 0

for tc in range(1, T+1):
    N, M = map(int, input().split())

    A_list = list(sorted(map(int, input().split())))
    B_list = list(map(int, input().split()))
    result = 0
    for item in B_list:
        result += binary(item, A_list)


    print(f'#{tc} {result}')