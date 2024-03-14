import sys, heapq
input = sys.stdin.readline

N = int(input().rstrip())

hq = []
for _ in range(N):
    num = int(input().rstrip())

    if num == 0:
        if len(hq) == 0:
            print(0)
            continue
        pop_item = heapq.heappop(hq)
        print(pop_item[1])
    else:   
        heapq.heappush(hq, (-num, num))