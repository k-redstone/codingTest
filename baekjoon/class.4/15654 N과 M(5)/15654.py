import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
case_list = sorted(list(map(int, input().split())))
print_list = [0]*M
def backtrack(idx):
    if idx >= M:
        print(*print_list)
        return
    for num in case_list:
        if num not in print_list:
            print_list[idx] = num
            backtrack(idx+1)
            print_list[idx] = 0
backtrack(0)