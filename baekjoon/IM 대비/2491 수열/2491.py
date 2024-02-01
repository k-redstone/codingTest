import sys
sys.stdin = open("./baekjoon/IM 대비/2491 수열/input.txt", "r")


N = int(sys.stdin.readline())
case_list = list(map(int, sys.stdin.readline().rstrip().split()))

asc = [1] * N
des = [1] * N

for i in range(N - 1):
    if case_list[i + 1] >= case_list[i]:
        asc[i + 1] += asc[i]
for i in range(N - 1):
    if case_list[i + 1] <= case_list[i]:
        des[i + 1] += des[i]

print(max([max(asc), max(des)]))
