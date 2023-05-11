# https://www.acmicpc.net/problem/25206

import sys
sys.stdin = open("data.txt", "r")
input = sys.stdin.readline

grade = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
score = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]

total = 0
majorSum = 0

for _ in range(20):
    major, majorScore, majorGrade = input().split()
    majorScore = float(majorScore)

    if majorGrade != 'P':
        total += majorScore
        majorSum += majorScore * score[grade.index(majorGrade)]

print('%.6f' % (majorSum/total))
