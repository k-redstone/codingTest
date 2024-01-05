import sys
sys.stdin = open("./SW Expert Academy/input.txt", "r")

caseSize = int(input())


def calc(num, smallCase, bigCase):
  resultList = []
  for i in range(num+1):
    result = 0
    for j in range(len(smallCase)):
        result += smallCase[j] * bigCase[i+j]
    resultList.append(result)
  return max(resultList)    
      
for count in range(caseSize):
  lenA, lenB = map(int, input().split())
  caseA = list(map(int, input().split()))
  caseB = list(map(int, input().split()))
  num = abs(lenA-lenB)
  if lenA <= lenB:
    print(f'#{count+1} {calc(num, caseA, caseB)}')
  else:
    print(f'#{count+1} {calc(num, caseB, caseA)}')
    