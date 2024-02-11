import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
print_list = [0]*M

def backtrack(idx):
    if idx >= M:
        print(*print_list)
        return
    for num in range(1, N+1):
        if num not in print_list:
            if num > print_list[idx-1]:
                print_list[idx] = num
                backtrack(idx+1)
                print_list[idx] = 0
backtrack(0)