import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
case_list = [input().rstrip() for _ in range(N)]

weight_dict = defaultdict(int)

for item in case_list:
    for idx in range(len(item)-1, -1, -1):
        weight_dict[item[idx]] += 10 ** (len(item) - idx)

sorted_weight = sorted(weight_dict.items(), key=lambda item: item[1], reverse=True)
key_dict = dict()
max_num = 9

for key, value in sorted_weight:
    key_dict[key] = max_num
    max_num -= 1

answer = 0
for item in case_list:
    result = ''
    for i in item:
        result += str(key_dict[i])
    answer += int(result)
print(answer)