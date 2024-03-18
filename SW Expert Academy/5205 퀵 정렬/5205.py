import sys
sys.stdin = open("./input.txt", "r")

T = int(input())

def sort(arr, low, high):
    if high <= low:
        return
    mid = partition(arr, low, high)
    sort(arr, low, mid - 1)
    sort(arr, mid, high)

def partition(arr, low, high):
    pivot = arr[(low + high) // 2]
    while low <= high:
        while arr[low] < pivot:
            low += 1
        while arr[high] > pivot:
            high -= 1
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            low, high = low + 1, high - 1
    return low

for tc in range(1, T+1):
    N = int(input())
    case_list = list(map(int, input().split()))
    sort(case_list, 0, N-1)

    print(f'#{tc} {case_list[N//2]}')