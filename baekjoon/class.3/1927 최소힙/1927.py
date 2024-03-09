import sys
import heapq
input = sys.stdin.readline


N = int(input().rstrip())

hq = []
for _ in range(N):
    num = int(input().rstrip())
    if num == 0:
        if len(hq) == 0:
            print('0')
            continue
        print(heapq.heappop(hq))
    else:
        heapq.heappush(hq, num)