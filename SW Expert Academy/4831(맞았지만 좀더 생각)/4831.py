import sys
sys.stdin = open("input.txt", "r")

testSize = int(input())


def move(can_move, end_point, station_name):
    use_count = 0
    current_point = 0
    full = can_move

    # 충전할 수 있는 정류장 수 만큼 반복문
    for i in range(len(station_name)):
        # 현재 반복문이 마지막 정류장 일때
        if i == len(station_name)-1:
            # 마지막 충전소에서 (현재 위치 + 움직일 수 있는 범위)가 도착지보다 작으면
            # 마지막 충전소에서 기름넣고 출발
            if current_point + can_move < end_point:
                use_count += 1
                can_move = full
            # 마지막 충전소에서 움직일 수 있는 범위가 도칙지보다 크면
            # 충전횟수 리턴
            if current_point + can_move >= end_point:
                return use_count

        # 현재 충전소에서 (현재 위치 + max 기름양)이 다음 충전소보다 작다면
        # 중간에 충전을 못하므로 0을 리턴
        if current_point + full < station_name[i+1]:
            return 0

        # 현재 충전소에서 (현재 위치 + 움직일 수 있는 범위)가 다음 충전소보다 작으면
        # 현재 충전소에서 기름넣고 출발
        if current_point + can_move < station_name[i+1]:
            use_count += 1
            can_move = full
        current_point = station_name[i+1]
        can_move = can_move - (current_point - station_name[i])
    return use_count


for size in range(testSize):
    max_move, end_point, station_count = list(map(int, input().split()))
    station_name = list(map(int, input().split()))
    canMove = max_move
    station_name.insert(0, 0)
    result = move(canMove, end_point, station_name)
    print(f'#{size+1} {result}')
