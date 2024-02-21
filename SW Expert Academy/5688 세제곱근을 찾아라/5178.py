import sys
sys.stdin = open("./input.txt", "r")

T = int(input())

def binary_search(start, end, num):
    while start <= end:
        mod = (start+end) // 2
        temp = mod**3
        if temp == num:
            return mod
        elif temp < num:
            start = mod+1
        else:
            end = mod-1
    return -1

for tc in range(1, T+1):
    N = int(input())
    start = 1
    end = 1000000
    print(f'#{tc} {binary_search(start, end, N)}')