import sys
# sys.stdin = open("./baekjoon/other/15649 N과 M(1)/input.txt", "r")

N, M = map(int, sys.stdin.readline().rstrip().split())

print_list = [0]*M

def backtrack(idx):
    if idx >= M:
        print(*print_list)
        return
    for num in range(1, N+1):
        if num not in print_list:
            print_list[idx] = num
            backtrack(idx+1)
            print_list[idx] = 0
backtrack(0)