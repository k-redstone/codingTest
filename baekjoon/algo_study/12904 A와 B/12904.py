import sys
sys.stdin = open("./baekjoon/12904 A와 B/input.txt", "r")

start = list(sys.stdin.readline().rstrip())
final = list(sys.stdin.readline().rstrip())

for _ in range(len(final), len(start), -1):
    if final[-1] == 'A':
        final.pop()
    else:
        final.pop()
        final = list(reversed(final))

if start == final:
    print(1)
else:
    print(0)