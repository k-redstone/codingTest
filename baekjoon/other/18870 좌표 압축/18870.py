import sys
input = sys.stdin.readline

N = int(input())
case_list = list(map(int, input().split()))
sort_list = sorted(set(case_list))
sort_dict = {}
for idx, item in enumerate(sort_list):
    sort_dict[item] = idx

for item in case_list:
    print(sort_dict[item], end=' ')