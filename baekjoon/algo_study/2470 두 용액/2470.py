import sys
input = sys.stdin.readline

N = int(input())
case_list = sorted(map(int, input().split()))
start_point = 0
end_point = N -1

min_num = 2000000000
cnt = 0
while start_point != N-1:
    if start_point == end_point:
        start_point += 1
        end_point = N-1
        continue
    sum_num = case_list[start_point] + case_list[end_point]
    if sum_num == 0:
        result_start, result_end = start_point, end_point
        break
    if abs(sum_num) < abs(min_num):
        min_num = sum_num
        result_start, result_end = start_point, end_point
    end_point -= 1
    cnt+=1
print(cnt)
print(case_list[result_start], case_list[result_end])