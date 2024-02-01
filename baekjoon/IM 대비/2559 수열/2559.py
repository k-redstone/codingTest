import sys
sys.stdin = open("./baekjoon/IM 대비/2559 수열/input.txt", "r")


N, K = map(int, sys.stdin.readline().rstrip().split())
case_list = list(map(int, sys.stdin.readline().rstrip().split()))
sum_list = [sum(case_list[:K])]

for num in range(N - K):
    sum_list.append(sum_list[num] - case_list[num] + case_list[K + num])


print(max(sum_list))