import sys
input = sys.stdin.readline

def post_order(node):
    if 1 <= node < len(tree):
        # print(node)
        post_order(node+1)
        post_order(node+2)
        print(tree[node])


tree = []
while True:
    try:
        node = [int(input()), ]
        tree.append(node)
    except:
        break

print(tree)

post_order(1)