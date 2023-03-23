# https://www.acmicpc.net/problem/10988

import sys
sys.stdin = open("data.txt", "r")
input = sys.stdin.readline


input = list(str(input()))
if list(reversed(input)) == input:
    print(1)
else:
    print(0)
