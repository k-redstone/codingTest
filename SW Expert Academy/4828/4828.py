import sys
sys.stdin = open("./SW Expert Academy/input.txt", "r")

testSize = int(input())

for num in range (testSize):
  caseSize = int(input())
  caseList = list(map(int, input().split()))
  print(f'#{num+1} {max(caseList)-min(caseList)}')


