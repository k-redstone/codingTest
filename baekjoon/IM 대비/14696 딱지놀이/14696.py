import sys
sys.stdin = open("./baekjoon/IM 대비/14696 딱지놀이/input.txt", "r")


N = int(sys.stdin.readline().rstrip())

def judge(num1, num2):
    if num1 > num2:
        return 'A'
    if num1 < num2:
        return 'B'
    if num1 == num2:
        return 'D'
    
def start(A_list, B_list):
    result = judge(A_list.count(4), B_list.count(4)) 
    if result == 'D':
        result = judge(A_list.count(3), B_list.count(3))
        if result == 'D':
            result = judge(A_list.count(2), B_list.count(2)) 

            if result == 'D':
                return judge(A_list.count(1), B_list.count(1))
            else:
                return result
        else:
            return result
    else:
        return result

for _ in range(N):
    A = list(map(int, sys.stdin.readline().rstrip().split()))
    B = list(map(int, sys.stdin.readline().rstrip().split()))
    A = A[1:]
    B = B[1:]
    print(start(A, B))
