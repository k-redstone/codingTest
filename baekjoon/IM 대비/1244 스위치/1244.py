import sys
sys.stdin = open("./baekjoon/IM 대비/1244 스위치/input.txt", "r")

switch_num = int(sys.stdin.readline())
switch_list = list(map(int, sys.stdin.readline().split()))
student_num = int(sys.stdin.readline())

for _ in range(student_num):
    s, number = map(int, sys.stdin.readline().split())
    default_num = number
    if s == 1:
        while number <= switch_num:
            switch_list[number-1] = int(not switch_list[number-1])
            number += default_num
    else:
        for check in range(1, switch_num + 1):
            if 0 <= number-1-check < switch_num and 0 <= number-1+check < switch_num:
                if switch_list[number-1 - check] == switch_list[number-1+check]:
                    continue
            switch_list[number-1] = int(not switch_list[number-1])
            for re in range(1, check):
                switch_list[number-1-re] = int(not switch_list[number-1-re])
                switch_list[number-1+re] = int(not switch_list[number-1+re])
            break

for i in range(0, len(switch_list), 20):
	print(*switch_list[i:i+20])