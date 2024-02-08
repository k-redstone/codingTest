import sys
sys.stdin = open("./baekjoon/9935 문자열 폭발/input.txt", "r")

full_word = list(sys.stdin.readline().rstrip())
word = sys.stdin.readline().rstrip()


pointer = 0
stack = temp_list = []

while pointer < len(full_word):
    stack.append(full_word[pointer])
    if stack[-1] == word[-1] and len(stack) >= len(word):
        for num in range(len(word)):
            if stack[-1-num] != word[-1-num]:
                break
        else:
            for _ in range(len(word)):
                stack.pop()
        
    pointer += 1

if len(stack) == 0:
    print('FRULA')
else:
    print(''.join(stack))
