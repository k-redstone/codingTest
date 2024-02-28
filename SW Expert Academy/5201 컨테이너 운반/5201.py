import sys
sys.stdin = open("./input.txt", "r")

T = int(input())

def solution():
    weight = 0
    while container_list and truck_list:
        container = container_list.pop()
        truck = truck_list.pop()
        if container > truck:
            truck_list.append(truck)
            continue
        else:
            weight += container
    return weight

for tc in range(1, T+1):
    N, M = map(int, input().split())
    container_list = list(sorted(map(int, input().split())))
    truck_list = list(sorted(map(int, input().split())))
    print(f'#{tc} {solution()}')