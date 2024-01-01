import sys
sys.stdin = open("./SW Expert Academy/input.txt", "r")

listCount = int(input())

num = 1
for numList in range(listCount):
  lists = sorted(list(map(int, input().split())))
  print(f'#{num} {str(lists[-1])}')
  num +=1