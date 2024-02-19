import sys
input = sys.stdin.readline

N, M = map(int, input().split())
case_list = list(map(int, input().split()))
sum_num = 0
sum_list =[0]
for num in case_list:
    sum_num += num
    sum_list.append(sum_num)

for num in range(M):
    start_num, end_num = map(int, input().split())
    loop_num = end_num - start_num
    print(sum_list[end_num] - sum_list[start_num - 1])