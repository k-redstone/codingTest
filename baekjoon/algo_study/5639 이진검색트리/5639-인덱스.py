import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def solution(start, end):
    if start > end:
        return
    mid = end
    for idx in range(start+1, end+1):
        if case_list[start] < case_list[idx]:
            mid = idx-1
            break
    solution(start+1, mid)
    solution(mid+1, end)
    print(case_list[start], sep='\n')

case_list = []
while True:
    try:
        node = int(input())
        case_list.append(node)
    except:
        break

start = 0
end = len(case_list)-1
solution(start, end)