import sys
sys.stdin = open("data.txt", "r")


T = int(input())

for _ in range(T):
  test_list = list(input())

  stack = []
  for item in test_list:
    if len(stack) == 0:
      stack.append(item)
    else:
      if item == ")":
        if stack[-1] == "(":
          stack.pop()
        else:
          break
      else:
        stack.append(item)
  if len(stack) == 0:
    print(f"YES")
  else:
    print(f"NO")
    