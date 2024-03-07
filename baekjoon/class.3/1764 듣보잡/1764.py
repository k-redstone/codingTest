import sys
from collections import defaultdict
input = sys.stdin.readline

name_dict = defaultdict(int)

N, M = map(int, input().rstrip().split())

for _ in range(N+M):
    name_dict[input().rstrip()] += 1

arr = list(sorted(filter(lambda item: item[1] == 2, name_dict.items()), key=lambda key: key[0]))
print(len(arr))
for item in arr:
    print(item[0])