import sys
sys.stdin = open("./baekjoon/IM 대비/2116 주사위쌓기/input.txt", "r")


dice_num = int(sys.stdin.readline())
dice_list =[]
first_dice = list(map(int,sys.stdin.readline().split()))

for _ in range(1, dice_num):
    dice_list.append( list(map(int,sys.stdin.readline().split())))

p = {
    0: 5,
    1: 3,
    2: 4,
    3: 1,
    4: 2,
    5: 0,
}

max_list = []
for num in range(6):
    top = first_dice[num]
    except_first = first_dice[:]
    except_first[num] = 0
    except_first[p[num]] = 0 
    max_sum = max(except_first)
    for dice in dice_list:
        except_dice = dice[:]
        bottom_idx = except_dice.index(top)
        top_idx = p[bottom_idx]
        top = except_dice[top_idx]
        except_dice[bottom_idx] = 0
        except_dice[top_idx] = 0
        max_sum += max(except_dice)
    max_list.append(max_sum)


print(max(max_list))
