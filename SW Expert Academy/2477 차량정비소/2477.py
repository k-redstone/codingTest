import sys
from collections import deque
sys.stdin = open("./SW Expert Academy/2477 차량정비소/input.txt", "r")


# ① 여러 고객이 기다리고 있는 경우 고객번호가 낮은 순서대로 우선 접수한다.
# ② 빈 창구가 여러 곳인 경우 접수 창구번호가 작은 곳으로 간다.


# ① 먼저 기다리는 고객이 우선한다.
# ② 두 명 이상의 고객들이 접수 창구에서 동시에 접수를 완료하고 정비 창구로 이동한 경우, 이용했던 접수 창구번호가 작은 고객이 우선한다.
# ③ 빈 창구가 여러 곳인 경우 정비 창구번호가 작은 곳으로 간다.

class Reception():
    def __init__(self, count, time):
        self.que = deque()
        self.time = time
        self.usuage = [0]*count
        
    def waiting(self, person):
        self.que.append(person)

    def assign(self):
        if self.que:
            for idx in range(len(self.usuage)):
                if self.usuage[idx] == 0 and self.que:
                    person = self.que.popleft()
                    person[1] = idx+1
                    self.usuage[idx] = (self.time[idx], person)

    def using(self, repair):
        next_list = []
        for idx in range(len(self.usuage)):
            if self.usuage[idx] != 0:
                time, person = self.usuage[idx]
                new_time = time - 1
                if new_time == 0:
                    self.usuage[idx] = 0
                    next_list.append((person[1], person))
                    continue
                self.usuage[idx] = (new_time, person)

        if next_list:
            # print('move')
            repair.waiting(next_list)

class Repair():
    def __init__(self, count, time):
        self.que = deque()
        self.time = time
        self.num = 0
        self.usuage = [0]*count
        
    def waiting(self, arr):
        for item in arr:
            rece, person = item
            self.que.append((self.num, rece, person))
        self.que = deque(sorted(self.que, key=lambda x: (x[0], x[1])))
        self.num +=1

    def assign(self):
        if self.que:
            for idx in range(len(self.usuage)):
                if self.usuage[idx] == 0 and self.que:
                    num, rece, person = self.que.popleft()
                    person[2] = idx+1
                    self.usuage[idx] = (self.time[idx], person)
       

    def using(self):
        global end_num
        for idx in range(len(self.usuage)):
            if self.usuage[idx] != 0:
                time, person = self.usuage[idx]
                new_time = time -1
                if new_time == 0:
                    self.usuage[idx] = 0
                    end_arr.append(person)
                    continue
                self.usuage[idx] = (new_time, person)
            

def solution(person_idx, time, reception, repair):
    global end_num
    while end_num != len(end_arr):
        # print('시간', time, '대기', person_list)
        reception.using(repair)
        repair.using()
        while person_list and person_list[0] == time:
            person_list.popleft()
            reception.waiting([person_idx, 0, 0])
            person_idx += 1
        reception.assign()
        repair.assign()

        # print('시간', time)
        # print('접수중', reception.usuage)
        # print('정비중', repair.usuage)
        # print('---------------------------------')

        time += 1
        # if time == 10:
        #     break
    # print(end_arr)
    # print('ending')
    # pass




T = int(input())

for tc in range(1, T+1):
    N, M, K, A, B = map(int, input().split())
    reception_desk = list(map(int, input().split()))
    repair_desk = list(map(int, input().split()))
    reception = Reception(N, reception_desk)
    repair = Repair(M, repair_desk)


    person_list = deque(list(map(int, input().split())))
    end_num = len(person_list)
    end_arr = []
    solution(1, 0, reception, repair)

    result = 0
    # print(end_arr)
    for item in end_arr:
        if item[1] == A and item[2] == B:
            result += item[0]
    if result == 0:
        result = -1
    print(f'#{tc} {result}')