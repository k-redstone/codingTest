import sys
sys.stdin = open("./SW Expert Academy/1220 magnetic/input.txt", "r")

for t in range(1, 11):
    input()
    matrix = [input().split() for _ in range(100)]
    trans_matrix = list(map(list, zip(*matrix)))
    cnt = sum((''.join(filter(None, map(lambda x: x.replace('0', ''), col)))).count('12') for col in trans_matrix)
    print(f'#{t} {cnt}')