import sys
sys.stdin = open("./baekjoon/IM 대비/13300 방배정/input.txt", "r")


N, K = map(int, sys.stdin.readline().split())

w_grade_list = [0] * 7
m_grade_list = [0] * 7

cnt = 0
for _ in range(N):
    S, Y = map(int, sys.stdin.readline().split())
    if S == 0:
        w_grade_list[Y] += 1
        if w_grade_list[Y] > K:
            w_grade_list[Y] -= K
            cnt += 1
    else:
        m_grade_list[Y] += 1
        if m_grade_list[Y] > K:
            m_grade_list[Y] -= K
            cnt += 1

for item in w_grade_list:
    if item > 0:
        cnt += 1
        
for item in m_grade_list:
    if item > 0:
        cnt += 1

print(cnt)