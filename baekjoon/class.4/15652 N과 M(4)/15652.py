import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
print_list = [1]*M
def backtrack(idx, start):
    if idx >= M:
        print(*print_list)
        return
    for num in range(start, N+1):
        print_list[idx] = num
        backtrack(idx+1, num)
        print_list[idx] = 1
backtrack(0, 1)