import sys
input = sys.stdin.readline

N = int(input())
case_list = sorted(map(int, input().split()))
start_point, end_point = 0, N -1
sum_list= []

while start_point != end_point:
    sum_num = case_list[start_point] + case_list[end_point]
    if sum_num > 0:
        sum_list.append((sum_num, case_list[start_point], case_list[end_point]))
        end_point -= 1
    if sum_num < 0:
        sum_list.append((sum_num, case_list[start_point], case_list[end_point]))
        start_point += 1
    if sum_num == 0:
        sum_list.append((sum_num, case_list[start_point], case_list[end_point]))
        break
sum_list = sorted(sum_list, key=lambda item: abs(item[0]))
print(sum_list[0][1], sum_list[0][2])