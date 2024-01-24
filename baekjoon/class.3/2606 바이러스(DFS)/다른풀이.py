import sys
sys.stdin = open("data.txt", "r")

com=int(input())
graph=[[] for i in range(com+1)]
print(graph)
num=int(input())
for i in range(num):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

print(graph)

visited=[0 for i in range(com+1)]
count=-1
def dfs(v):
    visited[v]=1
    global count
    count += 1
    for i in graph[v]:
        if(visited[i]==0):
            dfs(i)

dfs(1)
print(count)