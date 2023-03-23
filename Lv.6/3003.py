# https://www.acmicpc.net/problem/3003

import sys
sys.stdin = open("data.txt", "r")
input = sys.stdin.readline

basic = [1, 1, 2, 2, 2, 8]
input = input().split()

for i in range(6):
    print(basic[i] - int(input[i]))
