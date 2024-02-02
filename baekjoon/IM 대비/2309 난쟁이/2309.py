import sys
import itertools
sys.stdin = open("./baekjoon/IM 대비/2309 난쟁이/input.txt", "r")

p_list = []

for _ in range(9):
    p_list.append(int(sys.stdin.readline().rstrip()))

p_list.sort()
who = itertools.combinations(p_list, 7)

for item in who:
    if sum(item) == 100:
        print(*item, sep="\n")
        
        break