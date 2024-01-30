import sys
sys.stdin = open("input.txt", "r")

T = int(input())

def move(condition, stop):
    max_move, end_point, station_count = condition
    station_name = stop
    cur = 0
    full_charge = 0

    while cur < end_point:
        for move_count in range(max_move, 0, -1):
            if (cur + move_count) in station_name:
                cur += move_count
                full_charge += 1
                break
            if (cur + move_count) >= end_point:
                cur += move_count
                break
        else:
            full_charge = 0
            break
    return full_charge


for _ in range(T):
    result = move(list(map(int, input().split())), list(map(int, input().split())))
    print(f'#{_ + 1} {result}')
